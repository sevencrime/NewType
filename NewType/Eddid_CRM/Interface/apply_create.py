#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib3

from Commons import GlobalMap, Logging

import requests 
import json
import random


def apply_create_api():

    gm = GlobalMap.GlobalMap()
    log = Logging.Logs()
 
    url = 'https://eddid-api.ntdev.be/eddid-api-uat/apply/create'

    headers = {
        'Content-Type' : 'application/json' ,
        'X-Token' : gm.get_value("token")
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
