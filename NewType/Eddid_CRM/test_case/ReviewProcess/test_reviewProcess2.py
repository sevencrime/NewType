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
from test_case import *


class reviewProcess2(unittest.TestCase):
	# App来源正向审核: 待cs1--待cs2--待RO--待ops--success`
	globals()["status"] = "待CS1审核"

	@classmethod
	def setUpClass(self):
		self.email = "8576onedi1521332@qq.com"

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

	@skipIf(status = "CS1")
	def test1_Process2_cs1tocs2(self):
		# CS1---CS2
		Test_Login.LoginCRM(user='cs1_onedi', psw="Abcd1234")

		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect("待CS1审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("通过")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()


		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待CS2审批", self.mainpage.get_status(self.email), "状态没有改变")
		# status = self.mainpage.get_status(self.email)
		globals()["status"] = self.mainpage.get_status(self.email)
		# import pdb; pdb.set_trace()
		
	@skipIf(status = "CS2")
	def test2_Process2_cs2toro(self):
		# cs2 to ro
		Test_Login.LoginCRM(user='cs_t1')

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect("待CS2审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("通过")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertNotIn("CS2", self.mainpage.get_status(self.email), "状态错误")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "待证券RO审批")
	def test3_Process2_cliff(self):
		# cliff审核
		Test_Login.LoginCRM(user='ro1_cliff', psw="Abcd1234")

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待RO审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("通过")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待证券RO审批", self.mainpage.get_status(self.email), "cliff审核不通过")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "待期货RO审批")
	def test4_Process2_don(self):
		# don审核
		Test_Login.LoginCRM(user='ro1_don', psw='Abcd1234')

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待RO审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("通过")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待期货RO审批", self.mainpage.get_status(self.email), "don审核不通过")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "待外汇RO审批")
	def test5_Process2_aaron(self):
		# aaron审核
		Test_Login.LoginCRM(user='aaron_chan')

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待RO审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("通过")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待外汇RO审批", self.mainpage.get_status(self.email), "aaron审核不通过")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "待黄金RO审批")
	def test6_Process2_gold(self):
		# gold 审核
		Test_Login.LoginCRM(self.loginCRM(user='gold_onedi', psw="Abcd1234"))

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待RO审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("通过")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待黄金RO审批", self.mainpage.get_status(self.email), "gold审核不通过")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "结算")
	def test7_Process2_opstosuccess(self):
		# ro to ops
		Test_Login.LoginCRM(user='ops_t1')

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待结算审批")
		self.mainpage.wait_LoadingModal()

		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("完成")
		self.applypage.send_accountNumber(randox=1)
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertEqual(self.mainpage.get_status(self.email), '成功', "ops审核有误")
		globals()["status"] = self.mainpage.get_status(self.email)


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess2))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
