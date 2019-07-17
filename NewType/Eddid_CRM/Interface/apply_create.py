#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Commons import GlobalMap, Logging

import requests 
import json
import random
from requests.packages import urllib3


def apply_create_api():

    gm = GlobalMap.GlobalMap()
    log = Logging.Logs()
 
    url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'

    headers = {
        'Content-Type' : 'application/json' ,
        'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI2NTIxNGJhYi1jMDFlLTRiNmItYmNkZS02ODMxNDdmN2NjYTgiLCJjb2duaXRvOmdyb3VwcyI6WyJzYWxlcyJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoic2FsZXNfdDEiLCJnaXZlbl9uYW1lIjoiTWkiLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiMjhkYTBmMzUtMDc3Mi00MWEwLTg3NTMtNTgzYTRhMzRkM2Y1IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NjMzNTc0NTMsImV4cCI6MTU2MzM2MTA1MywiaWF0IjoxNTYzMzU3NDUzLCJmYW1pbHlfbmFtZSI6IlhpYW8iLCJlbWFpbCI6ImNhcHMuY2hlbkBuZXd0eXBlLmlvIn0.b8v_QwKxURRi5KdBHiaUJ013W9V17sY6ssUSivW_RjkP2kN0Ks3RJpRq9_3hXA7YkCwH8c6LdKPHseQTAhxXVMstJykrbg6VyqHAeZIlo8uKLRVFdYx5xIxX-H7XsPlymuvEamIlGQn8U8nGL1QqzESIlbtie9DUHp0eSkMwe5N4Jonl92zuob7krSfuU1lcLTsBoy-IegNsg-aSWPhspcTBd1tTv7DPdGY-1BjO83QtU0wTg-G5g21oB63cEIVoOrcxwvcDNZd2OcpBTdDImhYcmVkn0Hu9RVO2q52OnkLoKPKiqVodZ3tfXeABQte2R-iVgpTD0tnXvh1n35eUUw'
    }

    data = {
        "applicationFor": "individual",
        # "applicationFor": "joint",
        "accountType": gm.get_value("accountType"),
        # "accountType": ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"],
        # "status" : "finish",
        "status": gm.get_value("apiStatus"),
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
        log.info("accountType == {}".format(gm.get_value("accountType")))
        log.info("apiStatus == {}".format(gm.get_value("apiStatus")))
        urllib3.disable_warnings()
        resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
        # print(resp.json())
        # print(resp.status_code)
        log.info("/apply/create: 創建的數據為:{}".format(resp.json()))
        if resp.status_code == 200:
            log.info("新创建数据的[email]为: {}".format(data['client'][0]['email']))
            return data['client'][0]['email']


if __name__ == '__main__':

    a = apply_create_api()
    print(a)
