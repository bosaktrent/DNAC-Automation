"""getToken.py: Gets an authentication token from DNAC"""
__author__ = "Trent Bosak"
__email__ = "tbosak@cisco.com"
from requests.auth import HTTPBasicAuth
import pprint
import requests
import json

def get_token():
    ip = "sandboxdnac.cisco.com"            # DNA Center cluster ip address
    response = requests.post(
       "https:///dna/system/api/v1/auth/token",
       auth=HTTPBasicAuth(
           username="devnetuser",           # DNA Center username
           password="Cisco123!"             # DNA Center password
       ),
      headers={'content-type': 'application/json'},
      verify=False,
    )
    token = response.json()["Token"]
    return token
