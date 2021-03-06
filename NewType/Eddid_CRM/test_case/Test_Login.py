#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("Eddid_CRM\\")+len("Eddid_CRM\\")]
sys.path.append(rootPath)
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageElement import *
from Commons import *

class Test_Login(unittest.TestCase):

    # log = Logging.Logs()

    def setUp(self):
        # self.log.info("正在执行Test_Login")
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        self.url = 'http://eddid-bos-uat.ntdev.be'

    def tearDown(self):
        time.sleep(5)
        print("结束driver")
        self.driver.quit()

    def LoginCRM(self, user='admin', psw='abcd1234'):

        # self.log.info("实例化LoginPage")
        login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
        # 打开浏览器
        # self.log.info("打开浏览器")
        login_page.open()
        # 输入用户名密码
        # self.log.info("输入用户名密码")
        login_page.input_username(user)
        login_page.input_password(psw)
        # 点击登录
        # self.log.info("点击登录")
        login_page.click_submit()
        login_page.wait_LoadingModal()
        # 断言userid
        # self.log.info("断言userid")
        # self.assertEqual(user, login_page.show_userid(), "userid与登录账户不一致")
        assert user in login_page.show_userid(), "userid与登录账户不一致"

    def test_login(self):
        self.LoginCRM()


if __name__ == '__main__':
    unittest.main()


