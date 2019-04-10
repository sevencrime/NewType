#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-03 13:56:31
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import time,os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from PageElement import *
from Commons import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class addApply(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        self.driver.implicitly_wait(30)
        self.url = 'http://eddid-bos-uat.ntdev.be'


        #在这里先登录
        login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
        login_page.open()
        login_page.input_username("admin")
        login_page.input_password("abcd1234")
        login_page.click_submit()
        self.assertEqual("admin", login_page.show_userid(), "userid与登录账户不一致")

    def tearDown(self):
        time.sleep(20)
        print("结束driver")
        self.driver.quit()

    def test_addApply(self):
        applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
        mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
        applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

        #点击开户管理，判断
        applylistpage.click_apply_manager()
        #点击开户列表，判断
        applylistpage.click_applylist()
        #等待
        mainpage.wait_LoadingModal()
        #点击新增按钮
        mainpage.click_add()

        applicationFor = applypage.send_applicationFor("个人账户")
        accountOpeningWay = applypage.send_accountOpeningWay("亲临开户")
        parentId = applypage.send_parentId()

        mailLanguage = applypage.send_mailLanguage("中文(简体)")

        accountType = applypage.send_accountType("杠杆式外汇账户(保证金)")

        title = applypage.send_title()
        firstName = applypage.send_firstName()
        lastName = applypage.send_lastName()
        
        mainpage.wait_LoadingModal()

        chineseName = applypage.send_chineseName()
        emali = applypage.send_emali()
        phoneAreaCode = applypage.send_phoneAreaCode()
        phone = applypage.send_phone()
        address = applypage.send_address()
        addressMail = applypage.send_addressMail()
        nationality = applypage.send_nationality()
        idList = applypage.send_idType()
        for i in range(len(idList)):
            if idList[0] == '其他':
                print(idList[i])
            else:
                print(idList[i])


        countryIssue = applypage.send_countryIssue()
        birthday = applypage.send_birthday()
        birthPlace = applypage.send_birthPlace()

        employments = applypage.employment()
        if isinstance(employments, tuple):
            for i in range(len(employments)):
                if employments[0].get_attribute("value") == "就业" or employments[0].get_attribute("value") == "自雇":
                    print(employments[i].get_attribute("value"))
                else:
                    print(employments[i].get_attribute("value"))
        else:
            print(employments.get_attribute("value"))

        applypage.uploadImage()
        
        totalRevenue = applypage.totalAnnualCustomerRevenueHK()
        netEstate = applypage.customerNetAssetValueHK()
        source_of_wealth = applypage.sourceOfWealth()
        securities = applypage.securities()
        CBBCcertificate = applypage.CBBC()
        derivativewarrant = applypage.warrants()
        futures = applypage.futures()
        Option = applypage.Option()
        foreignexchange = applypage.foreignExchange()
        bullion = applypage.bullion()
        otherInvest = applypage.otherInvestmentText()
        derivativeCourse = applypage.derivativeCourse()
        derivativeJobs = applypage.derivativeJobs()
        tradingFund = applypage.tradingFund()
        buyProduct = applypage.buyProduct()
        bankrupt = applypage.bankrupt()
        customerRelatives = applypage.customerRelatives()
        associatedcustomer = applypage.associatedcustomer()
        director = applypage.director()
        citizenOfUSA = applypage.citizenOfUSA()
        americanResident = applypage.americanResident()
        PEP_People = applypage.PEP_People()
        investmentTarget = applypage.investmentTarget()
        riskTolerance = applypage.riskTolerance()
        currency = applypage.bankaccount()
        marginAccount = applypage.marginAccount()
        discretion = applypage.discretion()
        companyAccounts = applypage.companyAccounts()
        channel = applypage.learnHow()
        beneficial = applypage.beneficial()
        Othed_People = applypage.Othed_People()
        jurisdiction = applypage.jurisdiction()
        acceptStatement = applypage.acceptStatement()
        useStatement = applypage.useStatement()

        applypage.click_sublime()

        mainpage.wait_LoadingModal()

        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交开户表单后跳转失败")


        pymongo = PyMongo.Pymongo()
        language = LanguagePack.LanguagePack.language   #语言包

        result = pymongo.find('apply', {'applySeqId':1431})
        # print(result)
        self.assertEqual(language[applicationFor], result['applicationFor'], "applicationFor数据错误")
        self.assertEqual(language[accountOpeningWay], result['accountOpeningWay'], "accountOpeningWay数据错误")





if __name__ == '__main__':
    unittest.main()


