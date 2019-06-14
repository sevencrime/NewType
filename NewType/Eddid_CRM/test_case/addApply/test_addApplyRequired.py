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
from selenium.common.exceptions import *


class addApplyRequired(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        # self.driver.implicitly_wait(30)   
        self.driver.set_page_load_timeout(35)
        self.driver.set_script_timeout(35)
        self.url = 'http://eddid-bos-uat.ntdev.be'

        self.MenuListPage = MenuListPage.MenuListPage(self.driver, self.url, "Eddid")
        self.mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
        self.applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

        Test_Login.LoginCRM(self)
        self.MenuListPage.click_menulist("开户管理", "开户列表")
        #等待
        self.mainpage.wait_LoadingModal()
        #点击新增按钮
        self.mainpage.click_add()

    def tearDown(self):
        time.sleep(20)
        print("结束driver")
        self.driver.quit()

    def AccountOpeningWay(way):
        # 把开户方法变成装饰器实现
        def wrapper(func):
            def inner_wrapper(self):
                # 点击选择开户方法
                accountOpeningWay = self.applypage.send_accountOpeningWay(way)
                assert way in accountOpeningWay

                try:
                    return func(self)   #执行用例
                except AssertionError:
                    # 捕捉断言失败异常AssertionError
                    if way == "手机应用程式身份验证":
                        # 输入银行名称
                        self.applypage.send_appBankName()
                        # 输入银行账户号码
                        self.applypage.send_appBankAccount()
                    if way == "电子签名认证":
                        # 输入电子签名证书号码
                        self.applypage.send_appcertificateNb()

                    #点击提交
                    try:
                        self.applypage.click_sublimeApply("提交")
                        self.mainpage.wait_LoadingModal()   #loading
                        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交表单失败, 页面没有跳转")
                        
                    except AssertionError:
                        import pdb; pdb.set_trace()
                        # 断言失败, 数据提交失败
                        # 查找是否有数据为空,并打印出为空的栏位
                        self.applypage.apply_error()

                    except Exception as e:
                        raise e

                except Exception as e:
                    # 查找出报错的位置
                    print(e, "用例执行失败")
                    raise e

                else:
                    # 用例执行失败
                    print(way, "没有输入必填参数")
                    assert 1 > 0    #只抛出异常

            return inner_wrapper
        return wrapper

    @unittest.skip("跳过")
    def test_apply_Required(self):
        # 用例: 个人账户--必填参数
        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别
        accountType = self.applypage.send_accountType("香港股票期权账户(现金)")
        # 称谓
        title = self.applypage.send_title()
        # 名字
        firstName = self.applypage.send_firstName()
        # 姓氏
        lastName = self.applypage.send_lastName()
        self.mainpage.wait_LoadingModal() # 这里校验姓名是否重复
        # 中文姓名
        chineseName = self.applypage.send_chineseName()
        # 电邮
        emali = self.applypage.send_emali()
        # 电话号码区号
        phoneAreaCode = self.applypage.send_phoneAreaCode()
        # 电话号码
        phone = self.applypage.send_phone()
        # 住宅地址
        address = self.applypage.send_address()
        # 国籍
        nationality = self.applypage.send_nationality()
        # 身份证件类型++身份证号码
        idList = self.applypage.send_idType()
        # 签发国家
        countryIssue = self.applypage.send_countryIssue()
        # 出生日期
        birthday = self.applypage.send_birthday()
        # 出生地点
        birthPlace = self.applypage.send_birthPlace()
        # 就业情况,职位, 受雇年限, 目前雇主名称, 业务性质,办公司地址
        employments = self.applypage.employment()
        # 客户全年总收入
        totalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        # 客户资产净值
        netEstate = self.applypage.customerNetAssetValueHK()
        # 客户交易资金/财富来源
        source_of_wealth = self.applypage.sourceOfWealth()
        # 证券
        securities = self.applypage.securities()
        # 牛熊证
        CBBCcertificate = self.applypage.CBBC()
        # 衍生权证
        derivativewarrant = self.applypage.warrants()
        # 期货
        futures = self.applypage.futures()
        # 期权
        Option = self.applypage.Option()
        # 客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程
        derivativeCourse = self.applypage.derivativeCourse()
        # 客户是否从现时或过去拥有与衍生产品有关的工作经验? 
        derivativeJobs = self.applypage.derivativeJobs()
        # 客户是否于过去3年曾执行 5次或以上有关衍生产品的交易，例如：衍生权证、牛熊证、股票期权、期货及期权、商品、结构性产品及交易所买卖基金等?
        tradingFund = self.applypage.tradingFund()
        # 客户是否曾经宣告破产或被申请破产?
        bankrupt = self.applypage.bankrupt()
        # 客户是否艾德证券及/或艾德金业的雇员或任何其客户的亲属?
        customerRelatives = self.applypage.customerRelatives()
        # 客户是否与任何艾德证券及/或艾德金业客户有关连?
        associatedcustomer = self.applypage.associatedcustomer()
        # 客户是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士?
        director = self.applypage.director()
        # 客户是否拥有美国公民或美国合法永久居民身份?
        citizenOfUSA = self.applypage.citizenOfUSA()
        # 就税务而言，您是否美国居民?
        americanResident = self.applypage.americanResident()
        # 客户是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系？
        PEP_People = self.applypage.PEP_People()
        # 客户的投资目标是:
        investmentTarget = self.applypage.investmentTarget()
        # 客户的风险承受能力是:---需校验
        riskTolerance = self.applypage.riskTolerance()
        # 结算账户-货币
        currency = self.applypage.bankaccount()
        # 介绍与推广--您透过哪些渠道认识艾德证券及/或艾德金业?(选择所有适用)
        channel = self.applypage.learnHow()
        # 客户是否账户的最终实益拥有人?
        beneficial = self.applypage.beneficial()
        # 客户是否最终负责下单的人?
        Othed_People = self.applypage.Othed_People()
        # 请选择您就税务用途的居留司法管辖区(您可选多一项)
        jurisdiction = self.applypage.jurisdiction()
        # 本人接受上述声明
        acceptStatement = self.applypage.acceptStatement()
        # 个人资料之使用声明
        useStatement = self.applypage.useStatement()

        # 点击提交按钮
        self.applypage.click_sublimeApply("提交")
        self.mainpage.wait_LoadingModal()   #loading
        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交开户表单后跳转失败")

    @AccountOpeningWay(way="手机应用程式身份验证")
    def test_apply_MobileAuthentication(self):
        # 用例: 手机应用程式身份认证--校验银行名称和银行账户号码是否必填
        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        # accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别
        accountType = self.applypage.send_accountType("香港股票期权账户(现金)")
        # 称谓
        title = self.applypage.send_title()
        # 名字
        firstName = self.applypage.send_firstName()
        # 姓氏
        lastName = self.applypage.send_lastName()
        self.mainpage.wait_LoadingModal() # 这里校验姓名是否重复
        # 中文姓名
        chineseName = self.applypage.send_chineseName()
        # 电邮
        emali = self.applypage.send_emali()
        # 电话号码区号
        phoneAreaCode = self.applypage.send_phoneAreaCode()
        # 电话号码
        phone = self.applypage.send_phone()
        # 住宅地址
        address = self.applypage.send_address()
        # 国籍
        nationality = self.applypage.send_nationality()
        # 身份证件类型++身份证号码
        idList = self.applypage.send_idType()
        # 签发国家
        countryIssue = self.applypage.send_countryIssue()
        # 出生日期
        birthday = self.applypage.send_birthday()
        # 出生地点
        birthPlace = self.applypage.send_birthPlace()
        # 就业情况,职位, 受雇年限, 目前雇主名称, 业务性质,办公司地址
        employments = self.applypage.employment()
        # 客户全年总收入
        totalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        # 客户资产净值
        netEstate = self.applypage.customerNetAssetValueHK()
        # 客户交易资金/财富来源
        source_of_wealth = self.applypage.sourceOfWealth()
        # 证券
        securities = self.applypage.securities()
        # 牛熊证
        CBBCcertificate = self.applypage.CBBC()
        # 衍生权证
        derivativewarrant = self.applypage.warrants()
        # 期货
        futures = self.applypage.futures()
        # 期权
        Option = self.applypage.Option()
        # 客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程
        derivativeCourse = self.applypage.derivativeCourse()
        # 客户是否从现时或过去拥有与衍生产品有关的工作经验? 
        derivativeJobs = self.applypage.derivativeJobs()
        # 客户是否于过去3年曾执行 5次或以上有关衍生产品的交易，例如：衍生权证、牛熊证、股票期权、期货及期权、商品、结构性产品及交易所买卖基金等?
        tradingFund = self.applypage.tradingFund()
        # 客户是否曾经宣告破产或被申请破产?
        bankrupt = self.applypage.bankrupt()
        # 客户是否艾德证券及/或艾德金业的雇员或任何其客户的亲属?
        customerRelatives = self.applypage.customerRelatives()
        # 客户是否与任何艾德证券及/或艾德金业客户有关连?
        associatedcustomer = self.applypage.associatedcustomer()
        # 客户是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士?
        director = self.applypage.director()
        # 客户是否拥有美国公民或美国合法永久居民身份?
        citizenOfUSA = self.applypage.citizenOfUSA()
        # 就税务而言，您是否美国居民?
        americanResident = self.applypage.americanResident()
        # 客户是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系？
        PEP_People = self.applypage.PEP_People()
        # 客户的投资目标是:
        investmentTarget = self.applypage.investmentTarget()
        # 客户的风险承受能力是:---需校验
        riskTolerance = self.applypage.riskTolerance()
        # 结算账户-货币
        currency = self.applypage.bankaccount()
        # 介绍与推广--您透过哪些渠道认识艾德证券及/或艾德金业?(选择所有适用)
        channel = self.applypage.learnHow()
        # 客户是否账户的最终实益拥有人?
        beneficial = self.applypage.beneficial()
        # 客户是否最终负责下单的人?
        Othed_People = self.applypage.Othed_People()
        # 请选择您就税务用途的居留司法管辖区(您可选多一项)
        jurisdiction = self.applypage.jurisdiction()
        # 本人接受上述声明
        acceptStatement = self.applypage.acceptStatement()
        # 个人资料之使用声明
        useStatement = self.applypage.useStatement()

        # 点击提交按钮
        self.applypage.click_sublimeApply("提交")
        self.mainpage.wait_LoadingModal()   #loading
        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交表单失败")


    @AccountOpeningWay(way="电子签名认证")
    def test_apply_certificateNb(self):
        # 用例: 电子签名认证--校验电子签名证书栏位是否必填
        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        # accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别
        accountType = self.applypage.send_accountType("香港股票期权账户(现金)")
        # 称谓
        title = self.applypage.send_title()
        # 名字
        firstName = self.applypage.send_firstName()
        # 姓氏
        lastName = self.applypage.send_lastName()
        self.mainpage.wait_LoadingModal() # 这里校验姓名是否重复
        # 中文姓名
        chineseName = self.applypage.send_chineseName()
        # 电邮
        emali = self.applypage.send_emali()
        # 电话号码区号
        phoneAreaCode = self.applypage.send_phoneAreaCode()
        # 电话号码
        phone = self.applypage.send_phone()
        # 住宅地址
        address = self.applypage.send_address()
        # 国籍
        nationality = self.applypage.send_nationality()
        # 身份证件类型++身份证号码
        idList = self.applypage.send_idType()
        # 签发国家
        countryIssue = self.applypage.send_countryIssue()
        # 出生日期
        birthday = self.applypage.send_birthday()
        # 出生地点
        birthPlace = self.applypage.send_birthPlace()
        # 就业情况,职位, 受雇年限, 目前雇主名称, 业务性质,办公司地址
        employments = self.applypage.employment()
        # 客户全年总收入
        totalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        # 客户资产净值
        netEstate = self.applypage.customerNetAssetValueHK()
        # 客户交易资金/财富来源
        source_of_wealth = self.applypage.sourceOfWealth()
        # 证券
        securities = self.applypage.securities()
        # 牛熊证
        CBBCcertificate = self.applypage.CBBC()
        # 衍生权证
        derivativewarrant = self.applypage.warrants()
        # 期货
        futures = self.applypage.futures()
        # 期权
        Option = self.applypage.Option()
        # 客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程
        derivativeCourse = self.applypage.derivativeCourse()
        # 客户是否从现时或过去拥有与衍生产品有关的工作经验? 
        derivativeJobs = self.applypage.derivativeJobs()
        # 客户是否于过去3年曾执行 5次或以上有关衍生产品的交易，例如：衍生权证、牛熊证、股票期权、期货及期权、商品、结构性产品及交易所买卖基金等?
        tradingFund = self.applypage.tradingFund()
        # 客户是否曾经宣告破产或被申请破产?
        bankrupt = self.applypage.bankrupt()
        # 客户是否艾德证券及/或艾德金业的雇员或任何其客户的亲属?
        customerRelatives = self.applypage.customerRelatives()
        # 客户是否与任何艾德证券及/或艾德金业客户有关连?
        associatedcustomer = self.applypage.associatedcustomer()
        # 客户是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士?
        director = self.applypage.director()
        # 客户是否拥有美国公民或美国合法永久居民身份?
        citizenOfUSA = self.applypage.citizenOfUSA()
        # 就税务而言，您是否美国居民?
        americanResident = self.applypage.americanResident()
        # 客户是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系？
        PEP_People = self.applypage.PEP_People()
        # 客户的投资目标是:
        investmentTarget = self.applypage.investmentTarget()
        # 客户的风险承受能力是:---需校验
        riskTolerance = self.applypage.riskTolerance()
        # 结算账户-货币
        currency = self.applypage.bankaccount()
        # 介绍与推广--您透过哪些渠道认识艾德证券及/或艾德金业?(选择所有适用)
        channel = self.applypage.learnHow()
        # 客户是否账户的最终实益拥有人?
        beneficial = self.applypage.beneficial()
        # 客户是否最终负责下单的人?
        Othed_People = self.applypage.Othed_People()
        # 请选择您就税务用途的居留司法管辖区(您可选多一项)
        jurisdiction = self.applypage.jurisdiction()
        # 本人接受上述声明
        acceptStatement = self.applypage.acceptStatement()
        # 个人资料之使用声明
        useStatement = self.applypage.useStatement()

        # 点击提交按钮
        self.applypage.click_sublimeApply("提交")
        self.mainpage.wait_LoadingModal()   #loading
        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交表单失败")



if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApplyRequired))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

