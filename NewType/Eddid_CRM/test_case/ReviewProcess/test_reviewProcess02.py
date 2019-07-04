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


class reviewProcess2(ReviewProcessTool):
	# App来源正向审核: 待cs1--待cs2--待RO--待ops--success`
	globals()["status"] = ""
	email = "4744onedi1118741@qq.com"

	# @skipIf(status = "CS1")
	def test1_Process2_cs1tocs2(self):
		# CS1---CS2

		Test_Login.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")
		globals()["status"] = self.reviewPass(email=self.email, statusSel="待CS1审批")

		
	# @skipIf(status = "CS2")
	def test2_Process2_cs2toro(self):
		# cs2 to ro
		#先判断状态是否正确
		if globals()["status"].find("待CS2审批") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='cs_t1')
		globals()["status"] = self.reviewPass(email=self.email, statusSel="待CS2审批")


	# @skipIf(status = "待证券RO审批")
	def test3_Process2_cliff(self):
		# cliff审核
		#先判断状态是否正确
		if globals()["status"].find("待证券RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")
		globals()["status"] = self.reviewPass(email=self.email, statusSel="待RO审批")


	# @skipIf(status = "待期货RO审批")
	def test4_Process2_don(self):
		# don审核
		#先判断状态是否正确
		if globals()["status"].find("待期货RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='ro1_don', psw='Abcd1234')
		globals()["status"] = self.reviewPass(email=self.email, statusSel="待RO审批")

	# @skipIf(status = "待外汇RO审批")
	def test5_Process2_aaron(self):
		# aaron审核
		#先判断状态是否正确
		if globals()["status"].find("待外汇RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='aaron_chan')
		globals()["status"] = self.reviewPass(email=self.email, statusSel="待RO审批")

	# @skipIf(status = "待黄金RO审批")
	def test6_Process2_gold(self):
		# gold 审核
		#先判断状态是否正确
		if globals()["status"].find("待黄金RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
		globals()["status"] = self.reviewPass(email=self.email, statusSel="待RO审批")

	# @skipIf(status = "结算")
	def test7_Process2_opstosuccess(self):
		# ro to ops
		#先判断状态是否正确
		if globals()["status"].find("待结算审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		Test_Login.LoginCRM(self, user='ops_t1')
		globals()["status"] = self.reviewFinish(email=self.email, statusSel="待结算审批")


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess2))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
