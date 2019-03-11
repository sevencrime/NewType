#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-07 09:37:23
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import json
import datetime

# print(datetime.datetime.now().strftime("%Y-%m-%d"))
# print((datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"))


url = 'https://eddid-api.ntdev.be/eddid-api-feature/public/leadDistribute/list'
headers = {
    'Content-Type' : 'application/json' ,
    'x-api-key' : 'sTCVd81kAq2MgztGZuBLf8h2RDJ4Yvm38zVWUrYe'
}

data = {
    "sortKey": "date",
    "sortVal": "ASC",
    "searchKey": "",
    "searchVal": "",
    "offset": 0,
    "limit": 10,
    "startDate": datetime.datetime.now().strftime("%Y-%m-%d"),
    "endDate": (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
}

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())
