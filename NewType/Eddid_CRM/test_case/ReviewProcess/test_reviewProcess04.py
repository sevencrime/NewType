#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess4(ReviewProcessTool):
	# CRM来源驳回流程: 待cs2--拒绝--sales修改给CS2

	@pytest.mark.dependency()
	def test_01_Process4_cs2torefuse(self):
		# CS1---Refuse
		self.gm.set_value(apiStatus="csApproval")
		self.gm.set_List("accountType", ["leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])
		self.gm.set_value(email=apply_create.apply_create_api())
		publicTool.LoginCRM(self, user='cs_t1')		#先登录
		status = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待CS2审批")


	@pytest.mark.dependency(depends=["TestExample::test_01_Process4_cs2torefuse"])
	def test_02_Process4_refusetucs2(self):
		# CS1---Refuse

		publicTool.LoginCRM(self, user='sales_t1')		#先登录
		status = self.reviewUpdate(email=self.gm.get_value("email"), statusSel="拒绝")



if __name__ == "__main__":
	pytest.main()