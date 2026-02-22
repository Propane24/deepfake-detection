import numpy as np
import cv2

def extract_frequency(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fft = np.fft.fft2(gray)
    fft_shift = np.fft.fftshift(fft)

    magnitude = np.log(np.abs(fft_shift)+1)

    resized = cv2.resize(magnitude, (32,32))
    return resized.flatten()
