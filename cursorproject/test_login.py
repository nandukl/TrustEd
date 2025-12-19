import requests
import json

url = "http://127.0.0.1:8000/login"
payload = {
    "email": "institution@trusted.dev",
    "password": "inst123"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")