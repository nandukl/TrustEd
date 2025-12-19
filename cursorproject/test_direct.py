import sys
import os
import asyncio
from fastapi import UploadFile
from io import BytesIO

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Import the upload function
from backend.main import upload_certificate

# Create a mock user
mock_user = {
    "email": "institution@trusted.dev",
    "role": "institution",
    "name": "Demo Institution",
    "token": "demo-token"
}

# Read the test certificate image
with open("test_certificate.png", "rb") as f:
    file_content = f.read()

# Create a mock file
file_bytes = BytesIO(file_content)
file_bytes.name = "test_certificate.png"

# Create an UploadFile object
upload_file = UploadFile(filename="test_certificate.png", file=file_bytes)

# Call the upload function with None values for Form parameters
async def test_upload():
    try:
        result = await upload_certificate(
            file=upload_file,
            student_id=None,
            student_name=None,
            institution_name=None,
            year=None,
            certificate_id=None,
            user=mock_user
        )
        print("Upload result:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")

# Run the test
asyncio.run(test_upload())