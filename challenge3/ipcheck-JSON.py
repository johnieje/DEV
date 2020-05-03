"""
Some lines are commented out.
You may or may not want to use the ipaddress library
but you will still need to check for a valid IPv4 adddress.

The 'with open('JSONdata') as f:' line will read the data file
AS LONG AS IT IS IN THE SAME DIRECTORY :)

The next line should get you started with a method you will need
from the json library to change the JSON text into something 
you can call from Python
"""

import json
import ipaddress


def check_ip(ip):
    try:
        if ipaddress.ip_address(ip):
            return f"{ip} is a Valid IP Address"
        else:
            return f"{ip} is not a Valid IP Address"
    except ValueError as e:
        # print(e)
        return f"{ip} is not a Valid IP Address"


with open('JSONdata') as f:
    data = json.load(f)
    for d in data:
        # use the check_ip method to check validity of IP Address
        print(check_ip(d['lanIp']) + " for Serial #" + d['serial'])
