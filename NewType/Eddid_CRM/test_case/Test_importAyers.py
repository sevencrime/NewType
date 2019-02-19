#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-16 16:36:44
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import unittest
from selenium import webdriver
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from PageElement.LoginPage import *
from PageElement.ApplyListPage import *
from PageElement.AccountlistPage import *
from Commons import Logging

#交易账户列表导入Ayers数据
class importAyers(unittest.TestCase):

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

    def test_importAyers(self):
        applylistpage = ApplyListPage(self.driver, self.url, "Eddid")
        #点击账户管理
        applylistpage.click_account_manager()
        # 点击交易账户
        applylistpage.click_accountlist()

        # 实例化AccountlistPage
        accountpage = AccountlistPage(self.driver, self.url, "Eddid")
        # 等待CSS加载完成
        accountpage.wait_LoadingModal()
        # 点击导入Ayers按钮
        accountpage.click_importAyers()
        # 点击导入主要信息
        # accountpage.click_importmain()
        
        accountpage.uploadAyers()
        print(accountpage.uploadAyers.get_attribute__('value'))

        

if __name__ == '__main__':
    # print(os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xls')
    unittest.main()
