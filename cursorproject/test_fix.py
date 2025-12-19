import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.gemini_extractor import extract_certificate_data

# Test data that simulates what would come from a form
test_student_name = None  # This simulates an empty form field

# Read the test certificate image
with open("test_certificate.png", "rb") as f:
    image_bytes = f.read()

# Extract certificate data
print("Extracting certificate data...")
extracted_data = extract_certificate_data(image_bytes, "test_certificate.png")
print("Extracted data:")
print(extracted_data)

# Test the fixed logic
final_student_name = test_student_name if test_student_name is not None else extracted_data.get("student_name", "Unknown Name")
print(f"\nWith fixed logic, final student name would be: {final_student_name}")

# Test with a provided name
test_student_name = "Provided Name"
final_student_name = test_student_name if test_student_name is not None else extracted_data.get("student_name", "Unknown Name")
print(f"With provided name, final student name would be: {final_student_name}")