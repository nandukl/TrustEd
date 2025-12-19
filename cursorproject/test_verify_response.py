import requests
import json

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
    with open("test_certificate.png", "rb") as f:
        files = {"file": f}
        verify_headers = {
            "Authorization": f"Bearer {token}"
        }
        
        verify_response = requests.post(
            "http://127.0.0.1:8000/verify",
            headers=verify_headers,
            files=files
        )
        
        print(f"Verify status: {verify_response.status_code}")
        print("Verify response:")
        print(json.dumps(verify_response.json(), indent=2))
else:
    print(f"Login failed: {login_response.status_code} - {login_response.text}")