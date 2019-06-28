#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_case.Test_Login import *
import unittest
import pytest
from ReviewProcessTool import ReviewProcessTool


class reviewProcess4(ReviewProcessTool):
	# CRM来源驳回流程: 未处理---待cs2--拒绝--sales修改给CS2--RO--RO拒绝--CS驳回给RO
	globals()["status"] = "待CS2审核"
	email = "8307onedi493907@qq.com"

	# @unittest.skipIf(globals()["status"].find("未处理") != -1, "状态不是未处理")
	# @skipIf("未处理")
	def test_a_Process1_salestocs2(self):
		# sales--cs2
		Test_Login.LoginCRM(self, user='sales_t1')		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
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
		
	# @unittest.skipUnless(globals()["status"].find("CS2") != -1, "状态不是CS2")
	# @skipIf("CS2")
	def test_b_Process4_cs2torefuse(self):
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
		
	# @unittest.skipUnless(globals()["status"].find("拒绝") != -1, "状态不是拒绝")
	# @skipIf("拒绝")
	def test_c_Process4_refusetucs2(self):
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

	# @unittest.skipUnless(globals()["status"].find("CS2") != -1, "状态不是待CS2审核")
	# @skipIf("CS2")
	def test_d_Process4_cs2toro(self):
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

	# @unittest.skipUnless(globals()["status"].find("待证券RO审批") != -1, "状态不是待证券RO审批")
	# @skipIf("待证券RO审批")
	def test_e_Process4_cliffRefuse(self):
		# cliff拒绝
		#先判断状态是否正确
		if "待证券RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待RO审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("拒绝")
		self.applypage.rejectReason("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("证券RO拒绝", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("证券RO拒绝") != -1, "状态不是证券RO拒绝")
	# @skipIf("证券RO拒绝")
	def test_f_Process4_cs2toro(self):
		# cs2 to ro
		#先判断状态是否正确
		if "证券RO拒绝" not in globals()["status"] :
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

		self.applypage.click_sublimeApply("信息无误")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		# self.assertIsNot("CS2", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("待期货RO审批") != -1, "状态不是待期货RO审批")
	# @skipIf("待期货RO审批")
	def test_g_Process4_donRefuse(self):
		# cliff拒绝
		#先判断状态是否正确
		if "待期货RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='ro1_don', psw="Abcd1234")		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待RO审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("拒绝")
		self.applypage.rejectReason("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("期货RO拒绝", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("期货RO拒绝") != -1, "状态不是期货RO拒绝")
	# @skipIf("期货RO拒绝")
	def test_h_Process4_cs2toro(self):
		# cs2 to ro
		#先判断状态是否正确
		if "期货RO拒绝" not in globals()["status"] :
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

		self.applypage.click_sublimeApply("信息无误")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		# self.assertIsNot("CS2", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("待外汇RO审批") != -1, "状态不是外汇RO审批")
	# @skipIf("待外汇RO审批")
	def test_i_Process4_aaronRefuse(self):
		# cliff拒绝
		#先判断状态是否正确
		if "待外汇RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='aaron_chan')		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待RO审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("拒绝")
		self.applypage.rejectReason("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("外汇RO拒绝", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("外汇RO拒绝") != -1, "状态不是外汇RO拒绝")
	# @skipIf("外汇RO拒绝")
	def test_j_Process4_cs2toro(self):
		# cs2 to ro
		#先判断状态是否正确
		if "外汇RO拒绝" not in globals()["status"] :
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

		self.applypage.click_sublimeApply("信息无误")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		# self.assertIsNot("CS2", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("待黄金RO审批") != -1, "状态不是待黄金RO审批")
	# @skipIf("待黄金RO审批")
	def test_k_Process4_glodRefuse(self):
		# cliff拒绝
		#先判断状态是否正确
		if "待黄金RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='gold_onedi', psw="Abcd1234")		#先登录

		self.MenuListPage.click_apply_manager()		#点击开户管理
		self.MenuListPage.click_applylist()		    #点击开户列表
		self.mainpage.wait_LoadingModal()

		self.mainpage.click_StatusSelect("待RO审批")
		self.mainpage.wait_LoadingModal()

		# import pdb;pdb.set_trace()
		self.mainpage.get_apply(email=self.email)
		self.mainpage.wait_LoadingModal()
		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-detail', '不能进入Apply详情页')

		self.applypage.click_sublimeApply("拒绝")
		self.applypage.rejectReason("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		self.assertIsNot("黄金RO拒绝", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)

	# @unittest.skipUnless(globals()["status"].find("黄金RO拒绝") != -1, "状态不是黄金RO拒绝")
	# @skipIf("黄金RO拒绝")
	def test_l_Process4_cs2toro(self):
		# cs2 to ro
		#先判断状态是否正确
		if "黄金RO拒绝" not in globals()["status"] :
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

		self.applypage.click_sublimeApply("信息无误")
		self.applypage.click_popWindow("确定")
		self.mainpage.wait_LoadingModal()

		self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "页面没有从Apply详情页跳转到list页面")
		# self.assertIsNot("CS2", self.mainpage.get_status(self.email), "状态没有改变")
		globals()["status"] = self.mainpage.get_status(self.email)



if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess4))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
