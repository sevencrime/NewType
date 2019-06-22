#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from PageElement import *
from Commons import *
from test_case.Test_Login import *
import unittest
from selenium import webdriver
import time
import pytest

class ReviewProcessTool(unittest.TestCase):
	# CRM and apply_form正向审核: 未处理--待cs2--待RO--待ops--success

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.set_page_load_timeout(20)
		self.driver.set_script_timeout(20)
		self.url = 'http://eddid-bos-uat.ntdev.be'

		# self.login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
		self.MenuListPage = MenuListPage.MenuListPage(self.driver, self.url, "Eddid")
		self.mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		self.applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

	def tearDown(self):
		# time.sleep(5)
		print("结束driver")
		self.driver.quit()

	# def skipIf(status):
	# 	# 装饰器, 用于判断用例是否执行
	# 	def wrapper(func):
	# 		def inner_wrapper(self):
	# 			if globals()['status'].find(status) != -1:
	# 				return func(self)
	# 			else:
	# 				print("状态不是 {}".format(status))
	# 				return 
	# 		return inner_wrapper
	# 	return wrapper


