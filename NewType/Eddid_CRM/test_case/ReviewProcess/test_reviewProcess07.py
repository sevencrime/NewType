#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

import pytest

from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess7(ReviewProcessTool):
    # CRM来源, 证券RO拒绝, CS2 确定拒绝
    globals()["status"] = ""
    gm = GlobalMap.GlobalMap()
    gm.set_value(apiStatus="processing")
    gm.set_List("accountType", ["securitiesCash"])

    # @reviewProcessTool.skipIf(status = "待证券RO审批")
    def test_01_Process7_cliff(self):
        # cliff审核
        publicTool.LoginCRM(self, user='ro1_cliff', psw="Abcd1234")
        globals()["status"] = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待RO审批")


    def test_02_Process7_cstoRefuse(self):
        if globals()["status"].find("证券RO拒绝") == -1 :
            pytest.xfail("数据状态是 {}".format(globals()["status"]))

        publicTool.LoginCRM(self, user='cs_t1')
        globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批", btn_text="确定拒绝")
        

if __name__ == "__main__":
    # pytest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess7))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)