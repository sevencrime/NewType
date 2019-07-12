#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests 
import json
import random
from requests.packages import urllib3

url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'

headers = {
    'Content-Type' : 'application/json' ,
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJmZWYwOWU1MC03Y2NkLTQ0NmQtOWIwYS1hZjFhZDlkZTcwMTIiLCJjb2duaXRvOmdyb3VwcyI6WyJjczEiXSwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjb2duaXRvOnByZWZlcnJlZF9yb2xlIjoiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIiwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoZWFzdC0xLmFtYXpvbmF3cy5jb21cL2FwLXNvdXRoZWFzdC0xX3U5Zno3bHlvTiIsImNvZ25pdG86dXNlcm5hbWUiOiJjczFfb25lZGkiLCJnaXZlbl9uYW1lIjoidGlhbnlhbmciLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiMWFiNWUyYWItNzU5My00Y2VlLWFlZDAtNjkxODY0ZWNlODk3IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NjI4MDk5MDIsImV4cCI6MTU2MjgxMzUwMiwiaWF0IjoxNTYyODA5OTAyLCJmYW1pbHlfbmFtZSI6IndhbmciLCJlbWFpbCI6IjE1MDg5NTE0NjI2QHNpbmEuY24ifQ.VgHeNxKosgXvaS2uXKu9rtDiMFQCHsmq4PnPLpyN1LWCSfgpHR3WDOR7PkkPFh2By-pTcnvR2Hm7AY7mdtpxn3U_bUpmm3KjfrXUSybTJP-fTRpSYVzOU5Y4r2oapd_RGVVL5i1-dSuSJISLQtsgv9fofSHgrafMZTYadw6lhytT4P99Pe2JAEZLwkA8vud3lvkelWsZGYklHdPaHbOB_m2Km5rtFrVhDyQnvuK6KVGJ_sj3kENaoriUwsqVT_UxV4Dcg0yh6oNpNWlsz1wMhKevCtPGIZ6YizL6WVoKhhSMfaRk1vC5dc8EPv7H0smtLzVkaAb_yo-CU46YmmlU0A'
}

data = {
    "applicationFor": "individual",
    # "applicationFor": "joint",
    # "accountType": ["securitiesCash"],
    "accountType": ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"],
    "status" : "reviewing",
    # "customerSource" : "app",
    "customerSource" : "crm",
    "client": [{
        "title": "mr",
        "firstName": "名",
        "lastName": "姓",
        "chineseName": "oneditesss",
        "email": "%sonedi%s@qq.com" %(random.randint(1,10235), random.randint(1,1562535)),
        # "email": "carl.e@newtype.io", 
        "phoneAreaCode": "CHN",
        "phone": "322%s546" %(random.randint(1,10235)),
        "address": "465456456456",
        # "nationality": "HKG",
        "nationality": "CHN",
        "idType": "2",
        "idNumber": "56%s56456" %(random.randint(1,102365)),
        # "idNumber": "568194956456",
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
    # "learnHowCode": "EDCG",
    "isRelatedAccounts": ["HK"],
    "agreeToTheTerms": "N",
    "personalInfoDeclartion": "Y"
}


# print(data)
urllib3.disable_warnings()
resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
print(resp.json())
print(resp.status_code)
print(data['client'][0]['email'])