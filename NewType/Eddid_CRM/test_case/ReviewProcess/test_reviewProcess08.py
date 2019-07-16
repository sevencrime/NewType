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
from test_case.public.publicTool import publicTool

class Test_reviewProcess8(ReviewProcessTool):
    # 期货RO拒绝, CS2驳回给RO 
    globals()["status"] = ""
    gm = GlobalMap.GlobalMap()
    gm.set_value(apiStatus="processing")
    gm.set_List("accountType", ["futuresMargin"])

    # @reviewProcessTool.skipIf(status = "待证券RO审批")
    def test_01_Process8_don(self):
        # cliff审核
        publicTool.LoginCRM(self, user='ro1_don', psw="Abcd1234")
        globals()["status"] = self.reviewRefuse(email=self.gm.get_value("email"), statusSel="待RO审批")


    def test_02_Process8_cstodon(self):
        if globals()["status"].find("期货RO拒绝") == -1 :
            pytest.xfail("数据状态是 {}".format(globals()["status"]))

        publicTool.LoginCRM(self, user='cs_t1')
        globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批", btn_text="信息无误")
        

if __name__ == "__main__":
    # pytest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess8))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)