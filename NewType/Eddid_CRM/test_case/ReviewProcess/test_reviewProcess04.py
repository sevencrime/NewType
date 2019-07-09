#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_case.Test_Login import *
import unittest
import pytest
from ReviewProcessTool import ReviewProcessTool


class reviewProcess4(ReviewProcessTool):
	# CRM来源驳回流程: 未处理---待cs2--拒绝--sales修改给CS2
    globals()["status"] = ""
    gm = GlobalMap.GlobalMap()
    gm.set_value(apiStatus="unprocessed")
    gm.set_List("accountType", ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])

	def test_01_Process4_cs2torefuse(self):
		# CS1---Refuse
		#先判断状态是否正确
		if globals()["status"].find("待CS2审批") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='cs_t1')		#先登录
		globals()["status"] = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待CS2审批")		


	# @unittest.skipUnless(globals()["status"].find("拒绝") != -1, "状态不是拒绝")
	# @skipIf("拒绝")
	def test_02_Process4_refusetucs2(self):
		# CS1---Refuse
		#先判断状态是否正确
		if globals()["status"].find("拒绝") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='sales_t1')		#先登录
		globals()["status"] = self.reviewUpdate(email=self.gm.get_value("email"), statusSel="拒绝")

		self.assertIsNot("待CS2审批", self.mainpage.get_status(self.gm.get_value("email")), "状态没有改变")
		

if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess4))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
