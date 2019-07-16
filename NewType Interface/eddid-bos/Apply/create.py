#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests 
import json
import random
from requests.packages import urllib3

url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'

headers = {
    'Content-Type' : 'application/json' ,
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoidGVzdCIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiJmMzg5NmIyYy1kYmViLTQyNWEtOGU0Mi1iODc3NTQ0N2UyNGUiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU2MzI2MjQ1MywiZXhwIjoxNTYzMjY2MDUzLCJpYXQiOjE1NjMyNjI0NTMsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluMTIzNEAxNjMuY29tIn0.Phfwd3JMSz02A1w6Q7-OVSVtKs7kbrCrbiM89Fk8gvG5Mz_fFvXwQlIOQp5NJEF5CL9ZyX-o2UxEb4UQvPjnNbp-fWJB9UfrPExoWul2plmAJlpC0Y8W0WelUDqSkaML-v7rwyf_d0FH0linA1BTZiJMcVLpndKEi5A-WWmXBsyt3G8QKJT6FeFZDdqgNJm6AXz3OPvuGp1gmXqjyuZM8sQJtaGpILzCGqR5cCNYQKPUFcpil3pRuF7PrXgzWHreiF7CYChINpNaMCSaaJ-Z4labUgZ70gnHpdna_g46G4VQQFLNVhXiODD88nxJrtHgE0xUQb3LvEP-CbCyeY4xig'
}

data = {
    "applicationFor": "individual",
    # "applicationFor": "joint",
    # "accountType": ["securitiesCash"],
    "accountType": ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"],
    "status" : "finish",
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