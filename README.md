# Cisco DNA Center Automation scripts

This repository contains some simple scripts to get started with Cisco DNA Center API.

To get started you'll need to `install` the required modules and edit the default controller credentials shown below. 

Found in `if __name__ == '__main__':`

    ip = "sandboxdnac.cisco.com"            # DNA Center cluser ip address
    username="devnetuser"                   # DNA Center username
    password="Cisco123!"                    # DNA Center password

## DeviceListToExcel.py

This script will get a list of network devices from Cisco DNA Center and present them in an Excel spreadsheet.

### Requirements
* Python 3
* [Requests][requests_link]
* [Tablib][tablib_link]

[requests_link]: https://2.python-requests.org/en/master/
[tablib_link]: http://docs.python-tablib.org/en/master/

	python3 DeviceListToExcel.py
	