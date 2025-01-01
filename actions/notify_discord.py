import requests

def run(webhook_url, message):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    return {"status": response.status_code, "response": response.text}