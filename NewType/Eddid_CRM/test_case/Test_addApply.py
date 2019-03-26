#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-03 13:56:31
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from PageElement.LoginPage import *
from PageElement.ApplyListPage import *
from PageElement.MainPage import *
from PageElement.ApplyPage import *
from Commons import Logging

class addApply(unittest.TestCase):

    def setUp(self):
        # self.log.info("正在执行Test_Login")

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        self.driver.implicitly_wait(30)
        self.url = 'http://eddid-bos-feature.ntdev.be'

        #在这里先登录
        login_page = LoginPage(self.driver, self.url, "Eddid")
        login_page.open()
        login_page.input_username("admin")
        login_page.input_password("abcd1234")
        login_page.click_submit()
        self.assertEqual("admin", login_page.show_userid(), "userid与登录账户不一致")

    def tearDown(self):
        time.sleep(10)
        print("结束driver")
        self.driver.quit()

    def test_addApply(self):
        applylistpage = ApplyListPage(self.driver, self.url, "Eddid")
        mainpage = MainPage(self.driver, self.url, "Eddid")
        applypage = ApplyPage(self.driver, self.url, "Eddid")

        #点击开户管理，判断
        applylistpage.click_apply_manager()
        #点击开户列表，判断
        applylistpage.click_applylist()
        #等待
        mainpage.wait_LoadingModal()
        #点击新增按钮
        mainpage.click_add()

        # applypage.send_applicationFor()
        # applypage.send_accountOpeningWay()
        # applypage.send_parentId()
        # applypage.send_mailLanguage()
        # applypage.send_accountType()
        # applypage.send_title()
        # applypage.send_firstName()
        # applypage.send_lastName()
        
        # mainpage.wait_LoadingModal()

        # applypage.send_chineseName()
        # applypage.send_emali()
        # applypage.send_phoneAreaCode()
        # applypage.send_phone()
        # applypage.send_address()
        # applypage.send_addressMail()
        # applypage.send_nationality()
        # applypage.send_idType()
        # applypage.send_idNumber()
        # applypage.send_countryIssue()
        # applypage.send_birthday()
        # applypage.send_birthPlace()

        applypage.employment()
        applypage.occupation()
        applypage.employedPeriod()
        applypage.employer()
        applypage.businessType()
        applypage.businessAddress()
        applypage.businessPhone()

        applypage.totalRevenue()
        applypage.netEstate()

if __name__ == '__main__':
    unittest.main()



