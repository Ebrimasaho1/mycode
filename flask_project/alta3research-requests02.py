#!/usr/bin/env python3
import requests
import json
from pprint import pprint

# url that returns the json 
URL= "http://127.0.0.1:2224/json"
resp= requests.get(URL).json()

print("Original response")

pprint(resp)

# new object to be added to the json/dictionary 
newcharacter = {
             "name" : "Jon Snow",
             "house" : "House Stark",
             "age" : 21,
             }

# posting to our endpoint
resp_post = requests.post("http://127.0.0.1:2224/newcharacter", json=json.dumps(newcharacter))

print('------------------------------------------------')
print("New response after the new object is posted")

# pretty print the response for a cleaner and more readeable output
pprint(resp_post.json())

