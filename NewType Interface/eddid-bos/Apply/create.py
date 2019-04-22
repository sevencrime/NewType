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
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJlODRjNDM1YS01OTFiLTQzMTktOWVhMC1lZDAyY2NkZTRjM2UiLCJjb2duaXRvOmdyb3VwcyI6WyJjczIiXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsImNvZ25pdG86cHJlZmVycmVkX3JvbGUiOiJhcm46YXdzOmlhbTo6ODMyNDMxODY0NjY2OnJvbGVcL2Rldi1lZGRpZC1jb2duaXRvLWFkbWluLXJvbGUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfdTlmejdseW9OIiwiY29nbml0bzp1c2VybmFtZSI6ImNzX3QxIiwiZ2l2ZW5fbmFtZSI6IkFpbWVlIiwiY29nbml0bzpyb2xlcyI6WyJhcm46YXdzOmlhbTo6ODMyNDMxODY0NjY2OnJvbGVcL2Rldi1lZGRpZC1jb2duaXRvLWFkbWluLXJvbGUiXSwiYXVkIjoiNTEzamZja3RyMW02ZXZvZ2ZxdTdvc2s3cGEiLCJldmVudF9pZCI6IjczMTNmNTY2LTY0YTUtMTFlOS1iYzEwLWYxMzBkZjM1MWY3MiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNTU1ODk5NzM3LCJleHAiOjE1NTU5MDMzMzcsImlhdCI6MTU1NTg5OTczNywiZmFtaWx5X25hbWUiOiJXZWkiLCJlbWFpbCI6IjEyMzQ1NkAxNjMuY29tIn0.YOdClUJSF4uQzPMFTbGszg5vp4VK4qUke5T14ew3y-XCTUkYq-hQTuX5nmWfCiaUXIUKtTkkfLxF_N2-mUA4zwD2YEqzF1RUm74NqhHfhh7HayDRnq-1UKmScWK6e3XGiSn-zrgXl_5UH0f81UIs0cq4AJmD313Bk9EDCIpmy62Hae3tIRylpPDdl0RjGZnILGNiNdD5kfxqiZyXLL8HQ8t_Q4MAYM5xCZ252u6Zs143wOkLEMWPoBXY5EWKTs-JBpFsgkvF2cq_0Ft7mUxdpuDBRY19k7yi-vEnFo1Qu01Ku268O1NbVHzitaKXReilQNBQvT4X5IakpGETeHF__w'


}


data = {
    "applicationFor": "individual",
    # "applicationFor": "joint",    
    # goldSpot 黄金
    "accountType": ["securitiesCash", "leveragedForeignExchangeAccountMargin","futuresMargin","securitiesDayTradeMargin", "bullionMargin"],
    # "accountType": ["bullionMargin"],
    #mobile:手机;visitingAccount:亲临开户;postal:邮递;onlineApplication:网上开户申请
    "accountOpeningWay": "visitingAccount",  #开户方式,
    "personalInfoDeclartion": "Y",
    "customerSource": "ballFives",    
    # "customerSource": "app",    
    # "customerSource": "crm",    
    "mailLanguage": "en",
    "appBankName": "",
    "appBankAccount": "",
    "appCertSn": "",
    "currency": "HKD",
    "bankAccount": [],
    "isMarginAccount": "",
    "marginAccountName": "",
    "marginAccountNumber": "",
    "isDiscretion": "",
    "discretionName": "",
    "discretionNumber": "",
    "isCompanyAccounts": "",
    "companyAccountsName": "",
    "companyAccountsNumber": "",
    "learnHow": ["advertising"],
    "learnHowOther": "",
    "learnHowCode": "EDYL",
    "IBparentId": "",
    "isBeneficiary": "Y",
    "beneficiaryName": "",
    "isOrders": "Y",
    "tradingAuthorization": [],
    "ordersName": "",
    "isRelatedAccounts": ["HK"],
    "relatedAccountsOpt": [{
        "id": 5888414,
        "residenceJurisdiction": "",
        "taxId": ""
    }],
    "receipt": ["download"],
    "agreeToTheTerms": "Y",
    "jointReportingStandardStatement": "Y",
    "privacyPolicyStatement": "Y",
    "customerStatement": "Y",
    "riskDisclosureStatement": "Y",
    "termsAndConditionsOfBusiness": "Y",
    "client": [{
        "riskInfo": {
            "passportMaterial": ["publicDropbox/BcPJde9SCkFdFssQaJz9KYRNMbfyYm2t.jpeg"],
            "addressVerificationMaterials": ["publicDropbox/8pRBJ8ssFtibKGdF4kw1r6irkijMe9G2.jpeg"],
            "bankCardMaterials": ["publicDropbox/NRccBw9hbN2ZXXbfajmrZw4TR17HNS3F.jpeg"],
            "referralCode": "",
            "isErr": False,
            "errText": "",
            "otherInformation": [],
            "proofOfIncome": [],
            "totalAnnualCustomerRevenueHK": "lt200000",
            "customerNetAssetValueHK": "lt1000000",
            "sourceOfWealth": ["savings"],
            "sourceOfWealthOther": "",
            "securities": "lt1Year",
            "CBBC": "lt1Year",
            "warrants": "lt1Year",
            "futures": "lt1Year",
            "options": "lt1Year",
            "otherInvestment": "",
            "otherInvestmentText": "",
            "foreignExchange": "lt1Year",
            "isLearnAboutProducts": "Y",
            "isIndustryExperience": "Y",
            "isStocks": "Y",
            "isTradingStructureAggree": "N",
            "isApplyToOpenTradingStructure": "Y",
            "isBankruptcy": "N",
            "bankruptcyDate": "",
            "bankruptcyProve": [],
            "isInAgtJobs": "N",
            "agtPosition": "",
            "isBondFuturesClientsConnected": "N",
            "agtName": "",
            "isAcquaintHighLevel": "N",
            "acquaintHighLevelInstructions": "",
            "acquaintHighLevelInstructionsProve": [],
            "isAmericanResidents": "N",
            "americanResidentsTaxId": "",
            "isAmericanResidentsb": "N",
            "americanResidentsTaxIdb": "",
            "isPoliticalFigure": "N",
            "politicalFigureName": "",
            "purposeOfInvestment": "hedging",
            "riskTolerance": "low"
        },
        "title": "mrs",
        "parentId": "sales_t1" ,
        "lastName": "last",
        "firstName": "first",
        "chineseName": "Test",
        "pastEnglishName": "",
        "pastChineseName": "",
        "idType": "2",
        "idNumber": "%s423523%s" %(random.randint(0,1001),random.randint(0,10600)),
        "countryIssue": "CHN",
        "nationality": "CHN",
        "birthPlace": "CHN",
        "birthday": 894384000000,
        "email": "%sonedi2s%s@qq.com" %(random.randint(0,1000),random.randint(0,10300)),
        # "email": "onedi.zheng@newtype.io" ,
        "phoneAreaCode": "HKG",
        "phone": "%s6253%s" %(random.randint(0,100002),random.randint(0,10502)),
        # "phone": "15089514626" ,
        "address": "3466324364",
        "addressMail": "34632646345",
        # "mailLanguage": "zh-hans",
        "mailLanguage": "zh-hans",
        "employment": "retired",
        "employmentOther": "",
        "occupation": "",
        "employedPeriod": "",
        "employer": "",
        "businessType": "",
        "businessAddress": "",
        "businessPhone": ""
    },
    # {
    #     "riskInfo": {
    #         "passportMaterial": ["publicDropbox/BcPJde9SCkFdFssQaJz9KYRNMbfyYm2t.jpeg"],
    #         "addressVerificationMaterials": ["publicDropbox/8pRBJ8ssFtibKGdF4kw1r6irkijMe9G2.jpeg"],
    #         "bankCardMaterials": ["publicDropbox/NRccBw9hbN2ZXXbfajmrZw4TR17HNS3F.jpeg"],
    #         "referralCode": "",
    #         "isErr": False,
    #         "errText": "",
    #         "otherInformation": [],
    #         "proofOfIncome": [],
    #         "totalAnnualCustomerRevenueHK": "lt200000",
    #         "customerNetAssetValueHK": "lt1000000",
    #         "sourceOfWealth": ["savings"],
    #         "sourceOfWealthOther": "",
    #         "securities": "lt1Year",
    #         "CBBC": "lt1Year",
    #         "warrants": "lt1Year",
    #         "futures": "lt1Year",
    #         "options": "lt1Year",
    #         "otherInvestment": "",
    #         "otherInvestmentText": "",
    #         "foreignExchange": "lt1Year",
    #         "isLearnAboutProducts": "Y",
    #         "isIndustryExperience": "Y",
    #         "isStocks": "Y",
    #         "isTradingStructureAggree": "N",
    #         "isApplyToOpenTradingStructure": "Y",
    #         "isBankruptcy": "N",
    #         "bankruptcyDate": "",
    #         "bankruptcyProve": [],
    #         "isInAgtJobs": "N",
    #         "agtPosition": "",
    #         "isBondFuturesClientsConnected": "N",
    #         "agtName": "",
    #         "isAcquaintHighLevel": "N",
    #         "acquaintHighLevelInstructions": "",
    #         "acquaintHighLevelInstructionsProve": [],
    #         "isAmericanResidents": "N",
    #         "americanResidentsTaxId": "",
    #         "isAmericanResidentsb": "N",
    #         "americanResidentsTaxIdb": "",
    #         "isPoliticalFigure": "N",
    #         "politicalFigureName": "",
    #         "purposeOfInvestment": "hedging",
    #         "riskTolerance": "low"
    #     },
        # "title": "mrs",
        # "parentId": "kwokwah.wong" ,
        # "lastName": "32455432",
        # "firstName": "3245532523",
        # "chineseName": "5235234",
        # "pastEnglishName": "",
        # "pastChineseName": "",
        # "idType": "2",
        # "idNumber": "%s423523%s" %(random.randint(0,100001),random.randint(0,106000)),
        # "countryIssue": "CHN",
        # "nationality": "CHN",
        # "birthPlace": "CHN",
        # "birthday": 894384000000,
        # "email": "%sonedi2s%s@qq.com" %(random.randint(0,1000),random.randint(0,10300)),
        # # "email": "onedi@qq.com" ,
        # "phoneAreaCode": "HKG",
        # "phone": "%s6253%s" %(random.randint(0,100002),random.randint(0,100502)),
        # # "phone": "15089514626" ,
        # "address": "3466324364",
        # "addressMail": "34632646345",
        # # "mailLanguage": "zh-hans",
        # "mailLanguage": "zh-hans",
        # "employment": "retired",
        # "employmentOther": "",
        # "occupation": "",
        # "employedPeriod": "",
        # "employer": "",
        # "businessType": "",
        # "businessAddress": "",
        # "businessPhone": ""
    # }
    ]
}

# print(data)
urllib3.disable_warnings()
resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
print(resp.json())

