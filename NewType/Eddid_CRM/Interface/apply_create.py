#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests 
import json
import random
from requests.packages import urllib3


def apply_create_api():

    url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'

    headers = {
        'Content-Type' : 'application/json' ,
        'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJlODRjNDM1YS01OTFiLTQzMTktOWVhMC1lZDAyY2NkZTRjM2UiLCJjb2duaXRvOmdyb3VwcyI6WyJjczIiXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsImNvZ25pdG86cHJlZmVycmVkX3JvbGUiOiJhcm46YXdzOmlhbTo6ODMyNDMxODY0NjY2OnJvbGVcL2Rldi1lZGRpZC1jb2duaXRvLWFkbWluLXJvbGUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfdTlmejdseW9OIiwiY29nbml0bzp1c2VybmFtZSI6ImNzX3QxIiwiZ2l2ZW5fbmFtZSI6IkFpbWVlMSIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiJlMjY3MWRmZi0zNmZhLTRiMjAtYmMxNi02M2YwYWZiMjVmMDIiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU2MjIyNjUwMywiZXhwIjoxNTYyMjk0MTM2LCJpYXQiOjE1NjIyOTA1MzYsImZhbWlseV9uYW1lIjoiV2VpMSIsImVtYWlsIjoiMTIzNDU2MzNAMTYzLmNvbSJ9.hJKpHtKZ_mzA8UH39BdL0juhqzBwHlKRIZ-B0_rH1UjkQxwu0UiUM-o79oleiqGCROiKaulRQXmH62rDSdC005aewjBjRTZOsdA2eL_dlEmlFPWhcRt6Hkil89FF_YjtidfhfkF5_RwLJOyc6B-rtXS8PTgm_vB1zMwno3s7xh05sahf6x3d7dBoJZUJDn5OlseKVmWplGdC5zK8xe9audGppVUO6NIYHl_Luuh5kBisppsi0ZYDvvY82LdlrlFDgVl6-K3arx2Z6cPzJMHIS2VaMGibPYuxyJ4L-_z7AXpQAMjRkBvvVYz-3fqaaRDQIRSGRCxAhPbn1pLY8k4Zhg'

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


    # print(data)
    for i in range(3):

        urllib3.disable_warnings()
        resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
        if resp.status_code == 200:
            return data['client'][0]['email']


<<<<<<< HEAD
if __name__ == '__main__':

    a = apply_create_api()
    print(a)
=======

>>>>>>> ff79fd9697223b77c7849ce1674309d69a2bdf59
