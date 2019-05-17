#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import unittest
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
# sys.path.append(os.getcwd()+"\\NewType\\Eddid_CRM")
from selenium import webdriver
from Commons import *
from PageElement import *


class reviewProcess3(unittest.TestCase):
	# App来源驳回流程: 待cs1--拒绝
	globals()["status"] = "待CS1审核"

	@classmethod
	def setUpClass(self):
		self.email = "6152onedi860057@qq.com"

	# 所有case执行之后清理环境
	@classmethod
	def tearDownClass(self):
	    print("This tearDownClass() method only called once too.")

	def setUp(self):
		self.driver = webdriver.Chrome()
		# self.driver = webdriver.Edge()
		# self.driver = webdriver.Firefox(executable_path = 'geckodriver')
		# self.driver.implicitly_wait(30)   
		self.driver.set_page_load_timeout(30)
		self.driver.set_script_timeout(30)
		self.url = 'http://eddid-bos-uat.ntdev.be'

	def tearDown(self):
		# time.sleep(5)
		print("结束driver")
		self.driver.quit()

	def loginCRM(self, user='admin', psw='abcd1234'):
		login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
		login_page.open()
		login_page.input_username(user)
		login_page.input_password(psw)
		login_page.click_submit()
		login_page.wait_LoadingModal()
		self.assertEqual(user, login_page.show_userid(), "userid与登录账户不一致")

	@unittest.skipUnless(globals()["status"].find("CS1") != -1, "状态不是未处理")
	def test1_Process3_cs1torefuse(self):
		# CS1---Refuse
		self.loginCRM(user='cs1_onedi', psw="Abcd1234")		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		# 下拉列表选择待CS2审批
		mainpage.click_StatusSelect("待CS1审批")
		mainpage.wait_LoadingModal()

		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("拒绝")
		# 选择拒绝原因
		applypage.rejectReason("确定")
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("拒绝", mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = mainpage.get_status(self.email)
		


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess3))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
