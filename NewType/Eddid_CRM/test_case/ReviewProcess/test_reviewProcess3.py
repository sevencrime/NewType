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
	# App来源驳回流程: 待cs1--拒绝--CS1修改后重新提交给CS2--CS2拒绝--sales修改给CS2--RO--OPS--成功
	globals()["status"] = "待CS1审核"

	@classmethod
	def setUpClass(self):
		self.email = "5953onedi417211@qq.com"

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

	@skipIf("CS1")
	def test_a_Process3_cs1torefuse(self):
		# CS1---Refuse
		Test_Login.LoginCRM(user='cs1_onedi', psw="Abcd1234")		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		# import pdb; pdb.set_trace()
		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect("待CS1审批")
		self.mainpage.wait_LoadingModal()

		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("拒绝")
		# 选择拒绝原因
		self.applypage.rejectReason("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("拒绝", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)
		
	@skipIf("拒绝")
	def test_b_Process3_refusetocs2(self):
		# CS1---Refuse
		Test_Login.LoginCRM(user='cs1_onedi', psw="Abcd1234")		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()
		# 下拉列表选择待CS2审批
		# import pdb; pdb.set_trace()
		self.mainpage.click_StatusSelect("拒绝")
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_checkbox(self.email)	#选择多选框
		self.mainpage.click_update()	#点击修改按钮
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-update', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("提交")
		# 选择拒绝原因
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("CS2", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf("CS2")
	def test_c_Process3_cs2torefuse(self):
		# CS1---Refuse
		Test_Login.LoginCRM(user='cs_t1')		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect("待CS2审批")
		self.mainpage.wait_LoadingModal()

		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("拒绝")
		# 选择拒绝原因
		self.applypage.rejectReason("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("拒绝", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf("拒绝")		
	def test_d_Process3_refusetucs2(self):
		# CS1---Refuse
		Test_Login.LoginCRM(user='sales_t1')		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		# 下拉列表选择待CS2审批
		self.mainpage.click_StatusSelect("拒绝")
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_checkbox(self.email)	#选择多选框
		self.mainpage.click_update()	#点击修改按钮
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-update', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("提交")
		# 选择拒绝原因
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("CS2", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf("CS2")
	def test_e_Process3_cs2toro(self):
		# cs2 to ro
		Test_Login.LoginCRM(user='cs_t1')		#先登录

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
		# self.assertIsNot("CS2", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf("待证券RO审批")
	def test_f_Process3_cliff(self):
		# cliff审核
		Test_Login.LoginCRM(user='ro1_cliff', psw="Abcd1234")		#先登录

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
		self.assertIsNot("待证券RO审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf("待期货RO审批")
	def test_g_Process3_don(self):
		# don审核
		Test_Login.LoginCRM(user='ro1_don', psw='Abcd1234')		#先登录

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
		self.assertIsNot("待期货RO审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf("待外汇RO审批")
	def test_h_Process3_aaron(self):
		# aaron审核
		Test_Login.LoginCRM(user='aaron_chan')		#先登录

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
		self.assertIsNot("待外汇RO审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	@skipIf("待黄金RO审批")
	def test_i_Process3_gold(self):
		# gold 审核
		Test_Login.LoginCRM(user='gold_onedi', psw="Abcd1234")		#先登录

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
		self.assertIsNot("待黄金RO审批", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("结算") != -1, "状态不是待结算审核")
	@skipIf("RO审批")
	def test_j_Process3_opstosuccess(self):
		# ro to ops
		Test_Login.LoginCRM(user='ops_t1')		#先登录

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
		self.assertEqual("成功", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)



		


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess3))
	runner = unittest.TextTestRunner(verbosity=3)
	runner.run(suite)
