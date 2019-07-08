from requests.auth import HTTPBasicAuth
import getToken
import pprint
import requests
import json

def get_device_from_dnac(device_ip):
    response = requests.get(
        "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/ip-address/{}".format(device_ip),
        headers={
            "X-Auth-Token": getToken.get_token(),
            "Content-type": "application/json",
        },
        verify=False
    )
    return response.json()

result = get_device_from_dnac("10.10.22.70")
print(pprint.pprint(result))
