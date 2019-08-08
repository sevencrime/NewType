#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap

pytest.mark.skip(reason="隐藏黄金,跳过")
class Test_reviewProcess12(ReviewProcessTool):
    # 黄金RO拒绝, CS2驳回给RO 

    @pytest.mark.dependency()
    def test_01_Process12_gold(self):
        # cliff审核
        self.gm.set_value(apiStatus="processing")
        self.gm.set_List("accountType", ["bullionMargin"])
        self.gm.set_value(email=apply_create.apply_create_api())
        publicTool.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
        status = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待RO审批")


    @pytest.mark.dependency(depends=["TestExample::test_01_Process12_gold"])
    def test_02_Process12_cstogold(self):

        publicTool.LoginCRM(self, user='cs_t1')
        status = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批", btn_text="信息无误")
        

if __name__ == "__main__":
    pytest.main()