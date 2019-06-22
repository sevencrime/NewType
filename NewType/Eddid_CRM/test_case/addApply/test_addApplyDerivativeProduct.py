# usr/bin/env python
# -*- coding: utf-8 -*-

import time,os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
# import addApplyTool
from addApplyTool import addApplyTool
import unittest, pytest

class Test_addApplyDerivativeProduct(addApplyTool):
    # 校验衍生产品隐藏框是否必填

    """
    # 用例: 账户类别选择香港及环球证券账户(现金),校验衍生产品是否必填.
    #       衍生产品选择"否"
    """
    @addApplyTool.DerivativeProduct(num=1)
    def test_apply_CashNotDerivativeProduct(self):
        # 用例的前置条件
        addApplyTool.precondition()

        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别--选择香港及环球证券账户(现金)
        accountType = self.applypage.send_accountType("香港及环球证券账户(现金)")
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

    """
    # 用例: 账户类别选择香港及环球证券账户(现金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露不填
    """
    @addApplyTool.DerivativeProduct(num=0, linkTag=False)
    def test_apply_CashisDerivativeProductNone(self):
        # 用例的前置条件
        addApplyTool.precondition()

        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别--选择香港及环球证券账户(现金)
        accountType = self.applypage.send_accountType("香港及环球证券账户(现金)")
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

    """
    # 用例: 账户类别选择香港及环球证券账户(现金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露选 "是"
    """
    @addApplyTool.DerivativeProduct(num=0, linknum=0)
    def test_apply_CashisDerivativeProductyes(self):
        # 用例的前置条件
        addApplyTool.precondition()

        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别--选择香港及环球证券账户(现金)
        accountType = self.applypage.send_accountType("香港及环球证券账户(现金)")
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

    """
    # 用例: 账户类别选择香港及环球证券账户(现金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露选 "否"
    """
    @addApplyTool.DerivativeProduct(num=0, linknum=1)
    def test_apply_CashisDerivativeProductNo(self):
        # 用例的前置条件
        addApplyTool.precondition()

        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别--选择香港及环球证券账户(现金)
        accountType = self.applypage.send_accountType("香港及环球证券账户(现金)")
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


    """
    # 用例: 账户类别选择香港及环球证券账户(保证金),校验衍生产品是否必填.
    #       衍生产品选择"否"
    """
    @addApplyTool.DerivativeProduct(num=1)
    def test_apply_MarginNotDerivativeProduct(self):
        # 用例的前置条件
        addApplyTool.precondition()

        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别--选择香港及环球证券账户(现金)
        accountType = self.applypage.send_accountType("香港及环球证券账户(保证金)")
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

    """
    # 用例: 账户类别选择香港及环球证券账户(保证金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露不填
    """
    @addApplyTool.DerivativeProduct(num=0, linkTag=False)
    def test_apply_MarginisDerivativeProductNone(self):
        # 用例的前置条件
        addApplyTool.precondition()

        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别--选择香港及环球证券账户(保证金)
        accountType = self.applypage.send_accountType("香港及环球证券账户(保证金)")
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

    """
    # 用例: 账户类别选择香港及环球证券账户(保证金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露选 "是"
    """
    @addApplyTool.DerivativeProduct(num=0, linknum=0)
    def test_apply_MarginisDerivativeProductyes(self):
        # 用例的前置条件
        addApplyTool.precondition()

        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别--选择香港及环球证券账户(现金)
        accountType = self.applypage.send_accountType("香港及环球证券账户(保证金)")
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

    """
    # 用例: 账户类别选择香港及环球证券账户(保证金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露选 "否"
    """
    @addApplyTool.DerivativeProduct(num=0, linknum=1)
    def test_apply_MarginisDerivativeProductNo(self):
        # 用例的前置条件
        addApplyTool.precondition()
        
        # 账户类型
        applicationFor = self.applypage.send_applicationFor("个人账户")
        # 开户方法
        accountOpeningWay = self.applypage.send_accountOpeningWay("亲临开户")
        # 负责人
        parentId = self.applypage.send_parentId()
        # 邮件语言
        mailLanguage = self.applypage.send_mailLanguage("中文(简体)")
        # 账户类别--选择香港及环球证券账户(现金)
        accountType = self.applypage.send_accountType("香港及环球证券账户(保证金)")
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
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApplyDerivativeProduct))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

