#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess9(ReviewProcessTool):
    # CRM来源, 期货RO拒绝, CS2 确定拒绝

    @pytest.mark.dependency()
    def test_01_Process9_don(self):
        # cliff审核
        self.gm.set_value(apiStatus="processing")
        self.gm.set_List("accountType", ["futuresMargin"])
        self.gm.set_value(email=apply_create.apply_create_api())
        publicTool.LoginCRM(self, user='ro1_don', psw="Abcd1234")
        status = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待RO审批")

    @pytest.mark.dependency(depends=["TestExample::test_01_Process9_don"])
    def test_02_Process9_cstoRefuse(self):

        publicTool.LoginCRM(self, user='cs_t1')
        status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批", btn_text="确定拒绝")
        

if __name__ == "__main__":
    pytest.main()