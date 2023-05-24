import requests
import json
def get_token():
    url="https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    username="devnetuser"
    password="Cisco123!"
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
    }
    auth_payload = {
    "username": username,
    "password": password
    }
    response = requests.post(url,headers=headers, data=auth_payload,verify=False)
    print(response.text)
get_token()