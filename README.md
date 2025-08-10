# bert-domestic-violence-risk-detector

A deep learning-powered application that uses BERT for detecting the risk of domestic violence from text, voice input, or uploaded audio files. The model classifies input into high, medium, or low risk levels and suggests appropriate actions.

<h1>Table of Contnets</h1>
<ul>
  <li><a href="">Features</a></li>
  <li><a href="">Model Architecture</a></li>
  <li><a href="">Dataset</a></li>
  <li><a href="">Installation</a></li>
  <li><a href="">Getting started</a></li>
  <li><a href="">Risk Interpretation</a></li>
  <li><a href="">Dependencies</a></li>
  <li><a href="">File Structure</a></li>
  <li><a href="">Ethical USe</a></li>
  <li><a href="">Contributing</a></li>
</ul>

# Features

🔤 Text Input Analysis – Type and evaluate messages for risk. 

🎙️ Voice Recording Support – Record your voice to assess speech.

🎧 Audio File Upload (MP3) – Upload an audio clip for risk analysis.

🤖 BERT-based Classification – Fine-tuned bert-base-uncased model.

📊 Risk Levels Output – High, Medium, or Low with probability score.

📈 Model Training & Validation – Includes complete training pipeline.

# Model Architecture
Tokenizer: bert-base-uncased

Model: BertForSequenceClassification

Training: Fine-tuned with labeled domestic violence dataset

Output: Binary classification (0 = low risk, 1 = high risk)

# Dataset
domestic_violence_data.csv – Training and validation data

text_test.csv – Testing data for evaluation

Labels:

0: Low Risk

1: High Risk

# Installation

*Clone the repository*

git clone https://github.com/VinayBR03/bert-domestic-violence-risk-detector.git

cd bert-domestic-violence-risk-detector

*Install dependencies*

pip install -r requirements.txt

# Getting Started
Run the main script in Google Colab or locally:

python main.py

Choose your preferred input method:

Type text directly

Record your voice

Upload an audio file
# Dependencies
pip install -r requirements.txt
# Getting Started
Run the main script in Google Colab or locally:

python main.py
Choose your preferred input method:

Type text directly

Record your voice

Upload an audio file

# Risk Interpretation



Score Range | Risk Level | Suggested Action

0.70 - 1.00 | High Risk | 🚨 Immediate intervention recommended

0.30 - 0.69 | Medium Risk | ⚠️ Monitor closely and provide support resources

0.00 - 0.29 | Low Risk | ✅ No immediate action, stay vigilant
# Dependencies
transformers

torch

sklearn

pandas

pydub

speechrecognition

IPython

tqdm

*Install via:*

pip install -r requirements.txt
# File Structure

.

├── main.py

├── domestic_violence_data.csv

├── text_test.csv

├── requirements.txt

└── README.md
# Ethical Use
This tool is intended to support professionals in assessing risks. It is not a replacement for certified mental health or legal advice.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

