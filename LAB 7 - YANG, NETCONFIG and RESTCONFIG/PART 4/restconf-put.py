import json
import requests

# Disable SSL certificate warnings
requests.packages.urllib3.disable_warnings()

# API URL for the target device
api_url = "https://192.168.56.102/restconf/data/ietfinterfaces:interfaces/interface=Loopback2"

# Headers for the request
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

# Basic authentication credentials
basicauth = ("cisco", "cisco123!")

# Configuration data in YANG format
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

# Send the RESTCONF PUT request to configure the loopback interface
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

# Check the response status code
if resp.status_code >= 200 and resp.status_code <= 299:
    print("STATUS OK: {}".format(resp.status_code))
else:
    # Display error message and response JSON in case of an error
    print('Error. Status Code: {}\nError message:\n{}'.format(resp.status_code, resp.json()))

