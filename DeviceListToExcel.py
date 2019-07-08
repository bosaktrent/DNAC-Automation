"""DeviceListToExcel.py: Presents a  list of network devices from DNAC in an excel spreadsheet"""
__author__ = "Trent Bosak"
__email__ = "tbosak@cisco.com"

from requests.auth import HTTPBasicAuth
import requests
import json
import tablib

def get_token():
    ip = "sandboxdnac.cisco.com"            # DNA Center cluser ip address
    response = requests.post(
       "https://{}/dna/system/api/v1/auth/token".format(ip),
       auth=HTTPBasicAuth(
           username="devnetuser",           # DNA Center username
           password="Cisco123!"             # DNA Center password
       ),
      headers={'content-type': 'application/json'},
      verify=False,
    )
    token = response.json()["Token"]
    return token

def get_device_list():
    ip = "sandboxdnac.cisco.com"            # DNA Center cluser ip address
    response = requests.get(
        "https://{}/dna/intent/api/v1/network-device/".format(ip),
        headers={
            "X-Auth-Token": get_token(),
            "Content-type": "application/json",
        },
        verify=False
    )
    return response.json()["response"]

def main():
    deviceList = json.dumps(get_device_list())
    data = tablib.Dataset()
    data.json = deviceList
    open('Device_List.xls', 'wb').write(data.xls)

if __name__ == '__main__':
    main()
