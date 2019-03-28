#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-14 21:30:24
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import BasePage, Logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

class ApplyPage(BasePage.BasePage):
    # log = Logging.Logs()

    # applicationFor_loc = (By.XPATH, "//div[contains(text(), '账户类型')]/following-sibling::span/div")
    # checkbox_loc = (By.XPATH, "//span[contains(text(), '香港及环球证券账户(现金)')]/preceding-sibling::span")

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
            # print("if not", text)
            if top:
                select_loc = (By.XPATH, "//div[@x-placement = 'top-start']//li[2]")
            else:
                select_loc = (By.XPATH, "//div[@x-placement = 'bottom-start']//li[2]")

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
        time.sleep(5)
        ActionChains(self.driver).click(self.find_element(*others_loc)).perform()

    def scrollinto(self, loc):
        self.script("arguments[0].scrollIntoView();", loc)
        loc.click()


    # 账户类型
    def send_applicationFor(self):
        self.find_element(*self.get_input('账户类型')).click()
        time.sleep(5)
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
        self.find_element(*self.get_select()).click()

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
        self.find_element(*self.get_select()).click()

    def send_idType(self):
        self.find_element(*self.get_input("身份证件类型")).click()
        self.find_element(*self.get_select(text="内地身份证")).click()

    def send_idNumber(self):
        self.find_element(*self.get_input("身份证或护照号码")).send_keys("44150266621212")

    def send_countryIssue(self):
        countryIssue = self.find_element(*self.get_input("签发国家"))
        self.scrollinto(countryIssue)
        self.find_element(*self.get_select()).click()

    def send_birthday(self):
        self.find_element(*self.get_input("出生日期(日/月/年)")).send_keys("21/01/2000")
        self.find_element(*self.get_input("出生日期(日/月/年)")).send_keys(Keys.ENTER)

    def send_birthPlace(self):
        birthPlace = self.find_element(*self.get_input('出生地点'))
        self.scrollinto(birthPlace)
        self.find_element(*self.get_select()).click()

    def employment(self):
        employment = self.find_element(*self.get_input("就业情况"))
        time.sleep(1)
        self.scrollinto(employment)
        self.find_element(*self.get_select()).click()

    def occupation(self):
        self.find_element(*self.get_input("职位")).send_keys("销售")

    def employedPeriod(self):
        self.find_element(*self.get_input("受雇年期")).send_keys("十年以上")

    def employer(self):
        self.find_element(*self.get_input("目前雇主名称")).send_keys("newtype")

    def businessType(self):
        self.find_element(*self.get_input("业务性质")).send_keys("互联网")

    def businessAddress(self):
        self.find_element(*self.get_input("办公室地址")).send_keys("广东省深圳市南山区桑达科技大厦802")

    def businessPhone(self):
        self.find_element(*self.get_input("办公室电话")).send_keys("15089500015")

    def totalRevenue(self):
        self.find_element(*self.get_radio("客户全年总收入为(港元)")).click()

    def netEstate(self):
        self.find_element(*self.get_radio("客户资产净值(港元)")).click()

    def source_of_wealth(self):
        self.find_element(*self.get_checkbox("就业薪金")).click()

    def securities(self):
        securities = self.find_element(*self.get_input("证券"))
        self.scrollinto(securities)
        self.find_element(*self.get_select()).click()

    def CBBCcertificate(self):
        CBBCcertificate = self.find_element(*self.get_input("牛熊证"))
        time.sleep(0.3)
        self.scrollinto(CBBCcertificate)
        self.find_element(*self.get_select()).click()

    def derivativewarrant(self):
        derivativewarrant = self.find_element(*self.get_input("衍生权证(窝轮)"))
        time.sleep(0.3)
        self.scrollinto(derivativewarrant)
        self.find_element(*self.get_select()).click()

    def futures(self):
        futures = self.find_element(*self.get_input("期货"))
        time.sleep(0.3)
        self.scrollinto(futures)
        self.find_element(*self.get_select()).click()

    def Option(self):
        Option = self.find_element(*self.get_input("期权"))
        time.sleep(0.3)
        self.scrollinto(Option)
        self.find_element(*self.get_select()).click()

    def foreignexchange(self):
        foreignexchange = self.find_element(*self.get_input("外汇"))
        time.sleep(0.3)
        self.scrollinto(foreignexchange)
        self.find_element(*self.get_select()).click()

    def otherInvest(self):
        self.find_element(*self.get_input("其他投资")).send_keys("otherInvest")
        # self.get_action("其他投资")
        # time.sleep(5)
        # other_loc = (By.XPATH, "//div[contains(text(), '其他投资')]/parent::*/parent::span/following-sibling::*//input")
        # self.find_element(other_loc).click()
        # self.find_element(*self.get_select()).click()

    def derivativeCourse(self):
        derivativeCourse = self.find_element(*self.get_derivativeInput("相关课程"))
        self.scrollinto(derivativeCourse)
        self.find_element(*self.get_select()).click()

    def derivativeJobs(self):
        derivativeJobs = self.find_element(*self.get_derivativeInput("工作经验"))
        # time.sleep(0.3)
        self.scrollinto(derivativeJobs)
        self.find_element(*self.get_select()).click()

    def tradingFund(self):
        tradingFund = self.find_element(*self.get_derivativeInput("买卖基金"))
        # time.sleep(0.3)
        self.scrollinto(tradingFund)
        self.find_element(*self.get_select()).click()

    def buyProduct(self):
        buyProduct = self.find_element(*self.get_derivativeInput("买卖衍生"))
        # time.sleep(0.3)
        self.scrollinto(buyProduct)
        self.find_element(*self.get_select()).click()

    def bankrupt(self):
        bankrupt = self.find_element(*self.get_input("申请破产"))
        # time.sleep(0.5)
        self.scrollinto(bankrupt)
        self.find_element(*self.get_select()).click()

    def customerRelatives(self):
        customerRelatives = self.find_element(*self.get_input("艾德证券的雇员", other=True))
        time.sleep(0.5)
        self.scrollinto(customerRelatives)
        self.find_element(*self.get_select()).click()

    def associatedcustomer(self):
        associatedcustomer = self.find_element(*self.get_input("艾德证券客户有关连", other=True))
        time.sleep(0.5)
        self.scrollinto(associatedcustomer)
        self.find_element(*self.get_select()).click()

    def director(self):
        director = self.find_element(*self.get_input("认可人士?", other=True))
        time.sleep(0.5)
        self.scrollinto(director)
        self.find_element(*self.get_select()).click()

    def citizenOfUSA(self):
        citizenOfUSA = self.find_element(*self.get_input("美国公民", other=True))
        time.sleep(0.5)
        self.scrollinto(citizenOfUSA)
        self.find_element(*self.get_select()).click()

    def americanResident(self):
        americanResident = self.find_element(*self.get_input("美国居民", other=True))
        time.sleep(0.5)
        self.scrollinto(americanResident)
        self.find_element(*self.get_select()).click()

    def PEP_People(self):
        PEP_People = self.find_element(*self.get_input("政治公众人物（PEP）", other=True))
        time.sleep(0.5)
        self.scrollinto(PEP_People)
        self.find_element(*self.get_select()).click()

    def investmentTarget(self):
        investmentTarget = self.find_element(*self.get_input("投资目标", other=True))
        self.scrollinto(investmentTarget)
        time.sleep(0.5)
        self.find_element(*self.get_select()).click()

    def riskTolerance(self):
        riskTolerance = self.find_element(*self.get_input("风险承受能力", other=True))
        time.sleep(0.5)
        self.scrollinto(riskTolerance)
        self.find_element(*self.get_select()).click()








