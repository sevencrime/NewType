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

class Test_reviewProcess14(ReviewProcessTool):
    # 多角色RO
    globals()["status"] = ""
    gm = GlobalMap.GlobalMap()
    gm.set_value(apiStatus="processing")
    gm.set_List("accountType", ["bullionMargin", "leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])

    def test_01_Process14_roadmin(self):
        # 多角色通过

        publicTool.LoginCRM(self, user='onedi.admin', psw="Abcd1234")      #先登录
        globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

        self.assertEqual("待结算审批", globals()["status"], "onedi.admin审核后状态没有改变")

        


if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess5))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    pytest.main(['-k', "test_reviewProcess5"])