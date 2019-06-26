#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from selenium import webdriver
import unittest
from test_case.Test_Login import *
from Commons import *
from PageElement import *
import time


class addApplyTool(unittest.TestCase):

    globals()["email"] = ""

    def setUp(self):
        globals()["email"] = ""
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        # self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(3)
        self.url = 'http://eddid-bos-uat.ntdev.be'

        self.MenuListPage = MenuListPage.MenuListPage(
            self.driver, self.url, "Eddid")
        self.mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
        self.applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")
        Test_Login.LoginCRM(self)

        self.MenuListPage.click_menulist("开户管理", "开户列表")
        # 等待
        self.mainpage.wait_LoadingModal()
        # 点击新增按钮
        self.mainpage.click_add()

    def tearDown(self):
        print("用例执行完成")
        self.driver.quit()
        # 删除数据
        print(globals()["email"])
        if globals()["email"] != "":
            PyMongo.Database().del_linked("apply_info", {"email": globals()["email"]})

    """
        #Apply 必填步骤
    """

    def RequiredField(self, *args, **kwargs):
        # 账户类型
        applicationFor = self.applypage.send_applicationFor(
            kwargs["applicationFor"])
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay(
            kwargs["way"])
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别
        accountType = self.applypage.send_accountType(kwargs["type"])
        # 称谓
        title = self.applypage.send_title()
        # 名字
        firstName = self.applypage.send_firstName()
        # 姓氏
        lastName = self.applypage.send_lastName()
        self.mainpage.wait_LoadingModal()  # 这里校验姓名是否重复
        # 中文姓名
        chineseName = self.applypage.send_chineseName()
        # 电邮
        globals()["email"] = self.applypage.send_emali()
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
        riskTolerance = self.applypage.riskTolerance(num=0)
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

    """
        #Apply 联名账户必填步骤
    """

    def JoinRequiredField(self):
        # 进入联名账户
        # 联名账户- 称谓
        Jointtitle = self.applypage.send_title()
        # 联名账户- 与主要账户持有人关系 + 触发的隐藏框
        Jointprimary = self.applypage.primaryRelations()
        # 联名账户- 名字
        JointfirstName = self.applypage.send_firstName()
        # 联名账户- 姓氏
        JointlastName = self.applypage.send_lastName()
        self.mainpage.wait_LoadingModal()  # 这里校验姓名是否重复
        # 联名账户-中文姓名
        JointchineseName = self.applypage.send_chineseName()
        # 联名账户- 电邮
        Jointemali = self.applypage.send_emali()
        # 联名账户- 电话号码区号
        JointphoneAreaCode = self.applypage.send_phoneAreaCode()
        # 联名账户- 电话号码
        Jointphone = self.applypage.send_phone()
        # 联名账户- 住宅地址
        Jointaddress = self.applypage.send_address()
        # 联名账户- 国籍
        Jointnationality = self.applypage.send_nationality()
        # 联名账户- 身份证件类型++身份证号码
        JointidList = self.applypage.send_idType()
        # 联名账户- 签发国家
        JointcountryIssue = self.applypage.send_countryIssue()
        # 联名账户- 出生日期
        Jointbirthday = self.applypage.send_birthday()
        # 联名账户- 出生地点
        JointbirthPlace = self.applypage.send_birthPlace()
        # 联名账户- 就业情况
        Jointemployments = self.applypage.employment()
        # 联名账户- 客户全年总收入
        JointtotalRevenue = self.applypage.totalAnnualCustomerRevenueHK()
        # 联名账户- 客户资产净值
        JointnetEstate = self.applypage.customerNetAssetValueHK()
        # 联名账户- 客户交易资金/财富来源
        Jointsource_of_wealth = self.applypage.sourceOfWealth()
        # 联名账户- 证券
        Jointsecurities = self.applypage.securities()
        # 联名账户- 牛熊证
        JointCBBCcertificate = self.applypage.CBBC()
        # 联名账户- 衍生权证
        Jointderivativewarrant = self.applypage.warrants()
        # 联名账户- 期货
        Jointfutures = self.applypage.futures()
        # 联名账户- 期权
        JointOption = self.applypage.Option()
        # 联名账户- 客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程
        JointderivativeCourse = self.applypage.derivativeCourse()
        # 联名账户- 客户是否从现时或过去拥有与衍生产品有关的工作经验?
        JointderivativeJobs = self.applypage.derivativeJobs()
        # 联名账户- 客户是否于过去3年曾执行 5次或以上有关衍生产品的交易，例如：衍生权证、牛熊证、股票期权、期货及期权、商品、结构性产品及交易所买卖基金等?
        JointtradingFund = self.applypage.tradingFund()
        # 联名账户- 客户是否曾经宣告破产或被申请破产?
        Jointbankrupt = self.applypage.bankrupt()
        # 联名账户- 客户是否艾德证券及/或艾德金业的雇员或任何其客户的亲属?
        JointcustomerRelatives = self.applypage.customerRelatives()
        # 联名账户- 客户是否与任何艾德证券及/或艾德金业客户有关连?
        Jointassociatedcustomer = self.applypage.associatedcustomer()
        # 联名账户- 客户是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士?
        Jointdirector = self.applypage.director()
        # 联名账户- 客户是否拥有美国公民或美国合法永久居民身份?
        JointcitizenOfUSA = self.applypage.citizenOfUSA()
        # 联名账户- 就税务而言，您是否美国居民?
        JointamericanResident = self.applypage.americanResident()
        # 联名账户- 客户是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系？
        JointPEP_People = self.applypage.PEP_People()
        # 联名账户- 本人确认并同意主要账户持有人之风险承受能力选择？
        self.applypage.jointRiskTolerance()

    """
        #提交表单按钮
    """

    def applySublime(self, Jump=True):
        # 点击提交按钮
        self.applypage.click_sublimeApply("提交")
        self.mainpage.wait_LoadingModal()  # loading
        try:
            if Jump == True:
                self.assertEqual(
                    self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交开户表单后跳转失败")
            else:
                self.assertEqual(
                    self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-create', "提交开户表单后跳转失败")

        except AssertionError:
            self.applypage.apply_error()
            raise AssertionError

    """
    开户方式装饰器
    用于校验开户方式所触发的隐藏框是否必填
    """
    def AccountOpeningWay(way):
        # 把开户方法变成装饰器实现
        def wrapper(func):
            def inner_wrapper(self, *args, **kwargs):
                try:
                    return func(self, *args, **kwargs)  # 执行用例
                except AssertionError:
                    print("断言失败,进行装饰器校验")
                    # 捕捉断言失败异常AssertionError
                    if way == "手机应用程式身份验证":
                        # 输入银行名称
                        self.applypage.send_appBankName()
                        # 输入银行账户号码
                        self.applypage.send_appBankAccount()
                    if way == "电子签名认证":
                        # 输入电子签名证书号码
                        self.applypage.send_appcertificateNb()

                    # 点击提交
                    self.applySublime()

                except Exception as e:
                    # 查找出报错的位置
                    print(e, "用例 {} 执行失败".format(func.__name__))
                    raise e

                else:
                    print("风险承受能力为低或为中可以提交成功, 用例'{}'执行失败".format(func.__name__))
                    raise AttributeError(
                        "用例 {} , 测试结果为失败".format(func.__name__))  # 只抛出异常

            return inner_wrapper
        return wrapper

    # 衍生产品隐藏框
    # 用于校验触发该隐藏框后是否必填
    """
    num : 下拉框选项,从上往下
    linkTag : 判断触发的隐藏框是否填写
    linknum : 触发的隐藏框的下拉框选项
    """
    def DerivativeProduct(num=None, linkTag=False, linknum=None):

        def wrapper(func):
            def inner_wrapper(self, *args, **kwargs):
                print("正在执行用例 {}".format(func.__name__))
                try:
                    return func(self, *args, **kwargs)
                except AssertionError:
                    print("断言失败,进行装饰器校验")
                    # 断言错误,提交失败,输入衍生产品隐藏框后再次点击提交按钮
                    # 输入衍生产品隐藏框
                    # import pdb; pdb.set_trace()
                    self.applypage.buyProduct(num, linkTag, linknum)
                    try:
                        self.applypage.click_sublimeApply("提交")
                        self.mainpage.wait_LoadingModal()  # loading
                        if linkTag == True or num == 1:
                            self.assertEqual(
                                self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交表单失败, 页面没有跳转")
                        else:
                            self.assertEqual(
                                self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-create', "表单没有停留在同一页")

                    except AssertionError:
                        # 断言失败, 数据提交失败
                        # 查找是否有数据为空,并打印出为空的栏位
                        self.applypage.apply_error()
                        raise AssertionError("断言失败(可能是接口报错)")

                    except Exception as e:
                        raise e

                except Exception as e:
                    # 查找出报错的位置
                    print(e, "用例 {} 执行失败".format(func.__name__))
                    raise e

                else:
                    print("风险承受能力为低或为中可以提交成功, 用例'{}'执行失败".format(func.__name__))
                    raise AttributeError(
                        "用例 {} , 测试结果为失败".format(func.__name__))  # 只抛出异常

            return inner_wrapper
        return wrapper

    # 风险承受能力装饰器

    def RiskTolerance(num=None):

        def wrapper(func):
            def inner_wrapper(self, *args, **kwargs):
                print("正在执行用例 :", func.__name__)
                try:
                    # import pdb; pdb.set_trace()
                    return func(self, *args, **kwargs)
                except AssertionError:
                    print("断言失败,进行装饰器校验")
                    # 风险承受能力
                    try:
                        # 输入风险承受能力
                        riskTolerance = self.applypage.riskTolerance(num)
                        if num == 0:
                            # 风险承受能力选择为"高"
                            self.applySublime()

                    except AttributeError:
                        print("点击风险承受能力方法有异常, 请优化方法")
                        raise AttributeError


                except Exception as e:
                    # 查找出报错的位置
                    print(e, "用例 {} 执行失败".format(func.__name__))
                    raise e

                else:
                    print("风险承受能力为空可以提交成功, 用例'{}'执行失败".format(func.__name__))
                    raise AttributeError(
                        "用例 {} , 测试结果为失败".format(func.__name__))  # 只抛出异常

            return inner_wrapper
        return wrapper


if __name__ == "__main__":
    print(sys.path)
    print(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))