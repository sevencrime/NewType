#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-14 21:30:24
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import os,sys,time
import random
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ApplyPage(BasePage.BasePage):
    # log = Logging.Logs()

    def get_input(self, text, other=False):
        if not other:
            input_loc = (By.XPATH, "//div[contains(text(), '%s')]/following-sibling::span//input" %text)
        else:
            input_loc = (By.XPATH, "//div[contains(text(), '%s')]/parent::div/following-sibling::*//input" %text)

        return input_loc

    def get_derivativeInput(self, text):
        derivativeInput_loc = (By.XPATH, "//div[contains(text(), '%s')]/parent::div/following-sibling::div//input" %text)
        return derivativeInput_loc

    def get_checkbox(self, text):
    	checkbox_loc = (By.XPATH, "//span[contains(text(), '%s')]/preceding-sibling::span" %text)
    	return checkbox_loc

    def get_select(self, text=False, top=False):
        if not text:
            if top:
                select_loc = (By.XPATH, "//div[@x-placement = 'top-start']//li")
            else:
                select_loc = (By.XPATH, "//div[@x-placement = 'bottom-start']//li")

            selectlist = self.find_elements(*select_loc)
            randox = random.randint(0,len(selectlist))
            for i in range(len(selectlist)):
                if i == randox:
                    # selectlist[i].click()
                    # js.executeScript("var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);", findElement(element));

                    # time.sleep(0.1)
                    self.scrollinto(selectlist[i])
                    return selectlist[i]

        else:
            # print("进入这里", text)
            select_loc = (By.XPATH, "//span[contains(text(), '%s')]" %text) 

            return select_loc

    def del_readonly(self, loc):
        self.script('arguments[0].removeAttribute(\"readonly\")', loc);

    def get_radio(self, text):
        radio_loc = (By.XPATH, "//div[contains(text(), '%s')]/following-sibling::span//label[1]" %text)
        return radio_loc

    def get_action(self, text):
        print("action")
        others_loc = (By.XPATH, "//div[contains(text(), '%s')]" %text)
        # time.sleep(5)
        ActionChains(self.driver).click(self.find_element(*others_loc)).perform()

    def scrollinto(self, loc):
        self.script("arguments[0].scrollIntoView();", loc)
        loc.click()


    # 账户类型
    def send_applicationFor(self):
        self.find_element(*self.get_input('账户类型')).click()
        self.find_element(*self.get_select(text='个人账户')).click()

    # 开户方法
    def send_accountOpeningWay(self):
        self.find_element(*self.get_input('开户方法')).click()
        self.find_element(*self.get_select(text='亲临开户')).click()

    # 负责人
    def send_parentId(self):
        self.find_element(*self.get_input('负责人')).click()
        self.find_element(*self.get_select(text='sales_t1')).click()

    # 邮件语言
    def send_mailLanguage(self):
        self.find_element(*self.get_input('邮件语言')).click()
        self.find_element(*self.get_select(text='中文(简体)')).click()


    def send_accountType(self):
        self.find_element(*self.get_checkbox('香港及环球证券账户(现金)')).click()

    def send_title(self):
        self.find_element(*self.get_input('称谓')).click()
        self.find_element(*self.get_select(text='先生')).click()

    def send_firstName(self):
        self.find_element(*self.get_input('名字')).send_keys("firstName")

    def send_lastName(self):
        self.find_element(*self.get_input('姓氏')).send_keys("lastName")
        self.find_element(*self.get_input('姓氏')).send_keys(Keys.ENTER)
        # time.sleep(5)

    def send_chineseName(self):
        self.find_element(*self.get_input('中文姓名')).send_keys("郑某人")

    def send_emali(self):
        self.find_element(*self.get_input('电邮')).send_keys("oneditest@gmail.com")

    def send_phoneAreaCode(self):
        phoneAreaCode = self.find_element(*self.get_input('电话号码区号'))
        self.scrollinto(phoneAreaCode)
        # time.sleep(1)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def send_phone(self):
        self.find_element(*self.get_input("电话号码(用于通讯)")).send_keys("15089510001")

    def send_address(self):
        self.find_element(*self.get_input("住宅地址(不接受邮政信箱)")).send_keys("桑达科技大厦802")

    def send_addressMail(self):
        self.find_element(*self.get_input("邮寄地址(如与住宅地址不同)")).send_keys("桑达科技大厦802")

    def send_nationality(self):
        # print("send_nationality")
        nationality = self.find_element(*self.get_input("国籍"))
        self.scrollinto(nationality)
        # time.sleep(0.5)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def send_idType(self):
        idType = self.find_element(*self.get_input("身份证件类型"))
        # time.sleep(0.5)
        self.scrollinto(idType)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        if selectelement.get_attribute("textContent") == "其他":
            self.find_element(*self.get_input("其他证件类型")).send_keys("idType")
            self.find_element(*self.get_input("其他证件号码")).send_keys("43110120215251")
        else:
            self.find_element(*self.get_input("身份证或护照号码")).send_keys("44150266621212")


    def send_countryIssue(self):
        countryIssue = self.find_element(*self.get_input("签发国家"))
        # time.sleep(0.5)
        self.scrollinto(countryIssue)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def send_birthday(self):
        self.find_element(*self.get_input("出生日期(日/月/年)")).send_keys("21/01/2000")
        self.find_element(*self.get_input("出生日期(日/月/年)")).send_keys(Keys.ENTER)

    def send_birthPlace(self):
        birthPlace = self.find_element(*self.get_input('出生地点'))
        # time.sleep(0.5)
        self.scrollinto(birthPlace)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def employment(self):
        employment = self.find_element(*self.get_input("就业情况"))
        # time.sleep(0.5)
        self.scrollinto(employment)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))        

        if selectelement.get_attribute("textContent") == "就业" or selectelement.get_attribute("textContent") == "自雇":        
            occupation = self.find_element(*self.get_input("职位")).send_keys("销售")
            employedPeriod = self.find_element(*self.get_input("受雇年期")).send_keys("十年以上")
            employer = self.find_element(*self.get_input("目前雇主名称")).send_keys("newtype")
            businessType = self.find_element(*self.get_input("业务性质")).send_keys("互联网")
            businessAddress = self.find_element(*self.get_input("办公室地址")).send_keys("广东省深圳市南山区桑达科技大厦802")
            businessPhone = self.find_element(*self.get_input("办公室电话")).send_keys("15089500015")

        elif selectelement.get_attribute("textContent") == "其他":
            Hidden_loc = (By.XPATH, "//div[contains(text(), '就业情况')]/parent::div/parent::span/following-sibling::span//input")
            Hidden = self.find_element(*Hidden_loc)
            Hidden.send_keys("Hidden")

        elif selectelement.get_attribute("textContent") == "退休" or selectelement.get_attribute("textContent") == "无业":
            pass

    def totalRevenue(self):
        self.find_element(*self.get_radio("客户全年总收入为(港元)")).click()
        self.find_element(*self.get_input("请注明资金来源", other=True)).send_keys("资金来源")

    def netEstate(self):
        self.find_element(*self.get_radio("客户资产净值(港元)")).click()
        self.find_element(*self.get_input("请注明资产净值", other=True)).send_keys("请注明资产净值")

    def source_of_wealth(self):
        self.find_element(*self.get_checkbox("就业薪金")).click()

    def securities(self):
        # 客户投资经验及曾买卖产品>证券
        securities = self.find_element(*self.get_input("证券"))
        # time.sleep(0.3)
        self.scrollinto(securities)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def CBBCcertificate(self):
        # 客户投资经验及曾买卖产品>牛熊证
        CBBCcertificate = self.find_element(*self.get_input("牛熊证"))
        # time.sleep(0.3)
        self.scrollinto(CBBCcertificate)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def derivativewarrant(self):
        # 客户投资经验及曾买卖产品>衍生权证
        derivativewarrant = self.find_element(*self.get_input("衍生权证(窝轮)"))
        # time.sleep(0.3)
        self.scrollinto(derivativewarrant)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def futures(self):
        # 客户投资经验及曾买卖产品>期货
        futures = self.find_element(*self.get_input("期货"))
        # time.sleep(0.3)
        self.scrollinto(futures)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def Option(self):
        # 客户投资经验及曾买卖产品>期权
        Option = self.find_element(*self.get_input("期权"))
        # time.sleep(0.3)
        self.scrollinto(Option)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def foreignexchange(self):
        # 客户投资经验及曾买卖产品>外汇
        foreignexchange = self.find_element(*self.get_input("外汇"))
        # time.sleep(0.3)
        self.scrollinto(foreignexchange)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def otherInvest(self):
        # 客户投资经验及曾买卖产品>其他投资
        self.find_element(*self.get_input("其他投资")).send_keys("otherInvest")
        # self.get_action("其他投资")
        # time.sleep(5)
        # other_loc = (By.XPATH, "//div[contains(text(), '其他投资')]/parent::*/parent::span/following-sibling::*//input")
        # self.find_element(other_loc).click()
        # self.find_element(*self.get_select()).click()

    def derivativeCourse(self):
        # 客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程
        derivativeCourse = self.find_element(*self.get_derivativeInput("相关课程"))
        # time.sleep(0.3)
        self.scrollinto(derivativeCourse)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def derivativeJobs(self):
        # 客户是否从现时或过去拥有与衍生产品有关的工作经验?
        derivativeJobs = self.find_element(*self.get_derivativeInput("工作经验"))
        # time.sleep(0.3)
        self.scrollinto(derivativeJobs)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def tradingFund(self):
        # 客户是否于过去3年曾执行 5次或以上有关衍生产品的交易
        tradingFund = self.find_element(*self.get_derivativeInput("买卖基金"))
        self.scrollinto(tradingFund)
        # time.sleep(0.5)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def buyProduct(self):
        # 客户是否申请开通买卖衍生权证、牛熊证及结构性等产品
        buyProduct = self.find_element(*self.get_derivativeInput("买卖衍生"))
        # time.sleep(0.3)
        self.scrollinto(buyProduct)
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def bankrupt(self):
        bankrupt = self.find_element(*self.get_input("申请破产"))
        # time.sleep(0.3)
        self.scrollinto(bankrupt)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def customerRelatives(self):
        customerRelatives = self.find_element(*self.get_input("艾德证券的雇员", other=True))
        # time.sleep(0.3)
        self.scrollinto(customerRelatives)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def associatedcustomer(self):
        associatedcustomer = self.find_element(*self.get_input("艾德证券客户有关连", other=True))
        # time.sleep(0.3)
        self.scrollinto(associatedcustomer)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def director(self):
        director = self.find_element(*self.get_input("认可人士?", other=True))
        # time.sleep(0.3)
        self.scrollinto(director)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def citizenOfUSA(self):
        citizenOfUSA = self.find_element(*self.get_input("美国公民", other=True))
        # time.sleep(0.3)
        self.scrollinto(citizenOfUSA)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def americanResident(self):
        americanResident = self.find_element(*self.get_input("美国居民", other=True))
        # time.sleep(0.3)
        self.scrollinto(americanResident)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def PEP_People(self):
        PEP_People = self.find_element(*self.get_input("政治公众人物（PEP）", other=True))
        # time.sleep(0.3)
        self.scrollinto(PEP_People)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def investmentTarget(self):
        investmentTarget = self.find_element(*self.get_input("投资目标", other=True))
        self.scrollinto(investmentTarget)
        # time.sleep(0.3)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def riskTolerance(self):
        riskTolerance = self.find_element(*self.get_input("风险承受能力", other=True))
        # time.sleep(0.3)
        self.scrollinto(riskTolerance)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def currency(self):
        currency = self.find_element(*self.get_input("货币", other=True))
        # time.sleep(0.3)
        self.scrollinto(currency)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def bankAccount(self):
        bankAccount_loc = (By.XPATH, "//span[contains(text(), '删除')]/parent::*/parent::*/preceding-sibling::div//input")
        bankAccount = self.find_elements(*bankAccount_loc)
        for bankInput in bankAccount:
            bankInput.send_keys("bankAccount")


    def marginAccount(self):
        marginAccount = self.find_element(*self.get_input("客户的配偶", other=True))
        # time.sleep(0.3)
        self.scrollinto(marginAccount)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def discretion(self):
        discretion = self.find_element(*self.get_input("客户及/或其配偶", other=True))
        # time.sleep(0.3)
        self.scrollinto(discretion)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def companyAccounts(self):
        companyAccounts = self.find_element(*self.get_input("同一集团公司旗下", other=True))
        # time.sleep(0.3)
        self.scrollinto(companyAccounts)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")


    def channel(self):
        channel_loc = (By.XPATH, "//div[contains(text(), '您透过哪些渠道认识艾德证券')]/parent::div/following-sibling::div//label")
        channel = self.find_elements(*channel_loc)
        for i in range(len(channel)):
            if i != len(channel)-1:
                channel[i].click()

    def beneficial(self):
        beneficial = self.find_element(*self.get_input("是否账户的最终实益拥有人", other=True))
        # time.sleep(0.3)
        self.scrollinto(beneficial)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

        # self.find_element(*self.get_input("最终实益拥有人名称为", other=True)).send_keys("beneficial")

    def Othed_People(self):
        othedPeople = self.find_element(*self.get_input("负责下单", other=True))
        # time.sleep(0.3)
        self.scrollinto(othedPeople)
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")


    def jurisdiction(self):
        self.find_element(*self.get_checkbox("香港身份证号码")).click()


    def acceptStatement(self):
        self.find_element(*self.get_input("本人接受上述声明")).click()
        # self.find_element(*self.get_select()).click()
        selectelement = self.get_select()
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")

    def useStatement(self):
        self.find_element(*self.get_input("个人资料之使用声明")).click()
        # self.find_element(*self.get_select(top=True)).click()
        selectelement = self.get_select(top=True)
        print(selectelement.get_attribute("textContent"))
        return selectelement.get_attribute("textContent")


    def click_sublime(self):
        sublime_loc = (By.CLASS_NAME, "button-1")
        sublime = self.find_element(*sublime_loc).click()






