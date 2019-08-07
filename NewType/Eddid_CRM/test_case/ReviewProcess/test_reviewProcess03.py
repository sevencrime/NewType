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

	@pytest.mark.dependency()
	def test_01_Process3_cs1torefuse(self):
		# CS1---Refuse
		self.gm.set_value(apiStatus="reviewing")
		self.gm.set_List("accountType", ["leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])
		self.gm.set_value(email=apply_create.apply_create_api())
		publicTool.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")		#先登录
		status = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待CS1审批")
		
	@pytest.mark.dependency(depends=["TestExample::test_01_Process3_cs1torefuse"])
	def test_02_Process3_refusetocs2(self):
		# CS1---Refuse

		publicTool.LoginCRM(self, user='cs1_onedi', psw="Abcd1234")		#先登录
		status = self.reviewUpdate(email=self.gm.get_value("email"), statusSel="拒绝")


	@pytest.mark.dependency(depends=["TestExample::test_02_Process3_refusetocs2"])
	def test_03_Process3_cs2torefuse(self):
		# CS1---Refuse

		publicTool.LoginCRM(self, user='cs_t1')		#先登录
		status = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待CS2审批")


	@pytest.mark.dependency(depends=["TestExample::test_03_Process3_cs2torefuse"])
	def test_04_Process3_refusetucs2(self):
		# CS1---Refuse

		publicTool.LoginCRM(self, user='sales_t1')		#先登录
		status = self.reviewUpdate(email=self.gm.get_value("email"), statusSel="拒绝")




if __name__ == "__main__":
	pytest.main()