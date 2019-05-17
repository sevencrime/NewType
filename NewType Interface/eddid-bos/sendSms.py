#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json

headers = {
    'Content-Type' : 'application/json' ,
    'x-api-key' : 'r3ojKrHQnk6MdbgQ06sQH9L5CNo7IYbI7VCOnPzY'
}

url = 'https://comm-gw.ntdev.be/comm-gateway-uat/sendSms'

data = {
    "PhoneNumbers": "",
    "templateCode": "TemplateCode",
    "receiver": "onedi@qq.com "
}


resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())
