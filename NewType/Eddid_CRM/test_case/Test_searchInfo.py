#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 18:17:27
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$


import os,sys,time
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageElement import *
from Commons import *

class searchInfo(unittest.TestCase):

    # log = Logging.Logs()

    def setUp(self):
        # self.log.info("正在执行Test_Login")

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        # self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.url = 'http://eddid-bos-feature.ntdev.be'

        #在这里先登录
        login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
        login_page.open()
        login_page.input_username("admin")
        login_page.input_password("abcd1234")
        login_page.click_submit()
        self.assertEqual("admin", login_page.show_userid(), "userid与登录账户不一致")

    def tearDown(self):
        time.sleep(10)
        print("结束driver")
        self.driver.quit()

    def test_searchInfo(self):
        applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
        mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")

        #点击开户管理，判断
        applylistpage.click_apply_manager()
        #点击开户列表，判断
        applylistpage.click_applylist()

        #等待CSS.Loading-Modal加载完成
        mainpage.wait_LoadingModal()
        #点击下拉
        mainpage.click_StatusSelect()

        #选择下拉内容
        # mainpage.click_StatusOption()
        op = self.driver.find_elements_by_css_selector('.el-select-dropdown.el-popper')
        self.driver.execute_script('arguments[0].style.display="block";', op[2])
        self.log.info(op[2].text)
        op[2].click()



if __name__ == '__main__':
    unittest.main()



