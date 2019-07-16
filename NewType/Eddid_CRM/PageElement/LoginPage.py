#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-14 17:22:57
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

# login 登录页面元素
import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage.BasePage):

    # log = Logging.Logs()

    username_loc = (By.XPATH, "//input[@placeholder='用户名']")
    password_loc = (By.XPATH, "//input[@placeholder='密码']")
    btn_login_loc = (By.XPATH, "//button")
    userid_loc = (By.CSS_SELECTOR, ".el-dropdown-link.el-dropdown-selfdefine ")
    # LoadingModal_loc = (By.CSS_SELECTOR, ".Loading-modal")

    # def wait_LoadingModal(self):
    #     WebDriverWait(self.driver, 20).until_not(
    #         EC.presence_of_element_located(self.LoadingModal_loc))

    def input_username(self, username):
        # self.log.info(sys._getframe().f_code.co_name)
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        # self.log.info(sys._getframe().f_code.co_name)
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        # self.log.info(sys._getframe().f_code.co_name)
        self.find_element(*self.btn_login_loc).click()

    def show_userid(self):
        # self.log.info(sys._getframe().f_code.co_name)
        return self.find_element(*self.userid_loc).text
