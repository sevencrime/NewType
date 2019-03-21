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
import time
from selenium.webdriver.common.keys import Keys

class ApplyPage(BasePage.BasePage):
    # log = Logging.Logs()

    # applicationFor_loc = (By.XPATH, "//div[contains(text(), '账户类型')]/following-sibling::span/div")
    # checkbox_loc = (By.XPATH, "//span[contains(text(), '香港及环球证券账户(现金)')]/preceding-sibling::span")

    def get_input(self, text):
    	applicationFor_loc = (By.XPATH, "//div[contains(text(), '%s')]/following-sibling::span//input" %text)
    	return applicationFor_loc

    def get_checkbox(self, text):
    	checkbox_loc = (By.XPATH, "//span[contains(text(), '%s')]/preceding-sibling::span" %text)
    	return checkbox_loc

    def get_select(self, text):
    	select_loc = (By.XPATH, "//span[contains(text(), '%s')]" %text)
    	return select_loc

    def del_readonly(self, loc):
        self.script('arguments[0].removeAttribute(\"readonly\")', loc);


    # 账户类型
    def send_applicationFor(self):
    	self.find_element(*self.get_input('账户类型')).click()
    	self.find_element(*self.get_select('联名账户')).click()

    # 开户方法
    def send_accountOpeningWay(self):
        self.find_element(*self.get_input('开户方法')).click()
        self.find_element(*self.get_select('亲临开户')).click()

    # 负责人
    def send_parentId(self):
        self.find_element(*self.get_input('负责人')).click()
        self.find_element(*self.get_select('sales_t1')).click()

    # 邮件语言
    def send_mailLanguage(self):
        self.find_element(*self.get_input('邮件语言')).click()
        self.find_element(*self.get_select('中文(简体)')).click()


    def send_accountType(self):
        self.find_element(*self.get_checkbox('香港及环球证券账户(现金)')).click()

    def send_title(self):
        self.find_element(*self.get_input('称谓')).click()
        self.find_element(*self.get_select("先生")).click()

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
        self.del_readonly(phoneAreaCode)
        phoneAreaCode.send_keys("中华人民共和国 +86")
        phoneAreaCode.send_keys(Keys.ENTER)

    def send_phone(self):
        self.find_element(*self.get_input("电话号码(用于通讯)")).send_keys("15089510001")

    def send_address(self):
        self.find_element(*self.get_input("住宅地址(不接受邮政信箱)")).send_keys("桑达科技大厦802")

    def send_addressMail(self):
        self.find_element(*self.get_input("邮寄地址(如与住宅地址不同)")).send_keys("桑达科技大厦802")

    def send_nationality(self):
        nationality = self.find_element(*self.get_input("国籍"))
        # self.find_element(*self.get_select("中华人民共和国")).click()
        # self.find_elements((By.XPATH, "//span[contains(text(), '中华人民共和国')]"))
        self.del_readonly(nationality)
        nationality.send_keys("中华人民共和国")
        nationality.send_keys(Keys.ENTER)

    def send_idType(self):
        self.find_element(*self.get_input("身份证件类型")).click()
        self.find_element(*self.get_select("内地身份证")).click()

    def send_idNumber(self):
        self.find_element(*self.get_input("身份证或护照号码")).send_keys("44150266621212")

    def send_countryIssue(self):
        countryIssue = self.find_element(*self.get_input("签发国家"))

    def send_birthday(self):
        self.find_element(*self.get_input("出生日期(日/月/年)")).send_keys("21/01/2000")
        self.find_element(*self.get_input("出生日期(日/月/年)")).send_keys(Keys.ENTER)

    def send_birthPlace(self):
        birthPlace = self.find_element(*self.get_input('出生地方'))
        self.del_readonly(birthPlace)
        birthPlace.send_keys("中华人民共和国")
        birthPlace.send_keys(Keys.ENTER)
















