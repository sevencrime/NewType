#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from PageElement import *
from Commons import *
import unittest
from selenium import webdriver
import time

class reviewProcess1(unittest.TestCase):
	# CRM and apply_form正向审核: 未处理--待cs2--待RO--待ops--success

	email = "606onedi2s2729@qq.com"

	def setUp(self):
		self.driver = webdriver.Chrome()
		# self.driver = webdriver.Firefox(executable_path = 'geckodriver')
		# self.driver.implicitly_wait(30)   
		self.driver.set_page_load_timeout(30)
		self.driver.set_script_timeout(30)
		self.url = 'http://eddid-bos-uat.ntdev.be'

	def tearDown(self):
		time.sleep(5)
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

	# @unittest.skip("暂时跳过")
	def test1_Process1_salestocs2(self, email):
		# sales--cs2
		self.loginCRM(user='sales_t1')		#先登录

		applylistpage = ApplyListPage.ApplyListPage(self.driver, self.url, "Eddid")
		mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")

		# import pdb;pdb.set_trace()

		applylistpage.click_apply_manager()		#点击开户管理
		applylistpage.click_applylist()		    #点击开户列表
		mainpage.wait_LoadingModal()

		# 下拉列表选择未处理
		mainpage.click_StatusSelect("未处理")
		mainpage.wait_LoadingModal()

		# 判断状态校验功能是否正常,选择编号
		mainpage.click_checkbox(email=self.email)	
		mainpage.click_submitreview()
		mainpage.click_popWindow()
		mainpage.wait_LoadingModal()
		

	# @unittest.skip("暂时跳过")
	def test2_Process1_cs2toro(self):
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

		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		mainpage.click_popWindow()
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")

	# @unittest.skip("暂时跳过")
	def test3_Process1_cliff(self):
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

		import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		mainpage.click_popWindow()
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")

	# @unittest.skip("暂时跳过")
	def test4_Process1_don(self):
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

		import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		mainpage.click_popWindow()
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")

	# @unittest.skip("暂时跳过")
	def test4_Process1_aaron(self):
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

		import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		mainpage.click_popWindow()
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")

	# @unittest.skip("暂时跳过")
	def test4_Process1_gold(self):
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

		import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		mainpage.click_popWindow()
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")

	# @unittest.skip("暂时跳过")
	def test4_Process1_rotoops(self):
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

		import pdb;pdb.set_trace()
		mainpage.get_apply(email=self.email)
		mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		applypage.click_sublimeApply("通过")
		mainpage.click_popWindow()
		mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")





if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess1))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)