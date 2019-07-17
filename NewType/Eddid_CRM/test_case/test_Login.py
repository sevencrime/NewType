#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import unittest
import pytest
from selenium import webdriver
from Commons import Logging
from test_case.public.publicTool import publicTool


class Test_Login(unittest.TestCase):

    log = Logging.Logs()

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

    def test_login(self):
        publicTool.LoginCRM(self)

if __name__ == '__main__':
    unittest.main()


