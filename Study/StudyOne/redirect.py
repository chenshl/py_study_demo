# -*- coding:utf-8 -*-
import requests
import json

req = requests.get("http://httpbin.org/redirect/1")
# lc = req.headers
# h = req.history
print(req.text)
print(req.headers)
print(req.history)

