import os
from backend.gemini_extractor import extract_certificate_data

# Read the test certificate image
with open("test_certificate.png", "rb") as f:
    image_bytes = f.read()

# Extract certificate data
extracted_data = extract_certificate_data(image_bytes, "test_certificate.png")
print("Extracted Data:")
print(extracted_data)