#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("Eddid_CRM\\")+len("Eddid_CRM\\")]
sys.path.append(rootPath)
from test_case.Test_Login import *
import unittest
import pytest
from ReviewProcessTool import ReviewProcessTool

class reviewProcess1(ReviewProcessTool):
	# CRM and apply_form正向审核: 未处理--待cs2--待RO--待ops--success
	globals()["status"] = ""
	email = "6082onedi459928@qq.com"

	# @reviewProcessTool.skipIf(status = "未处理")
	def test1_Process1_sales_to_cs2(self):
		# sales--cs2
		Test_Login.LoginCRM(self, user='sales_t1')
		import pdb; pdb.set_trace()
		self.submitReview(email=self.email, statusSel="未处理")
		
	# @reviewProcessTool.skipIf(status = "CS2")
	def test2_Process1_cs2_to_ro(self):
		# cs2 to ro
		#先判断状态是否正确
		if "CS2" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		# self.loginCRM(user='cs_t1')		#先登录
		Test_Login.LoginCRM(self, user='cs_t1')
		self.reviewPass(email=self.email, statusSel="待CS2")

	# @reviewProcessTool.skipIf(status = "待证券RO审批")
	def test3_Process1_cliff(self):
		# cliff审核
		if "待证券RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		# self.loginCRM(user='ro1_cliff', psw="Abcd1234")		#先登录
		Test_Login.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")
		self.reviewPass(email=self.email, statusSel="待证券RO审批")

	# @reviewProcessTool.skipIf(status = "待期货RO审批")
	def test4_Process1_don(self):
		# don审核
		if "待期货RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		# self.loginCRM(user='ro1_don', psw='Abcd1234')		#先登录
		Test_Login.LoginCRM(self, user='ro1_don', psw='Abcd1234')
		self.reviewPass(email=self.email, statusSel="待期货RO审批")

	# @reviewProcessTool.skipIf(status = "待外汇RO审批")
	def test5_Process1_aaron(self):
		# aaron审核
		if "待外汇RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		Test_Login.LoginCRM(self, user='aaron_chan')
		self.reviewPass(email=self.email, statusSel="待外汇RO审批")

	# @reviewProcessTool.skipIf(status = "待黄金RO审批")
	def test6_Process1_gold(self):
		# gold 审核
		if "待黄金RO审批" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
		
		# self.loginCRM(user='gold_onedi', psw="Abcd1234")		#先登录
		Test_Login.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
		self.reviewPass(email=self.email, statusSel="待黄金RO审批")

	# @reviewProcessTool.skipIf(status = "结算")
	def test7_Process1_ops_to_success(self):
		# ro to ops
		if "结算" not in globals()["status"] :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		# self.loginCRM(user='ops_t1')		#先登录
		Test_Login.LoginCRM(self, user='ops_t1')
		self.reviewFinish(email=self.email, statusSel="待结算审批")


if __name__ == "__main__":
	# pytest.main()
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess1))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)