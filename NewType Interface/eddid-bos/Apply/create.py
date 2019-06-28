#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-30 09:44:36
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests 
import json
import random
from requests.packages import urllib3

url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'

headers = {
    'Content-Type' : 'application/json' ,
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI1MjdiMDY2YS01OGZiLTRmMDUtYWZjNi04MDIyYWI5MTIwZWUiLCJjb2duaXRvOmdyb3VwcyI6WyJjcyIsImNzMiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiY3NfdDIiLCJnaXZlbl9uYW1lIjoiS2FyeSIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiI3NGIwNjZiMS1hNzY3LTRhZWUtOTY0Yy1mZTBmZmJhZDYyM2EiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU2MTcxNjA3NiwiZXhwIjoxNTYxNzE5Njc2LCJpYXQiOjE1NjE3MTYwNzYsImZhbWlseV9uYW1lIjoi6ZmIIiwiZW1haWwiOiJrYXJ5Y2hlbjgwMkBkaW5ndGFsay5jb20ifQ.MpU08gXDvyHPfAx3C0C51cNO6YOlvGpTeF3cruIi7XJNvMLJ7OKHI0jeWN7kbSjoFsr7WeO6Vj18sU2kEcQE4Zyqwh_4Ys0BbAXnWgWPqEfGHk-xvlUJDQVPikOFx4E88OvZil45ufbYasU6ZjoLtqxCLG5JGEFw4FWhy2ZIa7qPfM_bLaCLi3Ij44C-5PvC17u1eeDnVUq4--nwvws3bi58aoAcwnMGD3VAHGJROa8xNcBCNC5jCUwnEyiRe8fNwHSoCWHdU_WWGHfcC35dc7MONSqsrU64xtYd4Hu_c5NDixyWUn4d0c5b7U2becCi7VJhj0IhEHbKJpOcWkKgng'

}


data = {
    "applicationFor": "individual",
    # "applicationFor": "joint",
    # "accountType": ["leveragedForeignExchangeAccountMargin"],
    "accountType": ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"],
    # "status" : "reviewing",
    # "customerSource" : "app",
    "customerSource" : "crm",
    "client": [{
        "title": "mr",
        "firstName": "名字",
        "lastName": "姓名",
        "chineseName": "oneditesss",
        "email": "%sonedi%s@qq.com" %(random.randint(1,10235), random.randint(1,1562535)),
        # "email": "carl.e@newtype.io", 
        "phoneAreaCode": "CHN",
        "phone": "322%s546" %(random.randint(1,10235)),
        "address": "465456456456",
        "nationality": "CHN",
        "idType": "2",
        "idNumber": "56%s56456" %(random.randint(1,102365)),
        "countryIssue": "CHN",
        "birthday": 947001600000,
        "birthPlace": "CHN",
        "employment": "retired",
        "occupation": "",
        "employedPeriod": "",
        "employer": "",
        "businessType": "",
        "businessAddress": "",
        "businessPhone": "",
        "riskInfo": {
            "isApplyToOpenTradingStructure": "Y",
            "isTradingStructureAggree": "Y",
            "isShowTradingStructureAggree": "Y",
            "isShowApplyToOpenTradingStructure": "Y",
            "isShowAlgoTrade": "N",
            "totalAnnualCustomerRevenueHK": "lt500000",
            "customerNetAssetValueHK": "lt3000000",
            "sourceOfWealth": ["selfOperated"],
            "futures": "1To5Years",
            "securities": "gt10Years",
            "CBBC": "6To10Years",
            "warrants": "gt10Years",
            "foreignExchange": "gt10Years",
            "options": "6To10Years",
            "bullion": "6To10Years",
            "algoTrade": "1To5Years",
            "isLearnAboutProducts": "Y",
            "isIndustryExperience": "Y",
            "isStocks": "Y",
            "isBankruptcy": "Y",
            "bankruptcyDate": 1557158400000,
            "isInAgtJobs": "N",
            "bankruptcyProve": ["1544166106_698802e5bebb842bfaf86bdf74458094.jpg"],
            "isBondFuturesClientsConnected": "N",
            "isAcquaintHighLevel": "N",
            "isAmericanResidents": "N",
            "isAmericanResidentsb": "N",
            "isPoliticalFigure": "N",
            "purposeOfInvestment": ["hedging", "asset"],
            "riskTolerance": "high"
        }
    }],
    "infoB": {},
    "bankAccount": "",
    "parentId": "sales_t1",
    "accountOpeningWay": "visitingAccount",
    "mailLanguage": "zh-hans",
    "currency": "NA",
    "isMarginAccount": "N",
    "isDiscretion": "N",
    "isCompanyAccounts": "N",
    "learnHow": ["lecture"],
    "isBeneficiary": "Y",
    "isOrders": "Y",
    "learnHowCode": "EDCG",
    "isRelatedAccounts": ["HK"],
    "agreeToTheTerms": "N",
    "personalInfoDeclartion": "Y"
}


# print(data)
urllib3.disable_warnings()
resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
print(resp.json())

print(data['client'][0]['email'])