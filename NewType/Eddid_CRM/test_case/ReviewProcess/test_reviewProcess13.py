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

class Test_reviewProcess13(ReviewProcessTool):
    #  黄金RO拒绝, CS2 确定拒绝
    globals()["status"] = ""

    # @reviewProcessTool.skipIf(status = "待证券RO审批")
    def test_01_Process13_gold(self):
        print(globals()["email"])
        import pdb;pdb.set_trace()
        # cliff审核
        Test_Login.LoginCRM(self, user='gold_onedi', psw="Abcd1234")
        globals()["status"] = self.reviewRefuse(email=globals()["email"], statusSel="待RO审批")


    # def test_02_Process13_cstoRefuse(self):
    #     print(globals()["email"])
    #     if globals()["status"].find("待CS2审批") == -1 :
    #         pytest.xfail("数据状态是 {}".format(globals()["status"]))

    #     Test_Login.LoginCRM(self, user='cs_t1')
    #     globals()["status"] = self.reviewPass(email=globals()["email"], statusSel="待RO审批", btn_text="确定拒绝")
        

if __name__ == "__main__":
    # pytest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_reviewProcess13))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # pytest.main(['-s', 'test_reviewProcess13.py'])
