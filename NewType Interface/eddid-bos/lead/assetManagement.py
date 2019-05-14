#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

# 投资管理
url = 'https://eddid-api.ntdev.be/eddid-api-feature/lead/create'
data = {
    "lastName":"lastName",
    "firstName":"firstName",
    "email":"555@163.com",
    "phoneNumber":"865112222",
    "customerSource":"assetManagement"
}
headers = {
    'Content-Type' : 'application/json', 
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoidGVzdCIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiI4YzI0ODMzMC03NjEzLTExZTktOGU2OS03OTI1YWU3NTg2MzgiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU1NzgxNjE5NCwiZXhwIjoxNTU3ODIzODAwLCJpYXQiOjE1NTc4MjAyMDEsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluMTIzNEAxNjMuY29tIn0.OZXGrnziAGxhStzo7RF6-mOvCFllSCtqjhOJRNNPa4fLKVEfifFiDcv4Apja3mfeTwrIpiJpP0ty4PYQhO_kVRPVhmTb7icL0kuX8Yo8ZgniLA-He1dE8tlFE98fqELnoyvTZmqen9-JUHozkMOh1JEuImZeG7pTdOekqwJXfIBZhYxsNgw0zUnoEfod5mbPqrKgrwpQQE_BnyEhI4nqsvz4kFa76a6ZNJvfKBpDrtugFRGzx5SSSXqYccd5ZO0cwVyPs3OMHqT8WAzNAyiCqGvSAMQFT1ETrZZBZyBWfLMZ4zcfCIVIGlpUf8OZajBapLfR3I3lfBtyCIkWch3RDQ'
}

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())


