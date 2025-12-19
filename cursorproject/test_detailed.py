import sys
import os
import logging

# Configure logging to see debug messages
logging.basicConfig(level=logging.INFO)

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Import the functions directly
from backend.gemini_extractor import extract_certificate_data
from backend.ocr import extract_text_from_file, extract_structured_data

# Read the test certificate image
with open("test_certificate.png", "rb") as f:
    image_bytes = f.read()

print("=== Testing extract_certificate_data function ===")
extracted_data = extract_certificate_data(image_bytes, "test_certificate.png")
print("Extracted data from extract_certificate_data:")
print(extracted_data)
print(f"Student name: {extracted_data.get('student_name')}")

print("\n=== Testing extract_text_from_file function ===")
ocr_text = extract_text_from_file("test_certificate.png", image_bytes)
print("OCR text:")
print(ocr_text)

print("\n=== Testing extract_structured_data function ===")
structured_data = extract_structured_data(ocr_text)
print("Structured data:")
print(structured_data)
print(f"Name from structured data: {structured_data.get('name')}")