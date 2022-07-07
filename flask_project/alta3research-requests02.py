#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/json"
resp= requests.get(URL).json()

pprint(resp)

newcharacter = {
             "name" : "Jon Snow",
             "house" : "House Stark",
             "age" : 21,
             }

# posting to our endpoint
resp_post = requests.post("http://127.0.0.1:2224/newcharacter", json=json.dumps(newcharacter))

pprint(resp_post.json())

