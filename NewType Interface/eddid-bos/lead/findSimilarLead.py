#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-29 10:33:30
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests 
import json
url = 'https://eddid-api.ntdev.be/eddid-api-feature/public/lead/findSimilarLead'
headers = {
    'Content-Type' : 'application/json' ,
    'x-api-key' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiMGFiZWM4MGMtMmRlMC0xMWU5LTg3OGYtYTE4ZGQxYTViYzYwIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NDk4Nzc1ODgsImV4cCI6MTU0OTg4MTE4OCwiaWF0IjoxNTQ5ODc3NTg4LCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbjEyM0BxcS5jb20ifQ.LGN8ZN7R4PoFo0B6gvAjg3XEaU4qwVYKIUgkBM0TK-XsOznsDzv9BzJqqp9m6cIOTl0BNMFsQyDpOLcWg-G4hK2BH9wgnnPfPnoki5p4hVCUpNCQS4bdMjsj9jII__ZGsHzf8IVrt2r1F-ZJMUfukNccsFScPEX8C-yCtDMctz-tLuRMW87nkngEZ8yAVmwufwsMQDE224SRNUlhQraG0HUEBUpla32Z9k8MnNdBVNjGcbMb4eq7EVPoBRDlHT5xTg0aR5Xl26b9Yw4NF6GPAZRJ564Pzh_VHVBNiXCn6DYFQx4g8Zzohmj0vzktA4m3BtqdRXlvs8At05dfo2s-Ew'
}

for i in range(10000):

    data = {
        "customerSource": "activity",
        "clientArr": [],
        "clientPhoneNumber": [],
        "phoneArr": [],
        "totalPeople": 1,
        "email": "onedi1%s@qq.com" %i, 
        "lastName": "234234",
        "firstName": "243243",
        "phoneNumber": 17600001 + i,
        "activityId": ["5c4fbab359fba2488a3854c2"],
        "writtenApplicationMaterials": [],
        "otherInformation": []
    }
    print(data)

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    i+=1
    print(i)
    print(resp.json())

