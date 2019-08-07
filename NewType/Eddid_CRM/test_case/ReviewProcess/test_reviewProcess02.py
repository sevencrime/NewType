#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import GlobalMap, Logging


class Test_reviewProcess2(ReviewProcessTool):
	# App来源正向审核: 待cs1--待cs2--待RO--待ops--success`

	@pytest.mark.dependency()
	def test1_Process2_cs1tocs2(self):
		# CS1---CS2
		self.gm.set_value(apiStatus="reviewing")
		self.gm.set_List("accountType", ["securitiesCash", "futuresMargin"])
		self.gm.set_value(email=apply_create.apply_create_api())
		publicTool.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")
		status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待CS1审批")

		
	@pytest.mark.dependency(depends=["TestExample::test1_Process2_cs1tocs2"])
	def test2_Process2_cs2toro(self):
		# cs2 to ro

		publicTool.LoginCRM(self, user='cs_t1')
		status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待CS2审批")


	@pytest.mark.dependency(depends=["TestExample::test2_Process2_cs2toro"])
	def test3_Process2_cliff(self):
		# cliff审核

		publicTool.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")
		status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")


	@pytest.mark.dependency(depends=["TestExample::test3_Process2_cliff"])
	def test4_Process2_don(self):
		# don审核

		publicTool.LoginCRM(self, user='ro1_don', psw='Abcd1234')
		status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @pytest.mark.dependency(depends=["TestExample::test1_Process2_cs1tocs2"])
	# def test5_Process2_aaron(self):
	#
	# 	publicTool.LoginCRM(self, user='aaron_chan')
	# 	status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @pytest.mark.dependency(depends=["TestExample::test1_Process2_cs1tocs2"])
	# def test6_Process2_gold(self):
	# 	# gold 审核
    #
	# 	publicTool.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
	# 	status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	@pytest.mark.dependency(depends=["TestExample::test4_Process2_don"])
	def test7_Process2_opstosuccess(self):
		# ro to ops

		publicTool.LoginCRM(self, user='ops_t1')
		status = self.reviewFinish(email=self.gm.get_value("email"), statusSel="待结算审批")


if __name__ == "__main__":
	# suite = unittest.TestSuite()
	# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess2))
	# runner = unittest.TextTestRunner(verbosity=2)
	# runner.run(suite)
	pytest.main()
