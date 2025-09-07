from flask import Flask, render_template, request, redirect, url_for, session
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import speech_recognition as sr
from pydub import AudioSegment, effects
import os
import base64
from io import BytesIO

app = Flask(__name__)
app.secret_key = "your-secret-key"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---- Load trained BERT model ----
tokenizer = BertTokenizer.from_pretrained("saved_model")
model = BertForSequenceClassification.from_pretrained("saved_model")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# ---- Helpers ----
def analyze_user_input(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
    return probs[0][1].item()

def convert_to_pcm_wav(input_path, output_path, input_format=None):
    audio = AudioSegment.from_file(input_path, format=input_format) if input_format else AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio = effects.normalize(audio)
    audio.export(output_path, format="wav", codec="pcm_s16le")

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)
    except:
        return None

# ---- Routes ----
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        transcription = None
        result = None
        option = request.form.get("option")

        if option == "text":
            transcription = request.form.get("text_input")

        elif option == "file":
            file = request.files.get("audio_file")
            if file and file.filename:
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                wav_path = os.path.splitext(filepath)[0] + "_converted.wav"
                convert_to_pcm_wav(filepath, wav_path)
                transcription = transcribe_audio(wav_path)

        elif option == "record":
            recorded_data = request.form.get("recorded_audio")
            if recorded_data:
                header, encoded = recorded_data.split(",", 1)
                audio_bytes = BytesIO(base64.b64decode(encoded))
                temp_input = os.path.join(UPLOAD_FOLDER, "recorded.webm")
                with open(temp_input, "wb") as f:
                    f.write(audio_bytes.read())
                wav_path = os.path.join(UPLOAD_FOLDER, "recorded.wav")
                convert_to_pcm_wav(temp_input, wav_path, input_format="webm")
                transcription = transcribe_audio(wav_path)

        if transcription:
            score = analyze_user_input(transcription)
            if score >= 0.7:
                result = f"High Risk ({score:.2f}): Immediate intervention recommended."
            elif score >= 0.3:
                result = f"Medium Risk ({score:.2f}): Monitor closely and provide support."
            else:
                result = f"Low Risk ({score:.2f}): No immediate action required."
        else:
            result = "Could not process input or audio not clear."

        session["transcription"] = transcription
        session["result"] = result
        return redirect(url_for("index"))

    transcription = session.pop("transcription", None)
    result = session.pop("result", None)
    return render_template("index.html", result=result, transcription=transcription)

if __name__ == "__main__":
    app.run(debug=True)
