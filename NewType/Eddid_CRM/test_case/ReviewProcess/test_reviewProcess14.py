#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess14(ReviewProcessTool):
    # 多角色RO

    def test_01_Process14_roadmin(self):
        # 多角色通过
        self.gm.set_value(apiStatus="processing")
        self.gm.set_List("accountType", ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])
        self.gm.set_value(email=apply_create.apply_create_api())
        publicTool.LoginCRM(self, user='onedi.admin', psw="Abcd1234")      #先登录
        status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")


        


if __name__ == "__main__":

    pytest.main(['-k', "test_reviewProcess14"])