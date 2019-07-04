#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("Eddid_CRM\\")+len("Eddid_CRM\\")]
sys.path.append(rootPath)
from test_case.Test_Login import *
import unittest
import pytest
from ReviewProcessTool import ReviewProcessTool

class reviewProcess11(ReviewProcessTool):
    # 外汇RO拒绝, CS2 确定拒绝
    globals()["status"] = ""
    email = "6621onedi374130@qq.com"

    # @reviewProcessTool.skipIf(status = "待证券RO审批")
    def test_01_Process11_aaron(self):
        # cliff审核
        Test_Login.LoginCRM(self, user='aaron_chan')
        globals()["status"] = self.reviewRefuse(email=self.email, statusSel="待RO审批")


    def test_02_Process11_cstoRefuse(self):
        if globals()["status"].find("待CS2审批") == -1 :
            pytest.xfail("数据状态是 {}".format(globals()["status"]))

        Test_Login.LoginCRM(self, user='cs_t1')
        globals()["status"] = self.reviewPass(email=self.email, statusSel="待RO审批", btn_text="确定拒绝")
        

if __name__ == "__main__":
    # pytest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess11))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)