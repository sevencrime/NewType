#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

import pytest

from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess13(ReviewProcessTool):
    #  黄金RO拒绝, CS2 确定拒绝
    globals()["status"] = ""
    gm = GlobalMap.GlobalMap()
    gm.set_value(apiStatus="processing")
    gm.set_List("accountType", ["bullionMargin"])

    # @reviewProcessTool.skipIf(status = "待证券RO审批")
    def test_01_Process13_gold(self):
        # print(self.gm.get_value("email"))
        # cliff审核
        publicTool.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
        globals()["status"] = self.reviewRefuse(email = self.gm.get_value("email"), statusSel="待RO审批")


    def test_02_Process13_cstoRefuse(self):
        # print(self.gm.get_value("email"))

        if globals()["status"].find("黄金RO拒绝") == -1 :
            pytest.xfail("数据状态是 {}".format(globals()["status"]))

        publicTool.LoginCRM(self, user='cs_t1')
        globals()["status"] = self.reviewPass(email = self.gm.get_value("email"), statusSel="待RO审批", btn_text="确定拒绝")
        

if __name__ == "__main__":
    # pytest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_reviewProcess13))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # pytest.main(['-s', 'test_reviewProcess13.py'])
