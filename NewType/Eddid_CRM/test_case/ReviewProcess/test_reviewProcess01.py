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
from test_case.public.publicTool import publicTool

class Test_reviewProcess1(ReviewProcessTool):
	# CRM and apply_form正向审核: 未处理--待cs2--待RO--待ops--success
	globals()["status"] = ""
	gm = GlobalMap.GlobalMap()
	gm.set_value(apiStatus="unprocessed")
	gm.set_List("accountType", ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])


	# @reviewProcessTool.skipIf(status = "未处理")
	def test01_Process1_sales_to_cs2(self):
		# sales--cs2
		publicTool.LoginCRM(self, user='sales_t1')
		globals()["status"] = self.submitReview(email=self.gm.get_value("email"), statusSel="未处理")
		
	# @reviewProcessTool.skipIf(status = "CS2")
	def test02_Process1_cs2_to_ro(self):
		# cs2 to ro
		#先判断状态是否正确
		if globals()["status"].find("待CS2审批") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='cs_t1')
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待CS2审批")


	# @reviewProcessTool.skipIf(status = "待证券RO审批")
	def test03_Process1_cliff(self):
		# cliff审核
		if globals()["status"].find("待证券RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @reviewProcessTool.skipIf(status = "待期货RO审批")
	def test04_Process1_don(self):
		# don审核
		if globals()["status"].find("待期货RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='ro1_don', psw='Abcd1234')
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @reviewProcessTool.skipIf(status = "待外汇RO审批")
	def test05_Process1_aaron(self):
		# aaron审核
		if globals()["status"].find("待外汇RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='aaron_chan')
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @reviewProcessTool.skipIf(status = "待黄金RO审批")
	def test6_Process1_gold(self):
		# gold 审核
		if globals()["status"].find("待黄金RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
		
		publicTool.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")


	# @reviewProcessTool.skipIf(status = "结算")
	def test07_Process1_ops_to_success(self):
		# ro to ops
		if globals()["status"].find("待结算审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='ops_t1')
		globals()["status"] = self.reviewFinish(email=self.gm.get_value("email"), statusSel="待结算审批")


if __name__ == "__main__":
	# pytest.main()
	# suite = unittest.TestSuite()
	# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess1))
	# runner = unittest.TextTestRunner(verbosity=2)
	# runner.run(suite)
	pytest.main("-s -v test_reviewProcess01.py::Test_reviewProcess1")