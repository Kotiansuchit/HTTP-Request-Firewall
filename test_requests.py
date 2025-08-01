import requests

# Your firewall server URL
URL = "http://localhost:8080"

# Malicious payload simulating Spring4Shell attack
malicious_payload = {
    "class.module.classLoader.resources.context.parent.pipeline.first.pattern": "malicious pattern",
    "suffix": "%>//",
    "c1": "Runtime",
    "c2": "<%",
    "directory": "webapps/ROOT",
    "prefix": "tomcatwar",
    "suffix2": ".jsp"
}

# Clean (non-malicious) payload
clean_payload = {
    "username": "admin",
    "password": "securepassword123"
}

def send_request(payload, label):
    print(f"\nSending {label} request...")
    response = requests.post(URL, data=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

if __name__ == "__main__":
    send_request(malicious_payload, "MALICIOUS")
    send_request(clean_payload, "CLEAN")
