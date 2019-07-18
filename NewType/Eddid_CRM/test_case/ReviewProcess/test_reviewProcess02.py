#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

import pytest

from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import GlobalMap, Logging


class Test_reviewProcess2(ReviewProcessTool):
	# App来源正向审核: 待cs1--待cs2--待RO--待ops--success`
	globals()["status"] = ""
	gm = GlobalMap.GlobalMap()
	log = Logging.Logs()
	gm.set_value(apiStatus="reviewing")
	gm.set_value(
		token="eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoidGVzdCIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjgzMjQzMTg2NDY2Njpyb2xlXC9kZXYtZWRkaWQtY29nbml0by1hZG1pbi1yb2xlIl0sImF1ZCI6IjUxM2pmY2t0cjFtNmV2b2dmcXU3b3NrN3BhIiwiZXZlbnRfaWQiOiI3YzZiOGYyNi1iN2YwLTQ0MmUtYWI3Ny01ZGFkNzA5ZDhmOWEiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU2MzQzNjk3NiwiZXhwIjoxNTYzNDQwNTc2LCJpYXQiOjE1NjM0MzY5NzYsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluMTIzNEAxNjMuY29tIn0.CAzsPSfywj4vK_bEs2SG72Lrk-poxAvLE5lJtOeI3RabGIr8LaiemP0cT0dM635zusgN5C_Dm89LThv38UzpX7dJaYfOLCj4mER_-n8d-5AO2m6OYUUPt47B_8NP_T7BIYqQE5abEQuCgJeoX3HWf_8wVNW2g7zX81b3blJVsm1Yfz0aOJmSqQ6Wt87Apv0roKD1SxREYFCnaUmJm5SQ5vdKYVmKOa34v7txfyP7Fmsxcbb5hjC7kXFObAUVNtTeEyxDEjL7S-Buc2k7jd9rQgXhVtrlnNQQXK--qraCnZcy2-h1htSUIrvi9tUTdUNlnnTfZqmn-ZtrTm2HKN7gCA")

	log.debug("类{}所创建的apistatuc的值为: {}".format("Test_reviewProcess01", gm.get_value("apiStatus")))
	gm.set_List("accountType", ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])

	# @skipIf(status = "CS1")
	def test1_Process2_cs1tocs2(self):
		# CS1---CS2

		publicTool.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待CS1审批")

		
	# @skipIf(status = "CS2")
	def test2_Process2_cs2toro(self):
		# cs2 to ro
		#先判断状态是否正确
		if globals()["status"].find("待CS2审批") == -1:
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='cs_t1')
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待CS2审批")


	# @skipIf(status = "待证券RO审批")
	def test3_Process2_cliff(self):
		# cliff审核
		#先判断状态是否正确
		if globals()["status"].find("待证券RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")


	# @skipIf(status = "待期货RO审批")
	def test4_Process2_don(self):
		# don审核
		#先判断状态是否正确
		if globals()["status"].find("待期货RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='ro1_don', psw='Abcd1234')
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @skipIf(status = "待外汇RO审批")
	def test5_Process2_aaron(self):
		# aaron审核
		#先判断状态是否正确
		if globals()["status"].find("待外汇RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='aaron_chan')
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @skipIf(status = "待黄金RO审批")
	def test6_Process2_gold(self):
		# gold 审核
		#先判断状态是否正确
		if globals()["status"].find("待黄金RO审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))

		publicTool.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
		globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

	# @skipIf(status = "结算")
	def test7_Process2_opstosuccess(self):
		# ro to ops
		#先判断状态是否正确
		if globals()["status"].find("待结算审批") == -1 :
			pytest.xfail("数据状态是 {}".format(globals()["status"]))
			
		publicTool.LoginCRM(self, user='ops_t1')
		globals()["status"] = self.reviewFinish(email=self.gm.get_value("email"), statusSel="待结算审批")


if __name__ == "__main__":
	# suite = unittest.TestSuite()
	# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess2))
	# runner = unittest.TextTestRunner(verbosity=2)
	# runner.run(suite)
	pytest.main()
