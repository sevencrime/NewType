#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import GlobalMap, Logging


class Test_reviewProcess01(ReviewProcessTool):
	# CRM and apply_form正向审核: 未处理--待cs2--待RO--待ops--success

	@pytest.mark.dependency()
	def test01_Process1_sales_to_cs2(self):
		# sales--cs2
		self.gm.set_value(apiStatus="unprocessed")
		self.log.info("类{}所创建的apistatuc的值为: {}".format("Test_reviewProcess01", self.gm.get_value("apiStatus")))
		self.gm.set_List("accountType",["leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])
		self.gm.set_value(email=apply_create.apply_create_api())
		publicTool.LoginCRM(self, user='sales_t1')
		status = self.submitReview(email=self.gm.get_value("email"), statusSel="未处理")
		assert status == "待CS2审批", "sales提交审核后状态没有修改"

	@pytest.mark.dependency(depends=["TestExample::test01_Process1_sales_to_cs2"])
	def test02_Process1_cs2_to_ro(self):
		# cs2 to ro

		publicTool.LoginCRM(self, user='cs_t1')
		status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待CS2审批")
		# assert status == ""

	@pytest.mark.dependency(depends=["TestExample::test02_Process1_cs2_to_ro"])
	def test03_Process1_cliff(self):
		# cliff审核
		# if globals()["status"].find("待证券RO审批") == -1 :
		# 	pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")
		status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	@pytest.mark.dependency(depends=["TestExample::test03_Process1_cliff"])
	def test04_Process1_don(self):
		# don审核
		# if globals()["status"].find("待期货RO审批") == -1 :
		# 	pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='ro1_don', psw='Abcd1234')
		status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	@pytest.mark.dependency(depends=["TestExample::test04_Process1_don"])
	def test05_Process1_aaron(self):
		# aaron审核
		# if globals()["status"].find("待外汇RO审批") == -1 :
		# 	pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='aaron_chan')
		status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @pytest.mark.dependency(depends=["TestExample::test05_Process1_aaron"])
	# def test6_Process1_gold(self):
	# 	# gold 审核
	# 	if globals()["status"].find("待黄金RO审批") == -1 :
	# 		pytest.xfail("数据状态是 {}".format(globals()["status"]))
	#
	# 	publicTool.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
	# 	globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")


	@pytest.mark.dependency(depends=["TestExample::test05_Process1_aaron"])
	def test07_Process1_ops_to_success(self):
		# ro to ops
		# if globals()["status"].find("待结算审批") == -1 :
		# 	pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='ops_t1')
		status = self.reviewFinish(email=self.gm.get_value("email"), statusSel="待结算审批")


if __name__ == "__main__":
	# pytest.main()
	# suite = unittest.TestSuite()
	# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess1))
	# runner = unittest.TextTestRunner(verbosity=2)
	# runner.run(suite)
	pytest.main(["-s", "--pdb", "test_reviewProcess01.py"])





