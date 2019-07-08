from requests.auth import HTTPBasicAuth
import pprint
import requests
import json

def get_token():
    response = requests.post(
       "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token",
       auth=HTTPBasicAuth(
           username="devnetuser",
           password="Cisco123!"
       ),
      headers={'content-type': 'application/json'},
      verify=False,
    )
    token = response.json()["Token"]
    return token
