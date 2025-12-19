import requests

# First, login to get the token
login_url = "http://127.0.0.1:8000/login"
login_payload = {
    "email": "verifier@trusted.dev",
    "password": "verify123"
}
login_headers = {
    "Content-Type": "application/json"
}

login_response = requests.post(login_url, json=login_payload, headers=login_headers)
if login_response.status_code == 200:
    token = login_response.json()["token"]
    print(f"Login successful. Token: {token}")
    
    # Now try to verify a certificate
    # We'll create a simple text file for testing
    with open("test_certificate.txt", "w") as f:
        f.write("This is a test certificate for verification.")
    
    verify_url = "http://127.0.0.1:8000/verify"
    verify_headers = {
        "Authorization": f"Bearer {token}"
    }
    
    with open("test_certificate.txt", "rb") as f:
        files = {"file": f}
        verify_response = requests.post(verify_url, headers=verify_headers, files=files)
        print(f"Verification status: {verify_response.status_code}")
        print(f"Verification response: {verify_response.text}")
else:
    print(f"Login failed: {login_response.status_code} - {login_response.text}")