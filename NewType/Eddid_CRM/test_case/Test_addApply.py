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
        accountOpeningWay = applypage.send_accountOpeningWay()
        parentId = applypage.send_parentId()
        mailLanguage = applypage.send_mailLanguage()

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
                    print(employments[i].get_attribut
                        e("value"))

        else:
            print(employments.get_attribute("value"))

        applypage.uploadImage()
        
        totalRevenue = applypage.totalRevenue()
        netEstate = applypage.netEstate()
        source_of_wealth = applypage.source_of_wealth()
        securities = applypage.securities()
        CBBCcertificate = applypage.CBBCcertificate()
        derivativewarrant = applypage.derivativewarrant()
        futures = applypage.futures()
        Option = applypage.Option()
        foreignexchange = applypage.foreignexchange()
        bullion = applypage.bullion()
        otherInvest = applypage.otherInvest()
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
        currency = applypage.currency()
        marginAccount = applypage.marginAccount()
        discretion = applypage.discretion()
        companyAccounts = applypage.companyAccounts()
        channel = applypage.channel()
        beneficial = applypage.beneficial()
        Othed_People = applypage.Othed_People()
        jurisdiction = applypage.jurisdiction()
        acceptStatement = applypage.acceptStatement()
        useStatement = applypage.useStatement()

        applypage.click_sublime()

        mainpage.wait_LoadingModal()






if __name__ == '__main__':
    unittest.main()


