from gemini_extractor import extract_certificate_data
import os

# Read the test certificate image
with open("../test_certificate.png", "rb") as f:
    data = f.read()

result = extract_certificate_data(data, "test_certificate.png")
print(result)