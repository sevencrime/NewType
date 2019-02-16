#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 15:46:03
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import BasePage, Logging
from selenium.webdriver.common.by import By

class ApplyListPage(BasePage.BasePage):

    open_account_manager = (By.XPATH, "//span[contains(text(),'开户管理')]")     #通过<i>标签定位
    open_account_list = (By.LINK_TEXT, "开户列表")

    account_manager = (By.XPATH, "//span[contains(text(),'账户管理')]")  #通过<i>标签定位
    transaction_account = (By.LINK_TEXT, "交易账户")
    bank_sub_account = (By.LINK_TEXT, "银行子账户")

    client_manager = (By.XPATH, "//span[contains(text(),'客户管理')]")
    client_list = (By.LINK_TEXT, "客户名单")
    review_list = (By.LINK_TEXT, "审核列表")
    client_transfer = (By.LINK_TEXT, "客户转移")

    activity_manager = (By.XPATH, "//span[contains(text(),'活动管理')]")
    activity_list = (By.LINK_TEXT, "活动列表")
    create_lecture = (By.LINK_TEXT, "创建讲座")
    activity_record_list = (By.LINK_TEXT, "活动记录列表")


    def open(self):
        self._open(self.base_url, self.pagetitle)

    def click_open_account_manager(self):
        self.find_element(*self.open_account_manager).click()

    def click_open_account_list(self):
        self.find_element(*self.open_account_list).click()

    def click_account_manager(self):
        self.find_element(*self.account_manager).click()

    def click_transaction_account(self):
        self.find_element(*self.transaction_account).click()

    def click_bank_sub_account(self):
        self.find_element(*self.bank_sub_account).click()

    def click_client_manager(self):
        self.find_element(*self.client_manager).click()

    def click_client_list(self):
        self.find_element(*self.client_list).click()

    def click_review_list(self):
        self.find_element(*self.review_list).click()

    def click_review_list(self):
        self.find_element(*self.review_list).click()

    def click_client_transfer(self):
        self.find_element(*self.client_transfer).click()

    def click_activity_manager(self):
        self.find_element(*self.activity_manager).click()

    def click_activity_list(self):
        self.find_element(*self.activity_list).click()

    def click_create_lecture(self):
        self.find_element(*self.create_lecture).click()

    def click_activity_record_list(self):
        self.find_element(*self.activity_record_list).click()



