import requests

# First, login to get the token
login_url = "http://127.0.0.1:8000/login"
login_payload = {
    "email": "institution@trusted.dev",
    "password": "inst123"
}
login_headers = {
    "Content-Type": "application/json"
}

login_response = requests.post(login_url, json=login_payload, headers=login_headers)
if login_response.status_code == 200:
    token = login_response.json()["token"]
    print(f"Login successful. Token: {token}")
    
    # Now try to access the institution certificates endpoint
    cert_url = "http://127.0.0.1:8000/institution/certificates"
    cert_headers = {
        "Authorization": f"Bearer {token}"
    }
    
    cert_response = requests.get(cert_url, headers=cert_headers)
    print(f"Certificate endpoint status: {cert_response.status_code}")
    print(f"Certificate response: {cert_response.text}")
else:
    print(f"Login failed: {login_response.status_code} - {login_response.text}")