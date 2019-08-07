#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess5(ReviewProcessTool):
    # 多角色RO

    @pytest.mark.dependency()
    def test_01_Process5_aaron(self):
        # aaron 通过
        self.gm.set_value(apiStatus="processing")
        self.gm.set_List("accountType", ["leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])
        self.gm.set_value(email=apply_create.apply_create_api())
        publicTool.LoginCRM(self, user='aaron_chan')
        status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

    @pytest.mark.dependency(depends=["TestExample::test_01_Process5_aaron"])
    def test_02_Process5_roadmin(self):
        # 多角色通过

        publicTool.LoginCRM(self, user='onedi.admin', psw="Abcd1234")      #先登录
        status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")


if __name__ == "__main__":

    pytest.main(['-k', "test_reviewProcess5"])