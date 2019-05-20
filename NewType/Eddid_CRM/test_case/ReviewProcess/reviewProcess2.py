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

	# @unittest.skipUnless(globals()["status"].find("CS1") != -1, "状态不是CS1")
	def test1_Process2_cs1tocs2(self):
		# CS1---CS2
		self.loginCRM(user='cs1_onedi', psw="Abcd1234")		#先登录

		# import pdb; pdb.set_trace()
		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		# 下拉列表选择待CS2审批
		mainpage.click_StatusSelect("待CS1审批")
		mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		applypage.click_popWindow("确定")
		mainpage.wait_LoadingModal()


		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待CS2审批", mainpage.get_status(self.email), "状态没有改变")
		# status = mainpage.get_status(self.email)
		globals()["status"] = mainpage.get_status(self.email)
		# import pdb; pdb.set_trace()
		

	# @unittest.skipUnless(globals()["status"].find("CS2") != -1, "状态不是待CS2审核")
	def test2_Process2_cs2toro(self):
		# cs2 to ro
		self.loginCRM(user='cs_t1')		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		# 下拉列表选择待CS2审批
		mainpage.click_StatusSelect("待CS2审批")
		mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		applypage.click_popWindow("确定")
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertNotIn("CS2", mainpage.get_status(self.email), "状态错误")
		globals()["status"] = mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("待证券RO审批") != -1, "状态不是待证券RO审批")
	def test3_Process2_cliff(self):
		# cliff审核
		self.loginCRM(user='ro1_cliff', psw="Abcd1234")		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		mainpage.click_StatusSelect("待RO审批")
		mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		applypage.click_popWindow("确定")
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待证券RO审批", mainpage.get_status(self.email), "cliff审核不通过")
		globals()["status"] = mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("待期货RO审批") != -1, "状态不是待期货RO审批")
	def test4_Process2_don(self):
		# don审核
		self.loginCRM(user='ro1_don', psw='Abcd1234')		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		mainpage.click_StatusSelect("待RO审批")
		mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		applypage.click_popWindow("确定")
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待期货RO审批", mainpage.get_status(self.email), "don审核不通过")
		globals()["status"] = mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("待外汇RO审批") != -1, "状态不是待外汇RO审批")
	def test5_Process2_aaron(self):
		# aaron审核
		self.loginCRM(user='aaron_chan')		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		mainpage.click_StatusSelect("待RO审批")
		mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		applypage.click_popWindow("确定")
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待外汇RO审批", mainpage.get_status(self.email), "aaron审核不通过")
		globals()["status"] = mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("待黄金RO审批") != -1, "状态不是待黄金RO审批")
	def test6_Process2_gold(self):
		# gold 审核
		self.loginCRM(user='gold_onedi', psw="Abcd1234")		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		mainpage.click_StatusSelect("待RO审批")
		mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		applypage.click_popWindow("确定")
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("待黄金RO审批", mainpage.get_status(self.email), "gold审核不通过")
		globals()["status"] = mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("结算") != -1, "状态不是待CS2审核")
	def test7_Process2_opstosuccess(self):
		# ro to ops
		self.loginCRM(user='ops_t1')		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
		applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		mainpage.click_StatusSelect("待结算审批")
		mainpage.wait_LoadingModal()

		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("完成")
		applypage.send_accountNumber(randox=1)
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertEqual(mainpage.get_status(self.email), '成功', "ops审核有误")
		globals()["status"] = mainpage.get_status(self.email)


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess2))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
