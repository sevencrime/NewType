#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

# 投资管理
url = 'https://eddid-api.ntdev.be/eddid-api-feature/lead/create'
data = {
    "lastName":"这是lastname",
    "firstName":"这是firstName",
    "email":"555@163.com",
    "phoneNumber":"8651122225677",
    "customerSource":"assetManagement"
}
headers = {
    'Content-Type' : 'application/json', 
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoidGVzdCIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiI0YWQ1OWNmZS03YzcyLTExZTktYjhkZi0wN2ExNjAwYWVhOTIiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU1ODUxNjU5MywiZXhwIjoxNTU4NTIwMTkzLCJpYXQiOjE1NTg1MTY1OTMsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluMTIzNEAxNjMuY29tIn0.ed3IahPPgCH5Oodo_02DUVOjJZ6N2rw9qGs7v5yadQev_kx49I08EUWfkkYMqn0N0pkJyTMqTIs8xJC5PVw5YN6ra4ubfPgR5J5VMs0Upem_XeFN_lNPSZQ4gt8aj3FCOPwfPLidceQE95IfxUqrR5RDEVr2P0yVseo0-mifImfz-61tVfF9UmamFxJlSOUqZLuGNnANOQy7Qq0tbd8GNpp1je9NYWfAeLaPM6s6Q0ZfEU9DJL-F3QTAf9yK0PpuJvCgaJqgBYf8pcU3ACjE2SEHwOTBfmNpcGt6HYMsBWS7e6BBFlR_32B9synIywz3oD9ikGXNQIugMLOW7cHoZg'
}

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())


