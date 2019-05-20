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
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoidGVzdCIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiI0YWMwOGU5Ny03YWEwLTExZTktOTIzNi01OTc4NGJkMWU0MjgiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU1ODMxNjQ0NywiZXhwIjoxNTU4MzIwMDQ3LCJpYXQiOjE1NTgzMTY0NDgsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluMTIzNEAxNjMuY29tIn0.c8i3iTxKPbmZ-6MSDbD_9IC03w3_e9SZhD8pgLwRPBsRSw3zw9ExBp5Spd9YCnaQo3F-W9uH-adgFfNK1xTYcfavX3CmtCBnExztVC6hXIwjtq6WnQL4-R85pNJVmN7DEzdsM4EFyPnwh1CGplZM-HgAhvDfjkFy34jZ8QM_D4klPwW20SI0mVV-pHqedcmEZq2JUBXzTkPwoj8IBcTEOIp9oTIKoe4WCbEt2FrZUyve0o-b4uS1TlLj44L2fz7KzAmXKIpp-f6o1T9R5m0wQk5rJSOZeRhBn2HM-o8pvgnQa6KjVncfloDEZB9xO_tDDrdj1PZ69w_u3z8B8PTLOA'
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
