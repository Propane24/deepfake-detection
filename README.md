#  DeepShield – Real-Time Deepfake Detection Extension

> A browser-native AI system that detects deepfake images directly while browsing the web.

DeepShield integrates a custom-trained deep learning model with a Chrome extension to automatically analyze images on any webpage and detect AI-generated content in real time.

---

##  The Problem

Generative AI models can now create hyper-realistic fake images that are almost indistinguishable from real photographs.

However:

- Most detection tools require manual uploads  
- No built-in browser authenticity layer exists  
- Users cannot verify images while scrolling social media  
- Fake media spreads faster than verification  

DeepShield solves this by bringing detection directly into the browser.

---

##  The Solution

DeepShield combines:

-  Chrome Extension (Manifest V3)
-  FastAPI Inference Server
-  Custom CNN Model (trained from scratch)
-  Frequency-Domain Artifact Detection
-  Real-Time Image Interception

Instead of uploading images manually, the system:

```
Webpage → Extension → Backend → Model → Authenticity Score → Overlay
```

All in real time.

---

##  Architecture

```
┌─────────────────────────────┐
│        Web Browser          │
│  (Social Media / News etc.) │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Chrome Extension         │
│  - Detects <img> elements   │
│  - Captures image data      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      FastAPI Backend        │
│  - Receives image           │
│  - Preprocesses             │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Deep Learning Model       │
│  - CNN Spatial Analysis     │
│  - Frequency Domain Features│
│  - Binary Classification    │
└──────────────┬──────────────┘
               │
               ▼
      Authenticity Score
```

---

##  Key Features

###  Custom Model Trained From Scratch
- Built using PyTorch
- CNN-based architecture
- Binary classifier (Real vs Fake)
- Designed for fast inference

###  Multi-Signal Detection
The model analyzes:
- Spatial pixel patterns
- Frequency-domain artifacts (FFT)
- Learned fake-generation inconsistencies

###  Real-Time Browser Detection
- Automatically scans `<img>` elements
- Sends images to backend
- Displays authenticity results

###  Mixed Image Testing Page
Includes a local testing page with 10 mixed (real + AI) images for demo purposes.

---

##  Project Structure

```
deepfake-detection/
│
├── cnn_file/                # ML model code
│   ├── model.py
│   ├── train.py
│   ├── dataset.py
│   ├── frequency.py
│   └── main.py
│
├── testing/                 # Mixed image demo page
│   ├── index.html
│   └── images/
│        ├── img1.jpg
│        ├── img2.jpg
│        └── ... up to img10.jpg
│
├── extension/               # Chrome extension
│
└── README.md
```

---

##  Installation & Setup

### 1️. Clone Repository

```bash
git clone https://github.com/Propane24/deepfake-detection.git
cd deepfake-detection
```

---

### 2️. Install Dependencies

```bash
pip install fastapi uvicorn torch torchvision opencv-python pillow
```

---

### 3️. Start Backend

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

### 4️. Load Chrome Extension

1. Open `chrome://extensions`
2. Enable **Developer Mode**
3. Click **Load Unpacked**
4. Select the extension folder

---

### 5️. Test with Mixed Image Page

Open:

```
testing/index.html
```

The extension will automatically detect and analyze all 10 images.

---

##  API Endpoint

### POST `/analyze`

Returns:

```json
{
  "fake_probability": 0.82,
  "label": "FAKE",
  "confidence": 0.64
}
```

---

##  Hackathon Value Proposition

DeepShield shifts deepfake detection from:

> Manual Upload Verification  
> to  
> Ambient Real-Time Detection

It acts as a browser-level authenticity layer.

---

##  Scalability & Future Roadmap

- Video frame temporal detection  
- ONNX model optimization  
- Edge deployment  
- On-device lightweight model  
- Blockchain authenticity registry  
- Social media API integration  

---

##  Use Cases

- Social media verification  
- Journalism authenticity tools  
- Fraud prevention  
- Misinformation control  
- Digital forensics  

---

##  Team

Built collaboratively with contributions in:

- ML Model Development  
- Backend API  
- Chrome Extension  
- UI Testing  

---

##  License

MIT License
