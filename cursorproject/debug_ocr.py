import os
from backend.ocr import extract_text_from_file, extract_structured_data

# Read the test certificate image
with open("test_certificate.png", "rb") as f:
    image_bytes = f.read()

# Extract text using OCR
ocr_text = extract_text_from_file("test_certificate.png", image_bytes)
print("OCR Text:")
print(ocr_text)
print("\nStructured Data:")
structured_data = extract_structured_data(ocr_text)
print(structured_data)