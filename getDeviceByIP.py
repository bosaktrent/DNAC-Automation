"""getDeviceByIP: Returns a device by IP address"""
__author__ = "Trent Bosak"
__email__ = "tbosak@cisco.com"

from requests.auth import HTTPBasicAuth
import getToken
import pprint
import requests
import json

def get_device_from_dnac(device_ip):
    ip = "sandboxdnac.cisco.com"            # DNA Center cluser ip address
    response = requests.get(
        "https://{}/dna/intent/api/v1/network-device/ip-address/{}".format(ip, device_ip),
        headers={
            "X-Auth-Token": getToken.get_token(),
            "Content-type": "application/json",
        },
        verify=False
    )
    return response.json()

result = get_device_from_dnac("10.10.22.70")
print(pprint.pprint(result))
