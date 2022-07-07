#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/json"
resp= requests.get(URL).json()

pprint(resp)
