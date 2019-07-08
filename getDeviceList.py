"""getDeviceList.py: Returns a list of devices on DNAC"""
__author__ = "Trent Bosak"
__email__ = "tbosak@cisco.com"

from requests.auth import HTTPBasicAuth
import requests
import json
import pprint
import getToken
import tablib

def get_device_list():
    ip = "sandboxdnac.cisco.com"            # DNA Center cluser ip address
    response = requests.get(
        "https://{}/dna/intent/api/v1/network-device/".format(ip),
        headers={
            "X-Auth-Token": getToken.get_token(),
            "Content-type": "application/json",
        },
        verify=False
    )
    return response.json()["response"]
