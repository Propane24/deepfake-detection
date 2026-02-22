🛡️ Deepfake Detection Extension
Real-time authenticity detection for the modern web

A browser-native system that detects AI-generated media while you browse — no uploads, no manual checks, just instant trust signals.

🚀 Why this exists

Generative AI can now produce hyper-realistic fake media.
But users still rely on manual tools to verify authenticity.

This project introduces a real-time authenticity layer directly inside the browser.

While scrolling through social media, news, or videos:

images are analyzed instantly

authenticity scores are computed

trust indicators appear on screen

All without interrupting the user experience.

🧠 What it does

Detects deepfake images directly in webpages

Extracts frames from videos for analysis

Runs forensic AI models in real time

Generates probabilistic authenticity scores

Overlays trust badges on media

Works while browsing normally

No uploads.
No external tools.
No friction.

🏗️ Architecture Overview
        ┌─────────────────────────┐
        │   Browser Extension     │
        │                         │
        │  Detects images/videos  │
        └──────────┬──────────────┘
                   │
                   ▼
        ┌─────────────────────────┐
        │   Frame/Image Capture   │
        │   (Canvas API)          │
        └──────────┬──────────────┘
                   │
                   ▼
        ┌─────────────────────────┐
        │   Backend API (FastAPI) │
        │                         │
        │  Deepfake model         │
        │  Frequency analysis     │
        │  Metadata checks        │
        └──────────┬──────────────┘
                   │
                   ▼
        ┌─────────────────────────┐
        │ Authenticity Score      │
        └──────────┬──────────────┘
                   │
                   ▼
        ┌─────────────────────────┐
        │ Overlay on Webpage      │
        └─────────────────────────┘
⚡ Core Features
🧩 Browser-Native Detection

Detects deepfakes directly inside webpages using a Chrome extension.

🧠 Multi-Signal AI Analysis

Instead of relying on one model, the system combines:

CNN deepfake classifier

frequency-domain artifact detection

metadata consistency checks

🎯 Probabilistic Trust Score

Each image/video receives a confidence score:

REAL   ←──── 0.0 — 1.0 ────→   FAKE
🎥 Video Frame Analysis

Extracts frames periodically and checks temporal consistency.

🟢 Real-Time Overlay UI

Badges appear directly on media:

🔴 Fake

🟢 Likely Real

🟡 Suspicious

🛠️ Tech Stack
Extension

Chrome Extension (Manifest v3)

JavaScript

HTML/CSS

Canvas API

MutationObserver

Backend

Python

FastAPI

PyTorch

OpenCV

REST API

AI Detection

CNN deepfake classifier

frequency-domain artifact detection

multi-signal scoring engine

📂 Project Structure
deepfake-detection/
│
├── extension/
│   ├── manifest.json
│   ├── content.js
│   ├── overlay.js
│   └── styles.css
│
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── scoring.py
│   └── requirements.txt
│
├── assets/
│   ├── demo.gif
│   └── screenshots/
│
└── README.md
⚙️ Local Setup
Clone repo
git clone https://github.com/YOUR_USERNAME/deepfake-detection.git
cd deepfake-detection
Start backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Backend runs at:

http://localhost:8000
Load extension

Open Chrome

Go to chrome://extensions

Enable Developer Mode

Click Load unpacked

Select extension/ folder

🧪 Example API Response
{
  "fake_probability": 0.78,
  "confidence": 0.91,
  "label": "FAKE"
}
🎯 Use Cases

Detect AI-generated misinformation

Journalist verification tools

Social media authenticity checks

Fraud & impersonation prevention

Digital forensics

📊 Scoring Strategy

Final authenticity score is computed using multiple signals:

Final Score =
0.6 × CNN prediction +
0.3 × frequency artifacts +
0.1 × metadata checks

This improves reliability compared to single-model detection.

🔮 Future Roadmap

On-device lightweight inference

Edge deployment

Blockchain authenticity verification

Temporal video analysis

Cross-browser support

Social media API integration

🏆 Built For

Hackathons

AI safety research

Browser security tools

Real-time media verification

👥 Team

Team RDR2

Extension Development

ML Model

Backend & Integration

💡 Key Innovation

Most deepfake tools require manual uploads.
This system moves detection into the browsing layer.

Verification becomes ambient.
Always running.
Always visible.

📜 License

MIT License
