# Background Removal and Masking Using Computer Vision

## Overview
This project demonstrates real-time background removal and masking using computer vision techniques with Python and OpenCV. The system captures live webcam video, detects the foreground object, generates a mask, and removes or replaces the background dynamically.

The project is designed as a beginner-friendly implementation of real-time image processing and segmentation concepts.

---

## Features
- Real-time webcam processing
- Background subtraction using OpenCV
- Foreground masking
- Noise reduction using morphological operations
- Live background removal
- Simple and lightweight implementation

---

## Technologies Used
- Python
- OpenCV
- NumPy

---

## System Workflow
1. Capture live webcam feed
2. Process frames using OpenCV
3. Detect foreground using background subtraction
4. Generate foreground mask
5. Remove noise from mask
6. Extract foreground object
7. Display background removed output

---

## Installation

Install required libraries:

```bash
pip install opencv-python numpy
