#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_case.Test_Login import *
import unittest
import pytest
from ReviewProcessTool import ReviewProcessTool


class reviewProcess3(ReviewProcessTool):
	# App来源驳回流程: 待cs1--拒绝--CS1修改后重新提交给CS2--CS2拒绝
	globals()["status"] = "待CS1审核"
	email = "5953onedi417211@qq.com"

	# @skipIf("CS1")
	def test_01_Process3_cs1torefuse(self):
		# CS1---Refuse
		Test_Login.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")		#先登录

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
		
	# @skipIf("拒绝")
	def test_02_Process3_refusetocs2(self):
		# CS1---Refuse
		#先判断状态是否正确
		if "拒绝" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")		#先登录

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

	# @skipIf("CS2")
	def test_03_Process3_cs2torefuse(self):
		# CS1---Refuse
		#先判断状态是否正确
		if "CS2" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='cs_t1')		#先登录

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

	# @skipIf("拒绝")		
	def test_04_Process3_refusetucs2(self):
		# CS1---Refuse
		#先判断状态是否正确
		if "拒绝" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='sales_t1')		#先登录

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

	# @skipIf("CS2")
	def test_05_Process3_cs2toro(self):
		# cs2 to ro
		#先判断状态是否正确
		if "CS2" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='cs_t1')		#先登录

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

		


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess3))
	runner = unittest.TextTestRunner(verbosity=3)
	runner.run(suite)
