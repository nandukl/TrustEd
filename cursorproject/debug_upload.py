import os
import sys
import json
from backend.gemini_extractor import extract_certificate_data

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Read the test certificate image
with open("test_certificate.png", "rb") as f:
    image_bytes = f.read()

# Extract certificate data
print("Extracting certificate data...")
extracted_data = extract_certificate_data(image_bytes, "test_certificate.png")
print("Extracted data:")
print(json.dumps(extracted_data, indent=2))

# Show what would be used for final values
student_name = None  # Simulating no user input
institution_name = None  # Simulating no user input
year = None  # Simulating no user input
certificate_id = None  # Simulating no user input

final_student_name = student_name or extracted_data.get("student_name", "Unknown Name")
final_institution_name = institution_name or extracted_data.get("institution_name", "Unknown Institution")
final_year = year or extracted_data.get("year", 2025)
final_certificate_id = certificate_id or extracted_data.get("certificate_id", "AUTO-99999")

print("\nFinal values that would be used:")
print(f"Student Name: {final_student_name}")
print(f"Institution Name: {final_institution_name}")
print(f"Year: {final_year}")
print(f"Certificate ID: {final_certificate_id}")