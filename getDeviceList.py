from requests.auth import HTTPBasicAuth
import requests
import json
import pprint
import getToken
import tablib

def get_device_list():
    response = requests.get(
        "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/",
        headers={
            "X-Auth-Token": getToken.get_token(),
            "Content-type": "application/json",
        },
        verify=False
    )
    return response.json()["response"]

deviceList = json.dumps(get_device_list())
data = tablib.Dataset()
data.json = deviceList

open('output.xls', 'wb').write(data.xls)
