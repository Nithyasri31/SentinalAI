# SentinelAI 🛡️

### AI-Powered Public Safety & Fraud Detection Platform

> **SentinelAI** is an AI-powered platform designed to enhance public safety by detecting and analyzing cyber threats such as voice scams, phishing messages, financial fraud, and fraud networks. The platform combines Artificial Intelligence, Machine Learning, Speech Processing, and Data Visualization to provide intelligent threat detection and actionable insights.

---

# 📌 Problem Statement

Cybercrime is increasing rapidly, with scams such as voice phishing, financial fraud, phishing emails, counterfeit identities, and digital arrest scams causing significant financial and emotional losses. Existing solutions are often reactive and focus on a single threat type, making it difficult to detect complex cyber attacks in real time.

SentinelAI addresses this challenge by providing a unified AI-powered platform capable of analyzing multiple sources of information, identifying suspicious activities, and assisting users in making informed decisions before becoming victims of cyber fraud.

---

# 🎯 Objectives

* Detect voice-based scam calls using AI.
* Identify phishing and spam messages.
* Monitor financial transactions for fraudulent activity.
* Visualize fraud networks and suspicious relationships.
* Increase public awareness about cyber threats.
* Provide a centralized AI-powered fraud detection platform.

---

# ✨ Features

## 🎤 Voice Scam Detection

* Speech-to-Text conversion
* AI-powered transcript analysis
* Scam probability detection
* Upload MP3, WAV, M4A, and MP4 audio files

---

## 📧 Scam Message Detection

* Detect phishing emails
* SMS spam detection
* Fake investment scam identification
* AI-generated risk assessment

---

## 📊 Financial Fraud Dashboard

* Transaction monitoring
* Fraud statistics
* Interactive charts
* Bank-wise fraud analysis
* Downloadable reports

---

## 🕸 Fraud Network Analysis

* Visualize suspicious relationships
* Detect fraud rings
* Network graph visualization
* Entity connection analysis

---

## 🤖 AI Assistant

* Cybersecurity awareness
* Scam identification assistance
* Threat explanation
* Public safety guidance

---

# 🏗 Project Architecture

```text
                    SentinelAI
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
 Voice Analysis     Scam Detection     Fraud Dashboard
                                              │
                                              │
                                    Fraud Network Analysis
                                              │
                                              │
                                     AI Threat Insights
```

---

# 🛠 Technology Stack

## Frontend

* Streamlit
* HTML
* CSS

## Backend

* Python

## Artificial Intelligence

* Google Gemini API
* Whisper Speech-to-Text

## Machine Learning

* Scikit-learn
* Pandas
* NumPy

## Data Visualization

* Plotly
* Matplotlib

## Others

* NetworkX
* Git
* GitHub

---

# 📂 Project Structure

```text
SentinelAI/
│
├── assets/
├── data/
├── docs/
├── models/
├── outputs/
├── pages/
│   ├── dashboard.py
│   ├── fraud_network.py
│   ├── scam_detection.py
│   └── voice_analysis.py
│
├── uploads/
│
├── utils/
│   ├── gemini_utils.py
│   ├── speech_utils.py
│   └── ...
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/SentinelAI.git
```

Move into the project

```bash
cd SentinelAI
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Modules

## 🏠 Home

Provides an overview of SentinelAI, project objectives, problem statement, and navigation to all modules.

### 🎤 Voice Scam Detector

Uploads audio recordings, converts speech to text, and uses AI to determine whether the conversation contains scam indicators.

### 📧 Scam Detection

Analyzes suspicious emails or messages and identifies phishing attempts, spam content, and social engineering attacks.

### 📊 Fraud Dashboard

Displays fraud analytics using interactive charts, transaction summaries, KPIs, and downloadable reports.

### 🕸 Fraud Network

Visualizes relationships between fraudulent entities to identify suspicious patterns and fraud rings.

---

# 👥 Team Roles

| Module                    | Responsibility                          |
| ------------------------- | --------------------------------------- |
| 🎤 Voice Scam Detection   | Speech-to-Text and AI scam analysis     |
| 📧 Scam Detection         | Phishing and spam message analysis      |
| 📊 Fraud Dashboard        | Fraud monitoring and data visualization |
| 🕸 Fraud Network Analysis | Fraud relationship visualization        |

---

# 📈 Future Enhancements

* Live scam call detection
* Real-time banking fraud alerts
* AI-powered chatbot
* Deepfake voice detection
* Multilingual support
* Mobile application
* Real-time public safety dashboard
* Integration with law enforcement systems

---

# 🔒 Security

* Secure file uploads
* AI-assisted threat analysis
* No permanent storage of uploaded files
* Privacy-focused processing
* Modular architecture for secure deployment

---

# 🌍 Applications

* Financial Institutions
* Government Agencies
* Law Enforcement
* Educational Institutions
* Cybersecurity Organizations
* General Public

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📜 License

This project is developed for educational, research, and hackathon purposes. Feel free to modify and extend it according to your requirements.

---

# ⭐ Acknowledgements

* OpenAI
* Google Gemini API
* OpenAI Whisper
* Streamlit
* Plotly
* Scikit-learn
* Pandas
* NumPy

---

## 🛡️ SentinelAI

**"Empowering Public Safety through Artificial Intelligence."**
