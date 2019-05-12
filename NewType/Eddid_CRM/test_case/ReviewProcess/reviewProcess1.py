#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from PageElement import *
from Commons import *
import unittest
from selenium import webdriver

class reviewProcess1(unittest.TestCase):
	# CRM and apply_form正向审核: 未处理--待cs2--待RO--待ops--success

	def setUp(self):
		self.driver = webdriver.Chrome()
		# self.driver = webdriver.Firefox(executable_path = 'geckodriver')
		# self.driver.implicitly_wait(30)   
		self.driver.set_page_load_timeout(30)
		self.driver.set_script_timeout(30)
		self.url = 'http://eddid-bos-uat.ntdev.be'

	def tearDown(self):
		time.sleep(20)
		print("结束driver")
		self.driver.quit()

	def login(self, user='admin', psw='abcd1234'):
		login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
		login_page.open()
		login_page.input_username(user)
		login_page.input_password(psw)
		login_page.click_submit()
		login_page.wait_LoadingModal()
		self.assertEqual("admin", login_page.show_userid(), "userid与登录账户不一致")

	def test1_Process1_salestocs2(self):
		# sales--cs2
		self.login(user='sales_t1')		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		# 下拉列表选择未处理
		mainpage.click_StatusSelect("未处理")
		mainpage.wait_LoadingModal()

		# 判断状态校验功能是否正常,选择编号
		mainpage.click_checkbox(email="244563@qq.com")	
		mainpage.click_submit()


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess1))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)