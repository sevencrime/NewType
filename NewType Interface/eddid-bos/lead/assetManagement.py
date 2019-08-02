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
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoidGVzdCIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiI1M2IyOTIyMS0zNGFkLTQxZWQtYjNhNy1jZDU5NDk2NWU1OGIiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU2NDY1OTMwNiwiZXhwIjoxNTY0NzE1NzkwLCJpYXQiOjE1NjQ3MTIxOTAsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluMTIzNEAxNjMuY29tIn0.MAhjmnrYVFIAGL-9EnCBhFC5ddWBaPX9BAk3Tdh_VRxvRh26E7K45YXhZUO98vF8AgD-p7VZdHthGLkd235bo_AM4ciuvwHG30mtHxu4IO3o4Wu7y6xlW55X2U56ZuucTF_Sv3cnZfzLRqHA6pBua79nvVkuw2EQFB11cwIqMc8E41BrmrlaVpt5nADGoyn7GhMXsjW4HLPlpwF0v9MR7VeIbQktj_qzqn-xDVfx-oSAanTlEuR8iitJ29Lom8ZbYxffBqjv25RNtTnT_Kxlvt2DIBTOPUhZNOsmr3SiYU_Gh5vrYNFnybqO5-pq7WIXmxXiYMqjnXI06yQSumU8YQ'
}

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())


