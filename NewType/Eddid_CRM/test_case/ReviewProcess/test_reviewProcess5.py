#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import unittest
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
# sys.path.append(os.getcwd()+"\\NewType\\Eddid_CRM")
from selenium import webdriver
from test_case.Test_Login import *
from Commons import *
from PageElement import *
import pytest


class reviewProcess5(unittest.TestCase):
    # 多角色RO
    globals()["status"] = "待CS2审核"

    @classmethod
    def setUpClass(cls):
        self.email = "9706onedi882636@qq.com"

    # 所有case执行之后清理环境
    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once too.")

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Edge()
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        # self.driver.implicitly_wait(30)   
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.url = 'http://eddid-bos-uat.ntdev.be'

        self.MenuListPage = MenuListPage.MenuListPage(self.driver, self.url, "Eddid")
        self.mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
        self.applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

    def tearDown(self):
        # time.sleep(5)
        print("结束driver")
        self.driver.quit()

    def skipIf(status):
        def wrapper(func):
            def inner_wrapper(self):
                if globals()['status'].find(status) != -1:
                    return func(self)
                else:
                    print("状态不是 {}".format(status))
                    return 
            return inner_wrapper
        return wrapper

    # @unittest.skipIf(globals()["status"].find("未处理") != -1, "状态不是未处理")
    @skipIf("未处理")
    def test_a_Process5_aaron(self):
        # aaron 通过
        Test_Login.LoginCRM(self, user='aaron_test')      #先登录

        self.MenuListPage = self.MenuListPage.self.MenuListPage(self.driver, self.url, "Eddid")
        self.mainpage = self.mainpage.self.mainpage(self.driver, self.url, "Eddid")
        self.applypage = self.applypage.self.applypage(self.driver, self.url, "Eddid")

        self.MenuListPage.click_apply_manager()     #点击开户管理
        self.MenuListPage.click_applylist()         #点击开户列表
        self.mainpage.wait_LoadingModal()
        # import pdb; pdb.set_trace()
        # 下拉列表选择未处理
        self.mainpage.click_StatusSelect("待RO审批")
        self.mainpage.wait_LoadingModal()

        # 判断状态校验功能是否正常,选择编号
        self.mainpage.get_apply(email=self.email)   
        self.mainpage.wait_LoadingModal()
        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')
        self.applypage.click_sublimeApply("通过")
        self.applypage.click_popWindow("确定")
        self.mainpage.wait_LoadingModal()

        # self.assertIsNot("待CS2审批", self.mainpage.get_status(self.email), "状态没有改变")
        globals()["status"] = self.mainpage.get_status(self.email)

    # @unittest.skipIf(globals()["status"].find("未处理") != -1, "状态不是未处理")
    def test_b_Process5_roadmin(self):
        # 多角色通过
        Test_Login.LoginCRM(self, user='onedi.admin', psw="Abcd1234")      #先登录

        self.MenuListPage = self.MenuListPage.self.MenuListPage(self.driver, self.url, "Eddid")
        self.mainpage = self.mainpage.self.mainpage(self.driver, self.url, "Eddid")
        self.applypage = self.applypage.self.applypage(self.driver, self.url, "Eddid")

        self.MenuListPage.click_apply_manager()     #点击开户管理
        self.MenuListPage.click_applylist()         #点击开户列表
        self.mainpage.wait_LoadingModal()

        # 下拉列表选择未处理
        self.mainpage.click_StatusSelect("待RO审批")
        self.mainpage.wait_LoadingModal()
        # 判断状态校验功能是否正常,选择编号
        self.mainpage.get_apply(email=self.email)   
        self.mainpage.wait_LoadingModal()
        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

        self.applypage.click_sublimeApply("通过")
        self.applypage.click_popWindow("确定")
        self.mainpage.wait_LoadingModal()

        # self.assertIsNot("待CS2审批", self.mainpage.get_status(self.email), "状态没有改变")
        globals()["status"] = self.mainpage.get_status(self.email)
        


if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess5))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    pytest.main(['-k', "test_reviewProcess5"])