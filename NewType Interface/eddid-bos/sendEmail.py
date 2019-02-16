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
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiZDZiY2Y4NGItMTg2Ni0xMWU5LWFmYWUtNjVlZTc0ODZlZTY1IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NDc1MTY1NTgsImV4cCI6MTU0NzYwNTQ4NSwiaWF0IjoxNTQ3NjAxODg1LCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbjEyM0BxcS5jb20ifQ.MPow99Yhv3D6fdG-3VTqlXIfeVzU7P8snNETNBgOSb7A795XaVWxE95JOI2J1qNv436J-UoAzQVNXBh4dwZKr4DPKxExoQXrX5iI_JcBta4m6BnJFU_hPKCHJ0PIKwQPI7hvzvUBw1BA9hwZ4ios5np1jAnZXsQa8ai1DMnAMcqAiJfQkDzR-lMNzcYlXbW9RzPHNMqqqH0T9khfDa5NksLbLweoVVrPdOgEskibudzPBZ9WGhZ7auIrDUbNL9Ig5gEBr1sfGqmmqjncdmfzrPdGHk4uBnvRO9SLr2wC6OcqNelVEnAiA7BxTarzmUvTBap77s92LkPu0EOk9ifkig'
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

