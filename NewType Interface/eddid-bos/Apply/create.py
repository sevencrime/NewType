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
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJlODRjNDM1YS01OTFiLTQzMTktOWVhMC1lZDAyY2NkZTRjM2UiLCJjb2duaXRvOmdyb3VwcyI6WyJjczIiXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsImNvZ25pdG86cHJlZmVycmVkX3JvbGUiOiJhcm46YXdzOmlhbTo6ODMyNDMxODY0NjY2OnJvbGVcL2Rldi1lZGRpZC1jb2duaXRvLWFkbWluLXJvbGUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfdTlmejdseW9OIiwiY29nbml0bzp1c2VybmFtZSI6ImNzX3QxIiwiZ2l2ZW5fbmFtZSI6IkFpbWVlMSIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiIyOGM5ZGFlOC04NjZmLTExZTktODQxZC01NWU3OGNiMTU4NTEiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU1OTYxNDc1OSwiZXhwIjoxNTU5NjE4MzU5LCJpYXQiOjE1NTk2MTQ3NTksImZhbWlseV9uYW1lIjoiV2VpMSIsImVtYWlsIjoiMTIzNDU2MzNAMTYzLmNvbSJ9.afsEqfpFtbgB7upMvUMn5Iq-6JWRTHPk-CyWBIBXhL1MiVUXwdgw9_o_5Te67iUH1OkSsq5DBSdiCsiwlnN_TxInOkbl-KR7ypKageCiGTn0z-sQq9K99VISgK82cYzazv0u8Ax9kqJnnIbshJUf-0S0T8Juon54GM4AAPwg17FtL7kgfoZHJMLJ2TbtzaBJzWT8NbJlC4v8RR_0C1yCgMIuHiImcPnFTkFAk_KhPqSMbAWMB6onj058R9zXI7ARZN0hCgajRZCbIrbh9BvE_LGOUUzEXqboq0Zbc2VBo1_8wKRl_ZWZbwzRs9GQyfQxxK9hdXM-pnMy5wUWAwhI7A'

}


data = {
    "applicationFor": "individual",
    # "applicationFor": "joint",
    # "accountType": ["securitiesCash"],
    "accountType": ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"],
    "status" : "reviewing",
    "customerSource" : "app",
    # "customerSource" : "crm",
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
    "learnHowCode": "EL[Y",
    "isRelatedAccounts": ["HK"],
    "agreeToTheTerms": "N",
    "personalInfoDeclartion": "Y"
}


# print(data)
urllib3.disable_warnings()
resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
print(resp.json())

print(data['client'][0]['email'])