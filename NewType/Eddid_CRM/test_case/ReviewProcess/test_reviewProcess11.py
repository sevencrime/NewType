#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess11(ReviewProcessTool):
    # 外汇RO拒绝, CS2 确定拒绝
    globals()["status"] = ""

    # @reviewProcessTool.skipIf(status = "待证券RO审批")
    def test_01_Process11_aaron(self):
        # cliff审核
        self.gm.set_value(apiStatus="processing")
        self.gm.set_List("accountType", ["leveragedForeignExchangeAccountMargin"])
        self.gm.set_value(email=apply_create.apply_create_api())
        publicTool.LoginCRM(self, user='aaron_chan')
        globals()["status"] = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待RO审批")


    def test_02_Process11_cstoRefuse(self):
        if globals()["status"].find("外汇RO拒绝") == -1 :
            pytest.xfail("数据状态是 {}".format(globals()["status"]))

        publicTool.LoginCRM(self, user='cs_t1')
        globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批", btn_text="确定拒绝")
        

if __name__ == "__main__":
    # pytest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess11))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)