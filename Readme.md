# Domestic Violence Risk Detector

This project is a web application for analyzing the risk of domestic violence from text or audio input. It uses a fine-tuned BERT model for sequence classification.

## Features

- **Text Analysis:** Enter text to assess risk.
- **Audio File Upload:** Upload an audio file (e.g., .wav, .mp3, .webm) for transcription and risk analysis.
- **Live Audio Recording:** Record audio in-browser for analysis.
- **Risk Levels:** Returns High, Medium, or Low risk with recommendations.

## Folder Structure

```
.
├── app.py
├── Domestic_Violence_Risk_Detector.ipynb
├── domestic_violence_data.csv
├── text_test.csv
├── requirements.txt
├── LICENSE
├── README.md
├── saved_model/
│   ├── config.json
│   ├── model.safetensors
│   ├── special_tokens_map.json
│   ├── tokenizer_config.json
│   └── vocab.txt
├── templates/
│   └── index.html
└── uploads/
    ├── recorded.wav
    └── recorded.webm
```

## Setup

### 1. Install Dependencies

Run the following command to install required packages:

```sh
pip install -r reqiurements.txt
```

### 2. Model Training (Optional)

See [`Domestic_Violence_Risk_Detector.ipynb`](Domestic_Violence_Risk_Detector.ipynb) for training and evaluation. The notebook fine-tunes a BERT model on `domestic_violence_data.csv` and saves it to [`saved_model/`](saved_model).

### 3. Running the Web App

Start the Flask server:

```sh
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Usage

- Choose input type: Text, Upload Audio File, or Record Live Audio.
- Submit your input.
- The app transcribes audio (if needed) and analyzes risk using the trained BERT model.
- Results and transcriptions are displayed.

## Files

- [`app.py`](app.py): Flask application source.
- [`templates/index.html`](templates/index.html): Web interface.
- [`saved_model/`](saved_model): Fine-tuned BERT model and tokenizer files.
- [`uploads/`](uploads): Stores uploaded and recorded audio files.
- [`Domestic_Violence_Risk_Detector.ipynb`](Domestic_Violence_Risk_Detector.ipynb): Model training and evaluation notebook.

## Data

- `domestic_violence_data.csv`: Training and validation data.
- `text_test.csv`: Independent test data.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Transformers](https://github.com/huggingface/transformers)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pydub](https://github.com/jiaaro/pydub)