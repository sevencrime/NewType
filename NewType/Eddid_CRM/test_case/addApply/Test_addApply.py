# usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-03 13:56:31
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import time,os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from PageElement import *
from Commons import *
from test_case.Test_Login import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class addApply(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        # self.driver.implicitly_wait(30)   
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.url = 'http://eddid-bos-uat.ntdev.be'

        Test_Login.LoginCRM(self)

        self.MenuListPage = MenuListPage.MenuListPage(self.driver, self.url, "Eddid")
        self.mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
        self.applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

    def tearDown(self):
        time.sleep(20)
        print("结束driver")
        self.driver.quit()

    # @unittest.skip("暂时跳过")
    def test1_addIndividual(self):
        # CRM开户列表,个人账户-随机

        # #点击开户管理，判断
        # self.MenuListPage.click_apply_manager()
        # #点击开户列表，判断
        # self.MenuListPage.click_applylist()
        self.MenuListPage.click_menulist("开户管理", "开户列表")
        #等待
        self.mainpage.wait_LoadingModal()
        #点击新增按钮
        self.mainpage.click_add()

        applicationFor = self.applypage.send_applicationFor("个人账户")
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        parentId = self.applypage.send_parentId()

        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")

        accountType = self.applypage.send_accountType("杠杆式外汇账户(保证金)")

        title = self.applypage.send_title()
        firstName = self.applypage.send_firstName()
        lastName = self.applypage.send_lastName()
        
        self.mainpage.wait_LoadingModal()

        chineseName = self.applypage.send_chineseName()
        emali = self.applypage.send_emali()
        phoneAreaCode = self.applypage.send_phoneAreaCode()
        phone = self.applypage.send_phone()
        address = self.applypage.send_address()
        addressMail = self.applypage.send_addressMail()
        nationality = self.applypage.send_nationality()
        idList = self.applypage.send_idType()
        # for i in range(len(idList)):
        #     if idList[0] == '其他':
        #         print(idList[i])
        #     else:
        #         print(idList[i])


        countryIssue = self.applypage.send_countryIssue()
        birthday = self.applypage.send_birthday()
        birthPlace = self.applypage.send_birthPlace()

        employments = self.applypage.employment()

        # if isinstance(employments, tuple):
        #     for i in range(len(employments)):
        #         if employments[0].get_attribute("value") == "就业" or employments[0].get_attribute("value") == "自雇":
        #             print(employments[i].get_attribute("value"))
        #         else:
        #             print(employments[i].get_attribute("value"))
        # else:
        #     print(employments.get_attribute("value"))

        self.applypage.uploadImage()
        
        totalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        netEstate = self.applypage.customerNetAssetValueHK()
        source_of_wealth = self.applypage.sourceOfWealth()
        securities = self.applypage.securities()
        CBBCcertificate = self.applypage.CBBC()
        derivativewarrant = self.applypage.warrants()
        futures = self.applypage.futures()
        Option = self.applypage.Option()
        foreignexchange = self.applypage.foreignExchange()
        bullion = self.applypage.bullion()
        otherInvest = self.applypage.otherInvestmentText()
        derivativeCourse = self.applypage.derivativeCourse()
        derivativeJobs = self.applypage.derivativeJobs()
        tradingFund = self.applypage.tradingFund()
        buyProduct = self.applypage.buyProduct()
        bankrupt = self.applypage.bankrupt()
        customerRelatives = self.applypage.customerRelatives()
        associatedcustomer = self.applypage.associatedcustomer()
        director = self.applypage.director()
        citizenOfUSA = self.applypage.citizenOfUSA()
        americanResident = self.applypage.americanResident()
        PEP_People = self.applypage.PEP_People()
        investmentTarget = self.applypage.investmentTarget()
        riskTolerance = self.applypage.riskTolerance()
        currency = self.applypage.bankaccount()
        marginAccount = self.applypage.marginAccount()
        discretion = self.applypage.discretion()
        companyAccounts = self.applypage.companyAccounts()
        channel = self.applypage.learnHow()
        beneficial = self.applypage.beneficial()
        Othed_People = self.applypage.Othed_People()
        jurisdiction = self.applypage.jurisdiction()
        acceptStatement = self.applypage.acceptStatement()
        useStatement = self.applypage.useStatement()

        self.applypage.click_sublimeApply("提交")

        self.mainpage.wait_LoadingModal()

        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交开户表单后跳转失败")


        # pymongo = PyMongo.Pymongo()
        # language = LanguagePack.LanguagePack.language   #语言包

        # result = pymongo.find('apply', {'applySeqId':1431})
        # # print(result)
        # self.assertEqual(language[applicationFor], result['applicationFor'], "applicationFor数据错误")
        # self.assertEqual(language[accountOpeningWay], result['accountOpeningWay'], "accountOpeningWay数据错误")

    @unittest.skip("暂时跳过")
    def test2_addJoint(self):
        # CRM开户列表,联名账户-随机

        #点击开户管理，判断
        self.MenuListPage.click_apply_manager()
        #点击开户列表，判断
        self.MenuListPage.click_applylist()
        #等待
        self.mainpage.wait_LoadingModal()
        #点击新增按钮
        self.mainpage.click_add()

        applicationFor = self.applypage.send_applicationFor("联名账户")
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        parentId = self.applypage.send_parentId()

        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")

        accountType = self.applypage.send_accountType("杠杆式外汇账户(保证金)")

        title = self.applypage.send_title()
        firstName = self.applypage.send_firstName()
        lastName = self.applypage.send_lastName()
        
        self.mainpage.wait_LoadingModal()

        chineseName = self.applypage.send_chineseName()
        emali = self.applypage.send_emali()
        phoneAreaCode = self.applypage.send_phoneAreaCode()
        phone = self.applypage.send_phone()
        address = self.applypage.send_address()
        addressMail = self.applypage.send_addressMail()
        nationality = self.applypage.send_nationality()
        idList = self.applypage.send_idType()

        countryIssue = self.applypage.send_countryIssue()
        birthday = self.applypage.send_birthday()
        birthPlace = self.applypage.send_birthPlace()

        employments = self.applypage.employment()
        
        self.applypage.uploadImage()
        
        totalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        netEstate = self.applypage.customerNetAssetValueHK()
        source_of_wealth = self.applypage.sourceOfWealth()
        securities = self.applypage.securities()
        CBBCcertificate = self.applypage.CBBC()
        derivativewarrant = self.applypage.warrants()
        futures = self.applypage.futures()
        Option = self.applypage.Option()
        foreignexchange = self.applypage.foreignExchange()
        bullion = self.applypage.bullion()
        otherInvest = self.applypage.otherInvestmentText()
        derivativeCourse = self.applypage.derivativeCourse()
        derivativeJobs = self.applypage.derivativeJobs()
        tradingFund = self.applypage.tradingFund()
        buyProduct = self.applypage.buyProduct()
        bankrupt = self.applypage.bankrupt()
        customerRelatives = self.applypage.customerRelatives()
        associatedcustomer = self.applypage.associatedcustomer()
        director = self.applypage.director()
        citizenOfUSA = self.applypage.citizenOfUSA()
        americanResident = self.applypage.americanResident()
        PEP_People = self.applypage.PEP_People()
        investmentTarget = self.applypage.investmentTarget()
        riskTolerance = self.applypage.riskTolerance()
        currency = self.applypage.bankaccount()
        marginAccount = self.applypage.marginAccount()
        discretion = self.applypage.discretion()
        companyAccounts = self.applypage.companyAccounts()
        channel = self.applypage.learnHow()
        beneficial = self.applypage.beneficial()
        Othed_People = self.applypage.Othed_People()
        jurisdiction = self.applypage.jurisdiction()
        acceptStatement = self.applypage.acceptStatement()
        useStatement = self.applypage.useStatement()

        self.applypage.click_sublimeApply("提交")

        title = self.applypage.send_title()
        primaryRelations = self.applypage.primaryRelations()    #联名账户-与主要账户的关系
        firstName = self.applypage.send_firstName()
        lastName = self.applypage.send_lastName()
        chineseName = self.applypage.send_chineseName()
        emali = self.applypage.send_emali()
        phoneAreaCode = self.applypage.send_phoneAreaCode()
        phone = self.applypage.send_phone()
        address = self.applypage.send_address()
        addressMail = self.applypage.send_addressMail()
        nationality = self.applypage.send_nationality()
        idList = self.applypage.send_idType()
        countryIssue = self.applypage.send_countryIssue()
        birthday = self.applypage.send_birthday()
        birthPlace = self.applypage.send_birthPlace()
        employments = self.applypage.employment()
        totalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        netEstate = self.applypage.customerNetAssetValueHK()
        source_of_wealth = self.applypage.sourceOfWealth()
        securities = self.applypage.securities()
        CBBCcertificate = self.applypage.CBBC()
        derivativewarrant = self.applypage.warrants()
        futures = self.applypage.futures()
        Option = self.applypage.Option()
        foreignexchange = self.applypage.foreignExchange()
        bullion = self.applypage.bullion()
        otherInvest = self.applypage.otherInvestmentText()
        derivativeCourse = self.applypage.derivativeCourse()
        derivativeJobs = self.applypage.derivativeJobs()
        tradingFund = self.applypage.tradingFund()
        buyProduct = self.applypage.buyProduct()
        bankrupt = self.applypage.bankrupt()
        customerRelatives = self.applypage.customerRelatives()
        associatedcustomer = self.applypage.associatedcustomer()
        director = self.applypage.director()
        citizenOfUSA = self.applypage.citizenOfUSA()
        americanResident = self.applypage.americanResident()
        PEP_People = self.applypage.PEP_People()
        self.applypage.click_sublimeApply("提交")

        self.mainpage.wait_LoadingModal()
        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交开户表单后跳转失败")

    @unittest.skip("暂时跳过")
    def test3_addJointFillAll(self):
        # CRM开户列表,联名账户-全部隐藏框

        #点击开户管理，判断
        self.MenuListPage.click_apply_manager()
        #点击开户列表，判断
        self.MenuListPage.click_applylist()
        #等待
        self.mainpage.wait_LoadingModal()
        #点击新增按钮
        self.mainpage.click_add()

        applicationFor = self.applypage.send_applicationFor("联名账户")
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        parentId = self.applypage.send_parentId()

        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")

        accountType = self.applypage.send_accountType("杠杆式外汇账户(保证金)")

        title = self.applypage.send_title()
        firstName = self.applypage.send_firstName()
        lastName = self.applypage.send_lastName()
        
        self.mainpage.wait_LoadingModal()

        chineseName = self.applypage.send_chineseName()
        emali = self.applypage.send_emali()
        phoneAreaCode = self.applypage.send_phoneAreaCode()
        phone = self.applypage.send_phone()
        address = self.applypage.send_address()
        addressMail = self.applypage.send_addressMail()
        nationality = self.applypage.send_nationality()
        idList = self.applypage.send_idType(3)

        countryIssue = self.applypage.send_countryIssue()
        birthday = self.applypage.send_birthday()
        birthPlace = self.applypage.send_birthPlace()

        employments = self.applypage.employment()

        
        self.applypage.uploadImage()
        
        totalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        netEstate = self.applypage.customerNetAssetValueHK()
        self.applypage.sourceOfWealth("其他")
        securities = self.applypage.securities()
        CBBCcertificate = self.applypage.CBBC()
        derivativewarrant = self.applypage.warrants()
        futures = self.applypage.futures()
        Option = self.applypage.Option()
        foreignexchange = self.applypage.foreignExchange()
        bullion = self.applypage.bullion()
        otherInvest = self.applypage.otherInvestmentText()
        derivativeCourse = self.applypage.derivativeCourse()
        derivativeJobs = self.applypage.derivativeJobs()
        tradingFund = self.applypage.tradingFund()
        buyProduct = self.applypage.buyProduct(0)
        bankrupt = self.applypage.bankrupt(0)
        customerRelatives = self.applypage.customerRelatives(0)
        associatedcustomer = self.applypage.associatedcustomer(0)
        director = self.applypage.director(0)
        citizenOfUSA = self.applypage.citizenOfUSA(0)
        americanResident = self.applypage.americanResident(0)
        PEP_People = self.applypage.PEP_People(0)
        investmentTarget = self.applypage.investmentTarget()
        riskTolerance = self.applypage.riskTolerance()
        currency = self.applypage.bankaccount(1)
        marginAccount = self.applypage.marginAccount(0)
        discretion = self.applypage.discretion(0)
        companyAccounts = self.applypage.companyAccounts(0)
        channel = self.applypage.learnHow()
        beneficial = self.applypage.beneficial(1)
        Othed_People = self.applypage.Othed_People(1)
        jurisdiction = self.applypage.jurisdiction()
        acceptStatement = self.applypage.acceptStatement()
        useStatement = self.applypage.useStatement()

        self.applypage.click_sublimeApply("提交")

        # self.driver.find_element_by_xpath("//div[contains(text(), '联名账户持有人资料')]").click()

        title = self.applypage.send_title()
        primaryRelations = self.applypage.primaryRelations()    #联名账户-与主要账户的关系
        firstName = self.applypage.send_firstName()
        lastName = self.applypage.send_lastName()
        chineseName = self.applypage.send_chineseName()
        emali = self.applypage.send_emali()
        phoneAreaCode = self.applypage.send_phoneAreaCode()
        phone = self.applypage.send_phone()
        address = self.applypage.send_address()
        addressMail = self.applypage.send_addressMail()
        nationality = self.applypage.send_nationality()
        idList = self.applypage.send_idType(3)
        countryIssue = self.applypage.send_countryIssue()
        birthday = self.applypage.send_birthday()
        birthPlace = self.applypage.send_birthPlace()
        employments = self.applypage.employment()
        totalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        netEstate = self.applypage.customerNetAssetValueHK()
        source_of_wealth = self.applypage.sourceOfWealth()
        securities = self.applypage.securities()
        CBBCcertificate = self.applypage.CBBC()
        derivativewarrant = self.applypage.warrants()
        futures = self.applypage.futures()
        Option = self.applypage.Option()
        foreignexchange = self.applypage.foreignExchange()
        bullion = self.applypage.bullion()
        otherInvest = self.applypage.otherInvestmentText()
        derivativeCourse = self.applypage.derivativeCourse()
        derivativeJobs = self.applypage.derivativeJobs()
        tradingFund = self.applypage.tradingFund()

        buyProduct = self.applypage.buyProduct(0)
        bankrupt = self.applypage.bankrupt(0)
        customerRelatives = self.applypage.customerRelatives(0)
        associatedcustomer = self.applypage.associatedcustomer(0)
        director = self.applypage.director(0)
        citizenOfUSA = self.applypage.citizenOfUSA(0)
        americanResident = self.applypage.americanResident(0)
        PEP_People = self.applypage.PEP_People(0)

        self.applypage.click_sublimeApply("提交")

        self.mainpage.wait_LoadingModal()
        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交开户表单后跳转失败")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApply))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

