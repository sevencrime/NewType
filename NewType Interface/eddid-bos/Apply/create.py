#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-30 09:44:36
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests 
import json
import random

url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'
headers = {
    'Content-Type' : 'application/json' ,
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiZmIxYWExYTgtMzRmMS0xMWU5LWIwMzYtN2Q5Y2ZjMjAxZTZhIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NTA2NTQ5NTEsImV4cCI6MTU1MDY1ODU1MSwiaWF0IjoxNTUwNjU0OTUxLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbjEyM0BxcS5jb20ifQ.Cog7wumfTbA5140M2jZo68w6qjKxE5GZ2-veRUgkALLbrlyR_F1TCqW_mpMBl1nYt_vlHsPTWLWdTY74d_5I4vAn73z8Etns6eMmDHgaBkYfHFVj24fMXpURr_lBT4iSLvA0H_ErNOQXuUhMlGAit0pdlhHuqqmmevqWaMFEL1kMyeygfSmXnzp5S1IUUQt8BUQ_SmyDtmkGV_9mF2gdrOb53o6UlCPKfbMX3YQyL525fzB44mQDBjZchpLimfWZNbbuksNkTfEqk77voKDiyre8vyuvne1TXVN3cyQ21xYJ2xQtsTNG90JfKmNxZ5wkJfll7S3iGXDD8MAdv7GojA'
}


data = {
    "applicationFor": "individual",
    # "applicationFor": "joint",    
    "accountType": ["securitiesCash", "leveragedForeignExchangeAccountMargin","futuresMargin","securitiesDayTradeMargin"],
    # "accountType": ["securitiesCash"],
    #mobile:手机;visitingAccount:亲临开户;postal:邮递;onlineApplication:网上开户申请
    "accountOpeningWay": "mobile",  #开户方式,
    "personalInfoDeclartion": "Y",
    # "customerSource": "ballFives",    
    # "customerSource": "app",    
    "customerSource": "crm",    
    "mailLanguage": "en",
    "appBankName": "",
    "appBankAccount": "",
    "appCertSn": "",
    "currency": "HKD",
    "bankAccount": [{
        "id": 6970416,
        "name": "34636",
        "number": "3464635",
        "holder": "36456435463",
        "currency": "HKD"
    }],
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
    "learnHowCode": "",
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
        "lastName": "32455432",
        "firstName": "3245532523",
        "chineseName": "5235234",
        "pastEnglishName": "",
        "pastChineseName": "",
        "idType": "2",
        "idNumber": "%s423523%s" %(random.randint(0,100001),random.randint(0,106000)),
        "countryIssue": "CHN",
        "nationality": "CHN",
        "birthPlace": "CHN",
        "birthday": 894384000000,
        "email": "%sonedi2s%s@qq.com" %(random.randint(0,100000),random.randint(0,103000)),
        # "email": "onedi@qq.com" ,
        "phoneAreaCode": "HKG",
        "phone": "%s6253%s" %(random.randint(0,100002),random.randint(0,100502)),
        # "phone": "15089514626" ,
        "address": "3466324364",
        "addressMail": "34632646345",
        # "mailLanguage": "zh-hans",
        "mailLanguage": "",
        "employment": "retired",
        "employmentOther": "",
        "occupation": "",
        "employedPeriod": "",
        "employer": "",
        "businessType": "",
        "businessAddress": "",
        "businessPhone": ""
    }]
}
# print(data)

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())

