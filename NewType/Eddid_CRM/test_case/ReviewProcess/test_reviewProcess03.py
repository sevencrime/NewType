#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess3(ReviewProcessTool):
	# App来源驳回流程: 待cs1--拒绝--CS1修改后重新提交给CS2--CS2拒绝
	globals()["status"] = ""

	# @skipIf("CS1")
	def test_01_Process3_cs1torefuse(self):
		# CS1---Refuse
		self.gm.set_value(apiStatus="reviewing")
		self.gm.set_List("accountType", ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])
		self.gm.set_value(email=apply_create.apply_create_api())
		publicTool.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")		#先登录
		globals()["status"] = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待CS1审批")
		
	# @skipIf("拒绝")
	def test_02_Process3_refusetocs2(self):
		# CS1---Refuse
		#先判断状态是否正确
		if globals()["status"].find("拒绝") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")		#先登录
		globals()["status"] = self.reviewUpdate(email=self.gm.get_value("email"), statusSel="拒绝")


	# @skipIf("CS2")
	def test_03_Process3_cs2torefuse(self):
		# CS1---Refuse
		#先判断状态是否正确
		if globals()["status"].find("待CS2审批") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='cs_t1')		#先登录
		globals()["status"] = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待CS2审批")


	# @skipIf("拒绝")		
	def test_04_Process3_refusetucs2(self):
		# CS1---Refuse
		#先判断状态是否正确
		if globals()["status"].find("拒绝") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='sales_t1')		#先登录
		globals()["status"] = self.reviewUpdate(email=self.gm.get_value("email"), statusSel="拒绝")




if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess3))
	runner = unittest.TextTestRunner(verbosity=3)
	runner.run(suite)
