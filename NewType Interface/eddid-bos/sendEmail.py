#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 09:53:09
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests

url = 'https://eddid-api.ntdev.be/eddid-api-uat/lead/sendemail/'
headers = {
    'content-type' : 'application/json' ,
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiYTdkMTBhMGUtMzNlNi0xMWU5LThiMDItYjM2ZTVhZDVlOGY1IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NTA1NDAxMzYsImV4cCI6MTU1MDU1NzY2NSwiaWF0IjoxNTUwNTU0MDY1LCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbjEyM0BxcS5jb20ifQ.cybRdmY29HJFCQNVRnalV8OhB557DGf2D-rtEBoJHuJwfVwgQQSdL5jXycAp9ctUBy50YoE1QzMy94Y8A5mpJBp1vvEa_HFFH_SrvoqiPg879jubFryL8ScKsAIyerVzMXZgKiQK-yyoVp7JlS_pHlKYTfS7xAktwwhjBdu_ETsG6lloc8wplCE0CEegoRCIfmvkJQWO2X49mBUHC-qvpZ7SU4jajHxw10iOiMrjWuRF-VTeJHSE6_y5RvzUJhfn_XW_OPxHeBtXJte78id54YIJlkjGfoONzs5anh2ylXzf8rYL5gkerA19r1e9KmCCctlQ1PoWMzHCi26SPE4W9A'
}

data = {
    'sortKey' : 'date' ,
    'sortVal' : 'ASC'  ,
    'offset' : 0 ,
    'limit' : 2000 ,
    'startDate' : 1547049601 ,
    'endDate' : 1547568001 ,
    'domain' : 'onedi@qq.com'
}

resp = requests.get(url, params=data, headers=headers)
print(resp)
print(resp.json())

