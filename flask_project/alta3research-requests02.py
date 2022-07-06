#!/usr/bin/env python3
import requests
import json

URL= "http://127.0.0.1:2224/json"
resp= requests.get(URL).json()

print(resp)
