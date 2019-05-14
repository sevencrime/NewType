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

url = 'https://eddid-api.ntdev.be/eddid-api-feature/apply/create'
headers = {
    'Content-Type' : 'application/json' ,
    'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoidGVzdCIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiJhYzYzZWNjOC03NjI4LTExZTktOWUzYy00OTA5MTUzMmY2NWIiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU1NzgyNTI2NywiZXhwIjoxNTU3ODI4ODY3LCJpYXQiOjE1NTc4MjUyNjcsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluMTIzNEAxNjMuY29tIn0.MF5ua47FW6O6A8DPMk7eQA2FQe93HoRB96K5lCHdn0Vt3FoA84cn_0xD83zsvgWxDKSah7YQV7zMg7__JdneGrGjXtpkvZJX7YuoA0chNrGWJYiaHGXR7YLVIWcOI8Oygtin4jisclA0eK8sW3dzN1yg2PqkvlxrCQRgqjPB0NJsN29BgxL4cZc70pDXXLXr726y3XU0umKjNUQaqXsEr6r10o-Rgm0XyVloZncKveEbKtMdDOrZk3f1foqESkd1LuRxaZubLm8bQm8Phd95njQuQ6qXd8oYU3D80uUnujQCQ5_qlUzh_g6QmG_R1DBrO015MMxr9GLqy8O-8VETfw'

}


data = {
    "updateEmail": False,
    "status": "unprocessed",
    "applicationFor": "individual",
    "accountType": ["securitiesCash", "futuresMargin", "leveragedForeignExchangeAccountMargin"],
    "learnHowCode": "",
    "learnHow": ["searchEngine", "socialMedia"],
    "referralCode": "",
    "certStatus": "certNew",
    "appBankName": "",
    "appCertSn": "64E15A95938A6CDE",
    "appCertDn": "CN=郑钦元,OU=441502199602120215,OU=115,O=0,L=汕尾市,ST=广东省,C=CN",
    "appFileId": "",
    "isReSubmit": "N",
    "client": [{
        "title": "mr",
        "firstName": "Qinyuan",
        "lastName": "Zheng",
        "chineseName": "郑钦元",
        "pastEnglishName": "",
        "email": "15089514626@sina.com",
        "phoneAreaCode": "CHN",
        "phone": "15089514626",
        "address": "东省汕尾市城区新港街道新港海滨居委广场路一巷48号101",
        "syncIDAddress": "Y",
        "isHongKongBankCard": "Y",
        "addressRegionProvince": "",
        "addressRegionCity": "",
        "addressRegionArea": "",
        "addressDetailed": "",
        "addressMail": "",
        "nationality": "CHN",
        "idType": "2",
        "idNumber": "441502199602120215",
        "countryIssue": "CHN",
        "birthday": 824083200000,
        "birthPlace": "CHN",
        "idCardAddress": "东省汕尾市城区新港街道新港海滨居委广场路一巷48号101",
        "idCardAddressReadOnly": "东省汕尾市城区新港街道新港海滨居委广场路一巷48号101",
        "employment": "unemployed",
        "occupation": "",
        "employedPeriod": "",
        "employer": "",
        "businessType": "",
        "businessAddress": "",
        "businessAddressRegionProvince": "",
        "businessAddressRegionCity": "",
        "businessAddressRegionArea": "",
        "businessAddressDetailed": "",
        "businessPhone": "",
        "riskInfo": {
            "isReferralCode": "Y",
            "isApplyToOpenTradingStructure": "Y",
            "isTradingStructureAggree": "Y",
            "disclaimerVideo": "57586b06-fe96-4a50-b7bf-816d3bb749b6.mp4",
            "passportMaterial": ["a731d094-201f-4f8e-8b42-d84cd32b9601.jpg", "c21d999f-ccb7-4765-8b67-6ed5374eacc7.jpg"],
            "sourceOfWealthOther": "",
            "addressVerificationMaterials": [],
            "bankCardMaterials": [],
            "writtenApplicationMaterials": ["ceae2f70-75f5-11e9-a894-e529367e5a5c.pdf"],
            "proofOfIncome": [],
            "otherInformation": [],
            "totalAnnualCustomerRevenueHK": "lt200000",
            "totalAnnualCustomerRevenueHKOther": "",
            "customerNetAssetValueHK": "lt1000000",
            "customerNetAssetValueHKOther": "",
            "sourceOfWealth": ["savings", "investment"],
            "securities": "1To5Years",
            "CBBC": "lt1Year",
            "warrants": "lt1Year",
            "futures": "1To5Years",
            "options": "lt1Year",
            "algoTrade": "lt1Year",
            "isAlgoTrade": "",
            "isAlgoTradeAggree": "",
            "bullion": "lt1Year",
            "foreignExchange": "lt1Year",
            "otherInvestmentText": "",
            "otherInvestment": "",
            "isLearnAboutProducts": "Y",
            "isIndustryExperience": "Y",
            "isStocks": "Y",
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
            "purposeOfInvestment": ["speculation", "hedging", "income"],
            "riskTolerance": "high"
        }
    }],
    "learnHowOther": "",
    "parentId": "kwokwah.wong",
    "bankAccount": [],
    "currency": "",
    "accountOpeningWay": "electronicAuth",
    "IBparentId": "",
    "mailLanguage": "zh-hans",
    "isMarginAccount": "",
    "marginAccountName": "",
    "marginAccountNumber": "",
    "isDiscretion": "",
    "discretionName": "",
    "discretionNumber": "",
    "isCompanyAccounts": "",
    "companyAccountsName": "",
    "companyAccountsNumber": "",
    "isBeneficiary": "Y",
    "beneficiaryName": "",
    "isOrders": "Y",
    "ordersName": "",
    # "isRelatedAccounts": ["opt"],
    # "relatedAccountsOpt": ["opt"],
    "agreeToTheTerms": "Y",
    "personalInfoDeclartion": "Y",
    "appVersion": "v1.3.2",
    "deviceModel": "iPhone 6s Plus/iOS:10.3.3",
    "step": "17"
}



# print(data)
urllib3.disable_warnings()
resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
print(resp.json())

