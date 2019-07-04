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

class reviewProcess12(ReviewProcessTool):
    # 黄金RO拒绝, CS2驳回给RO 
    globals()["status"] = ""
    email = "6621onedi374130@qq.com"

    # @reviewProcessTool.skipIf(status = "待证券RO审批")
    def test_01_Process12_gold(self):
        # cliff审核
        Test_Login.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
        globals()["status"] = self.reviewRefuse(email=self.email, statusSel="待RO审批")


    def test_01_Process12_cstogold(self):
        if globals()["status"].find("待CS2审批") == -1 :
            pytest.xfail("数据状态是 {}".format(globals()["status"]))

        Test_Login.LoginCRM(self, user='cs_t1')
        globals()["status"] = self.reviewPass(email=self.email, statusSel="待RO审批", btn_text="信息无误")
        

if __name__ == "__main__":
    # pytest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess1))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)