import requests
import time

# Test the upload certificate endpoint to verify our fix
def test_certificate_upload():
    print("Testing certificate upload with OCR fix...")
    
    # First, authenticate to get a token
    login_url = "http://127.0.0.1:8000/login"
    login_data = {
        "email": "institution@trusted.dev",
        "password": "inst123"
    }
    
    try:
        login_response = requests.post(login_url, json=login_data)
        if login_response.status_code != 200:
            print(f"❌ ERROR: Failed to authenticate - {login_response.json()}")
            return
            
        token = login_response.json()["token"]
        print(f"✅ Authenticated successfully with token: {token}")
        
        # URL of the backend API
        url = "http://127.0.0.1:8000/institution/upload-certificate"
        
        # Read the test certificate image
        with open("test_certificate.png", "rb") as f:
            files = {"file": ("test_certificate.png", f, "image/png")}
            headers = {"Authorization": f"Bearer {token}"}
            
            # Make the request without providing form fields
            # This should trigger the OCR extraction
            response = requests.post(url, files=files, headers=headers)
            
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
            
            # Check if the extracted data is being used correctly
            response_data = response.json()
            if response_data.get("success"):
                student_name = response_data.get("student_name")
                print(f"Extracted student name: {student_name}")
                
                if student_name and student_name != "Unknown Name":
                    print("✅ SUCCESS: OCR extraction is working correctly!")
                    print(f"✅ Student name '{student_name}' was extracted and used")
                else:
                    print("❌ ISSUE: Still showing 'Unknown Name'")
            else:
                print(f"❌ ERROR: {response_data.get('message')}")
                
    except FileNotFoundError:
        print("❌ ERROR: test_certificate.png not found")
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")

if __name__ == "__main__":
    test_certificate_upload()