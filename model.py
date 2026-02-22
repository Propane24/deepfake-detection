import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import numpy as np
import cv2
import re


# ==============================
# LOAD CNN MODEL
# ==============================

model_name = "prithivMLmods/Deep-Fake-Detector-Model"

processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

model.eval()


# ==============================
# CNN SCORE
# ==============================

def cnn_score(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probs = torch.softmax(logits, dim=1)

    # Find FAKE label safely
    fake_index = None
    for idx, label in model.config.id2label.items():
        if "fake" in label.lower():
            fake_index = idx

    if fake_index is None:
        raise ValueError("Fake label not found in labels")

    return probs[0][fake_index].item()


# ==============================
# SHARPNESS
# ==============================

def sharpness_score(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    return laplacian.var()


# ==============================
# NOISE
# ==============================

def noise_score(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return np.var(img)


# ==============================
# DOM ANALYSIS (REAL IMPLEMENTATION)
# ==============================

def calculate_dom_score(image_url, page_html):
    score = 0.0

    if image_url:
        url = image_url.lower()

        suspicious_keywords = [
            "midjourney",
            "stable",
            "diffusion",
            "dalle",
            "openai",
            "ai",
            "generated",
            "huggingface"
        ]

        for keyword in suspicious_keywords:
            if keyword in url:
                score += 0.15

        # Base64 inline images
        if url.startswith("data:image"):
            score += 0.2

        # Suspicious filename
        filename = url.split("/")[-1]
        for keyword in suspicious_keywords:
            if keyword in filename:
                score += 0.15

    # Analyze page HTML context
    if page_html:
        text = page_html.lower()

        context_keywords = [
            "ai generated",
            "stable diffusion",
            "midjourney prompt",
            "created using ai",
            "generated artwork",
            "diffusion model"
        ]

        for keyword in context_keywords:
            if keyword in text:
                score += 0.2

        # Prompt pattern detection (very strong signal)
        if re.search(r"prompt\s*:", text):
            score += 0.2

    return min(score, 1.0)


# ==============================
# NORMALIZATION
# ==============================

def normalize_sharpness(value):
    return min(1.0, value / 4000)

def normalize_noise(value):
    return min(1.0, value / 6000)


# ==============================
# MAIN DETECTION FUNCTION
# ==============================

def detect(image_path, image_url=None, page_html=None):
    """
    image_path  → local downloaded image file
    image_url   → original image src from browser
    page_html   → full page HTML or surrounding text
    """

    # CNN
    cnn_fake = cnn_score(image_path)

    # CV signals
    sharp_raw = sharpness_score(image_path)
    noise_raw = noise_score(image_path)

    sharp_norm = normalize_sharpness(sharp_raw)
    noise_norm = normalize_noise(noise_raw)

    # DOM
    dom_score = calculate_dom_score(image_url, page_html)

    # FINAL FUSION
    final_score = (
        0.5 * cnn_fake +
        0.25 * dom_score +
        0.15 * sharp_norm +
        0.10 * noise_norm
    )

    prediction = "FAKE" if final_score > 0.5 else "REAL"

    return {
        "cnn_score": round(cnn_fake, 4),
        "sharpness": round(sharp_norm, 4),
        "noise": round(noise_norm, 4),
        "dom_score": round(dom_score, 4),
        "final_score": round(final_score, 4),
        "prediction": prediction
    }