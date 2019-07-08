#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""getToken.py: Gets an authentication token from DNAC

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

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
