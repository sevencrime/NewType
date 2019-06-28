#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_case.Test_Login import *
import unittest
import pytest
from ReviewProcessTool import ReviewProcessTool


class reviewProcess2(ReviewProcessTool):
	# App来源正向审核: 待cs1--待cs2--待RO--待ops--success`
	globals()["status"] = "待CS1审核"
	email = "5600onedi1235041@qq.com"

	# @skipIf(status = "CS1")
	def test1_Process2_cs1tocs2(self):
		# CS1---CS2
		Test_Login.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")

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
		
	# @skipIf(status = "CS2")
	def test2_Process2_cs2toro(self):
		# cs2 to ro
		#先判断状态是否正确
		if "CS2" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='cs_t1')

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

	# @skipIf(status = "待证券RO审批")
	def test3_Process2_cliff(self):
		# cliff审核
		#先判断状态是否正确
		if "待证券RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")

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

	# @skipIf(status = "待期货RO审批")
	def test4_Process2_don(self):
		# don审核
		#先判断状态是否正确
		if "待期货RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='ro1_don', psw='Abcd1234')

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

	# @skipIf(status = "待外汇RO审批")
	def test5_Process2_aaron(self):
		# aaron审核
		#先判断状态是否正确
		if "待外汇RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='aaron_chan')

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

	# @skipIf(status = "待黄金RO审批")
	def test6_Process2_gold(self):
		# gold 审核
		#先判断状态是否正确
		if "待黄金RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='gold_onedi', psw="Abcd1234")

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

	# @skipIf(status = "结算")
	def test7_Process2_opstosuccess(self):
		# ro to ops
		#先判断状态是否正确
		if "结算" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		Test_Login.LoginCRM(self, user='ops_t1')

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
