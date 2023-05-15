#!/usr/bin/env python3
import requests
import json
from faker import Faker

def getAuthToken():
 authCreds = (LOGIN, PASSWORD)
 r = requests.post(
 f"{APIHOST}/api/v1/loginViaBasic",
 auth = authCreds
 )
if r.status_code == 200:
    return r.json()["token"]
else:
    raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")
