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

class ApplyPage(BasePage.BasePage):
    # log = Logging.Logs()

    # applicationFor_loc = (By.XPATH, "//div[contains(text(), '账户类型')]/following-sibling::span/div")
    # checkbox_loc = (By.XPATH, "//span[contains(text(), '香港及环球证券账户(现金)')]/preceding-sibling::span")

    def get_input(self, text):
    	applicationFor_loc = (By.XPATH, "//div[contains(text(), '%s')]/following-sibling::span/div" %text)
    	return applicationFor_loc

    def get_checkbox(self, text):
    	checkbox_loc = (By.XPATH, "//span[contains(text(), '%s')]/preceding-sibling::span" %text)
    	return checkbox_loc

    def get_select(self, text):
    	select_loc = (By.XPATH, "//span[contains(text(), '%s')]" %text)
    	return select_loc

    # 账户类型
    def send_applicationFor(self):
    	self.find_element(*self.get_input('账户类型')).click()
    	self.find_element(*self.get_select('个人账户')).click()

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



