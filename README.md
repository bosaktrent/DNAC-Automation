# Cisco DNA Center Automation scripts

This repository contains some simple scripts to get started with Cisco DNA Center API.

To get started you'll need to `install` the required modules and edit the default controller credentials shown below. 

*The credentials can be found in `if __name__ == '__main__':`*

    ip = "sandboxdnac.cisco.com"            # DNA Center cluser ip address
    username="devnetuser"                   # DNA Center username
    password="Cisco123!"                    # DNA Center password

## DeviceListToExcel.py

This script gets a list of network devices from Cisco DNA Center and presents them in an Excel spreadsheet. The default filename is `Device_List.xls` and will be saved in the same location as `DeviceListToExcel.py`.

### Requirements
* Python 3
* [Requests][requests_link]
* [Tablib][tablib_link]

[requests_link]: https://2.python-requests.org/en/master/
[tablib_link]: http://docs.python-tablib.org/en/master/

To run this script, run the command: `python3 DeviceListToExcel.py`
	