#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("Eddid_CRM\\")+len("Eddid_CRM\\")]
sys.path.append(rootPath)
import requests 
import json
import random
from requests.packages import urllib3
from Commons import *

def apply_create_api():

    gm = GlobalMap.GlobalMap()
 
    url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'

    headers = {
        'Content-Type' : 'application/json' ,
        'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoidGVzdCIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiJiOWQ0NzhjOS01YWZmLTRjNGQtYjAyMi1iNWE5Y2YxZDdlODMiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU2MjU3MjUxNiwiZXhwIjoxNTYyNTc2MTE2LCJpYXQiOjE1NjI1NzI1MTYsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluMTIzNEAxNjMuY29tIn0.aEsU3WC_7Jnxv0akmFdOc62lVj4yJPa2RxPXsXAFwWM3Qm-waXSScohppPQX4q51gFtduGVzSnwmHBBA9QESIKDsD3RtLbss52uHMJJuNUmGqzrHbrXjHGgW0Ed-DvOowb1ulQ8w-Aki0nE51URDEsI8ly4gMkNYOTYfNiW6DiTth4rqxgw4JXDyAzPI4Fx2ieP70TO9EU2at9PrFOW57vHfN6pB7Gdn3kjQMRqymhOoEvQxMTxeb2sRyzk3Uwwyuw1wk1SmxHgwNvX3MI6O1qn-MUqy0V161LZLQ0GW2O2HgGMikix44V1iiSQy98gEUSS5kiEbSOIwhXkIMbOp8g'

    }

    data = {
        "applicationFor": "individual",
        # "applicationFor": "joint",
        "accountType": gm.get_value("accountType"),
        # "accountType": ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"],
        # "status" : "finish",
        "status" : gm.get_value("apiStatus"),
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
            # "nationality": "CHN",
            "nationality": "HKG",
            "idType": "2",
            "idNumber": "56%s56456" %(random.randint(1,102365)),
            # "idNumber": "563296356456",
            "countryIssue": "HKG",
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

    for i in range(3):

        urllib3.disable_warnings()
        resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
        if resp.status_code == 200:
            return data['client'][0]['email']


if __name__ == '__main__':

    a = apply_create_api()
    print(a)
