#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from PageElement import *
from Commons import *
import unittest
from selenium import webdriver
from test_case.public import Decoration
import time
import pytest

class reviewProcess1(unittest.TestCase):
	# CRM and apply_form正向审核: 未处理--待cs2--待RO--待ops--success
	globals()["status"] = "未处理"
	@classmethod
	def setUpClass(self):
		self.email = "7296onedi35717@qq.com"

	# 所有case执行之后清理环境
	@classmethod
	def tearDownClass(self):
	    print("This tearDownClass() method only called once too.")

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.set_page_load_timeout(20)
		self.driver.set_script_timeout(20)
		self.url = 'http://eddid-bos-uat.ntdev.be'

		self.login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
		self.applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
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

	def loginCRM(self, user='admin', psw='abcd1234'):
		self.login_page.open()
		self.login_page.input_username(user)
		self.login_page.input_password(psw)
		self.login_page.click_submit()
		self.login_page.wait_LoadingModal()
		self.assertEqual(user, self.login_page.show_userid(), "userid与登录账户不一致")

	@skipIf(status = "未处理")
	def test1_Process1_salestocs2(self):
		# sales--cs2
		self.loginCRM(user='sales_t1')		#先登录

		self.applylistpage.click_apply_manager()		#点击开户管理
		self.applylistpage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		# 下拉列表选择未处理
		self.mainpage.click_StatusSelect("未处理")
		self.mainpage.wait_LoadingModal()

		# 判断状态校验功能是否正常,选择编号
		self.mainpage.click_checkbox(email=self.email)	
		self.mainpage.click_submitreview()
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertIsNot("待CS2审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)
	
	@skipIf(status = "CS2")
	def test2_Process1_cs2toro(self):
		# cs2 to ro
		self.loginCRM(user='cs_t1')		#先登录

		self.applylistpage.click_apply_manager()		#点击开户管理
		self.applylistpage.click_applylist()		    #点击开户列表
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
		# self.assertIsNot("待CS2审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "待证券RO审批")
	def test3_Process1_cliff(self):
		# cliff审核
		self.loginCRM(user='ro1_cliff', psw="Abcd1234")		#先登录

		self.applylistpage.click_apply_manager()		#点击开户管理
		self.applylistpage.click_applylist()		    #点击开户列表
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
		self.assertIsNot("待证券RO审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "待期货RO审批")
	def test4_Process1_don(self):
		# don审核
		self.loginCRM(user='ro1_don', psw='Abcd1234')		#先登录

		self.applylistpage.click_apply_manager()		#点击开户管理
		self.applylistpage.click_applylist()		    #点击开户列表
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
		self.assertIsNot("待期货RO审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "待外汇RO审批")
	def test5_Process1_aaron(self):
		# aaron审核
		self.loginCRM(user='aaron_chan')		#先登录

		self.applylistpage.click_apply_manager()		#点击开户管理
		self.applylistpage.click_applylist()		    #点击开户列表
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
		self.assertIsNot("待外汇RO审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "待黄金RO审批")
	def test6_Process1_gold(self):
		# gold 审核
		self.loginCRM(user='gold_onedi', psw="Abcd1234")		#先登录

		self.applylistpage.click_apply_manager()		#点击开户管理
		self.applylistpage.click_applylist()		    #点击开户列表
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
		self.assertIsNot("待黄金RO审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf(status = "结算")
	def test7_Process1_opstosuccess(self):
		# ro to ops
		self.loginCRM(user='ops_t1')		#先登录

		self.applylistpage.click_apply_manager()		#点击开户管理
		self.applylistpage.click_applylist()		    #点击开户列表
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
		self.assertEqual("成功", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)


if __name__ == "__main__":
	# pytest.main()
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess1))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)