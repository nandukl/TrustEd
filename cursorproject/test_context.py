import sys
import os

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.gemini_extractor import extract_certificate_data

# Read the test certificate image
with open("test_certificate.png", "rb") as f:
    image_bytes = f.read()

# Extract certificate data
print("Extracting certificate data...")
extracted_data = extract_certificate_data(image_bytes, "test_certificate.png")
print("Extracted data:")
print(extracted_data)