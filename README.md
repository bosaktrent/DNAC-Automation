# Cisco DNA Center Automation scripts

This repository contains some simple scripts to get started with Cisco DNA Center API.

It also contains some scripts for simple use cases.

Before you get started you'll need to edit the controller credentials.

## DeviceListToExcel.py

This script will get a list of network devices from Cisco DNA Center and present them in an Excel spreadsheet.

### Requirements
* Python 3
* [Requests][requests_link]
* [Tablib][tablib_link]

[requests_link]: https://2.python-requests.org/en/master/
[tablib_link]: http://docs.python-tablib.org/en/master/

	python3 DeviceListToExcel.py
	