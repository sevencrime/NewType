#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-29 10:33:30
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests 
import json
url = 'https://eddid-api.ntdev.be/eddid-api-uat/public/lead/findSimilarLead'
headers = {
    'Content-Type' : 'application/json' ,
    'x-api-key' : 'CCM4cuhy1e2r0XXkbzMuN1A5TiZ0tC6e6mJYKUez'
}


data = {
    "customerSource": "activity",
    "clientArr": [{
        "phoneNumber": 346436,
        "firstName": "245664352"
    }, {
        "phoneNumber": 3465235,
        "firstName": "3643646"
    }],
    "clientPhoneNumber": [346436, 3465235],
    "phoneArr": [346436, 3465235],
    "totalPeople": 3,
    "email": "onedi@qq.com",
    "lastName": "23424243",
    "firstName": "32325532",
    "phoneNumber": 3245325325,
    "activityId": ["5c74f4fd2f944e565492831b"],
    "writtenApplicationMaterials": [],
    "otherInformation": []
}

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())

# for i in range(10000):

#     data = {
#         "customerSource": "activity",
#         "clientArr": [],
#         "clientPhoneNumber": [],
#         "phoneArr": [],
#         "totalPeople": 1,
#         # "email": "onedi1%s@qq.com" %i, 
#         "email": "KJSA@qq.com" , 
#         "lastName": "234234",
#         "firstName": "243243",
#         "phoneNumber": 17600001 + i,
#         "activityId": ["5c4fbab359fba2488a3854c2"],
#         "writtenApplicationMaterials": [],
#         "otherInformation": []
#     }
#     print(data)

#     resp = requests.post(url, headers=headers, data=json.dumps(data))
#     i+=1
#     print(i)
#     print(resp.json())

