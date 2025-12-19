import sys
import os
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Import the upload function
from backend.main import upload_certificate
from backend.auth import TOKEN_TO_USER

# Mock the user
user = TOKEN_TO_USER["demo-token"]

# Read the test certificate image
with open("test_certificate.png", "rb") as f:
    image_bytes = f.read()

# Create a mock UploadFile
class MockUploadFile:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content
        self._file = None
    
    async def read(self):
        return self.content

# Create mock form fields (using defaults to simulate empty form)
student_id = None
student_name = None
institution_name = None
year = None
certificate_id = None

# Create mock file
file = MockUploadFile("test_certificate.png", image_bytes)

# Call the upload function
async def test_upload():
    print("Testing upload_certificate function directly...")
    try:
        # We need to handle the Form parameters correctly
        # In FastAPI, Form(None) means the parameter is optional
        # We'll pass the parameters as keyword arguments
        result = await upload_certificate(
            file=file,
            user=user,
            student_id=student_id,
            student_name=student_name,
            institution_name=institution_name,
            year=year,
            certificate_id=certificate_id
        )
        print("Result:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

# Run the test
asyncio.run(test_upload())