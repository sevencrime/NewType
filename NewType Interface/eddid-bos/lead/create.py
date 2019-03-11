#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-11 17:18:25
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import json

url = 'https://eddid-api.ntdev.be/eddid-api-uat/leadDistribute/create'
headers = {
    'Content-Type' : 'application/json' ,
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiNTk0MGVjMjYtNDNkNi0xMWU5LWJkMDctMjE1OWU5NmFhODVjIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NTIyOTIzNTEsImV4cCI6MTU1MjI5OTcwNSwiaWF0IjoxNTUyMjk2MTA1LCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbjEyM0BxcS5jb20ifQ.T-j10J-HhXvtgJ8jU3WOPzsa3m6m5DkpsrIQtqI8ItZ0qtxlkd_BpYl7trsA506bpGToUVLriRGMICEF-ry820dj8J1pNO7LXVU8F2No-iFdSiZoaYylR9ZWMZoM30l52q8spbwdlQUXUKIo-RrZalk45nRVG0v9FILDVqGvX_sDS9-oKzsIWNLBJCL0PZa5S8PdAMhqtiBAgAUIDzMVOLYDFpRJ1eMYRfhlJZiV2TlunmwRQMaV36THvH10csIzQd85JRKfCcryTzLHSqCgxOP75BpZw9kup7s68VNTt0_W_-Xgle6c_h9gLYe-gnuVUjbNmJ9i0XJ4sVOV08_Ckw'
}

data = {
    "principal": [],
    "isGreat": "0",
    "date": "2019-03-14",
    "time": "17:16-18:16",
    "title": "就業形勢12",
    "lecturer": "李政",
    "level": "middle",
    "location": "桑達科技大廈",
    "discounts": "34224332",
    "name": "就業形勢12",
    "activityType": "seminar",
    "selected": "0",
    "leadTotal": 0,
    "leadToUser": 0
}

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())
