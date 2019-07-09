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
    log = Logging.Logs()
 
    url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'

    headers = {
        'Content-Type' : 'application/json' ,
        'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI2NTIxNGJhYi1jMDFlLTRiNmItYmNkZS02ODMxNDdmN2NjYTgiLCJjb2duaXRvOmdyb3VwcyI6WyJzYWxlcyJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoic2FsZXNfdDEiLCJnaXZlbl9uYW1lIjoiTWkiLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiNTMzMTVkZTgtY2ZhMi00MzQ2LWEzNTItOGQwNjc4MzdmY2NmIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NjI2Njc0NjgsImV4cCI6MTU2MjY3MTA2OCwiaWF0IjoxNTYyNjY3NDY4LCJmYW1pbHlfbmFtZSI6IlhpYW8iLCJlbWFpbCI6ImNhcHMuY2hlbkBuZXd0eXBlLmlvIn0.PSV8n-PQCplJ5f8L0TGeAjb7ezlcTFZ6XfvNhn2rY_zjHs3g_cFeIq2tPZoY5ZXZYM1yf3qpeZBbCvFOuAx02nkPfCnA5yL7Aa8NhHjCjFvbyH8W1JctL-qZh4kmf8OhyIrLQRPr41G5IcjCiJ-h-gFuOEFszwqJGcFO3w-NZZdhIiZhNnpnyF0FJwwZ6S8q0CNNs578ssAvQRRo50VuegkxzeRMVzzOXmaxAtOlnWz76b-yaQSb6UaqXb1O3jvsX80exkglTku_2lv4jwZBnZnPdYTGzN0ZIO27EeEzoqbPaJA6HJ48evz0hldoZbjVxYPd5K9dWph13QK4DOxRIQ'

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

    # 失败重新请求三次
    for i in range(3):

        urllib3.disable_warnings()
        resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
        log.info("/apply/create: ", resp.json())
        if resp.status_code == 200:
            log.info("新创建数据的[email]为: {}".format(data['client'][0]['email']))
            return data['client'][0]['email']


if __name__ == '__main__':

    a = apply_create_api()
    print(a)
