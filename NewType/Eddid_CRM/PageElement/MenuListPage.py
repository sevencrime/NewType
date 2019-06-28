#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 15:46:03
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

#CRM侧边栏

import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import *
from selenium.webdriver.common.by import By


class MenuListPage(BasePage.BasePage):

    apply_manager = (By.XPATH, "//span[contains(text(),'开户管理')]")     #通过<i>标签定位
    applylist = (By.LINK_TEXT, "开户列表")

    account_manager = (By.XPATH, "//span[contains(text(),'账户管理')]")  #通过<i>标签定位
    accountlist = (By.LINK_TEXT, "交易账户")
    bankSubAccount = (By.LINK_TEXT, "银行子账户")

    client_manager = (By.XPATH, "//span[contains(text(),'客户管理')]")
    clientlist = (By.LINK_TEXT, "客户名单")
    client_reviewlist = (By.LINK_TEXT, "审核列表")
    client_transferlist = (By.LINK_TEXT, "客户转移")

    activity_manager = (By.XPATH, "//span[contains(text(),'活动管理')]")
    activitylist = (By.LINK_TEXT, "活动列表")
    create_seminar = (By.LINK_TEXT, "创建讲座")
    activity_record = (By.LINK_TEXT, "活动记录列表")

    def click_menulist(self, ul_text, li_text):
        
        manager_loc = (By.XPATH, "//span[contains(text(),'{}')]".format(ul_text))
        self.find_element(*manager_loc).click()     #点击主菜单
        if li_text == "开户列表":
            el_open_loc = (By.XPATH, "//a/div[contains(text(), '开户列表')]")
            self.find_element(*el_open_loc).click()
        else:
            # 子菜单
            linkmenu_loc = (By.LINK_TEXT, "{}".format(li_text))
            self.find_element(*linkmenu_loc).click()    #点击子菜单


    def click_apply_manager(self):
        self.find_element(*self.apply_manager).click()

    def click_applylist(self):
        self.find_element(*self.applylist).click()

    def click_account_manager(self):
        self.find_element(*self.account_manager).click()

    def click_accountlist(self):
        self.find_element(*self.accountlist).click()

    def click_bankSubAccount(self):
        self.find_element(*self.bankSubAccount).click()

    def click_client_manager(self):
        self.find_element(*self.client_manager).click()

    def click_clientlist(self):
        self.find_element(*self.clientlist).click()

    def click_client_reviewlist(self):
        self.find_element(*self.client_reviewlist).click()

    def click_review_list(self):
        self.find_element(*self.review_list).click()

    def click_client_transferlist(self):
        self.find_element(*self.client_transferlist).click()

    def click_activity_manager(self):
        self.find_element(*self.activity_manager).click()

    def click_activitylist(self):
        self.find_element(*self.activitylist).click()

    def click_create_seminar(self):
        self.find_element(*self.create_seminar).click()

    def click_activity_record(self):
        self.find_element(*self.activity_record).click()



