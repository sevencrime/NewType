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


class Test_reviewProcess3(ReviewProcessTool):
	# App来源驳回流程: 待cs1--拒绝--CS1修改后重新提交给CS2--CS2拒绝
	globals()["status"] = ""
	gm = GlobalMap.GlobalMap()
	gm.set_value(apiStatus="reviewing")
	gm.set_List("accountType", ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])

	# @skipIf("CS1")
	def test_01_Process3_cs1torefuse(self):
		# CS1---Refuse
		Test_Login.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")		#先登录
		globals()["status"] = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待CS1审批")
		
	# @skipIf("拒绝")
	def test_02_Process3_refusetocs2(self):
		# CS1---Refuse
		#先判断状态是否正确
		if globals()["status"].find("拒绝") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")		#先登录
		globals()["status"] = self.reviewUpdate(email=self.gm.get_value("email"), statusSel="拒绝")


	# @skipIf("CS2")
	def test_03_Process3_cs2torefuse(self):
		# CS1---Refuse
		#先判断状态是否正确
		if globals()["status"].find("待CS2审批") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='cs_t1')		#先登录
		globals()["status"] = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待CS2审批")


	# @skipIf("拒绝")		
	def test_04_Process3_refusetucs2(self):
		# CS1---Refuse
		#先判断状态是否正确
		if globals()["status"].find("拒绝") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		Test_Login.LoginCRM(self, user='sales_t1')		#先登录
		globals()["status"] = self.reviewUpdate(email=self.gm.get_value("email"), statusSel="拒绝")




if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess3))
	runner = unittest.TextTestRunner(verbosity=3)
	runner.run(suite)
