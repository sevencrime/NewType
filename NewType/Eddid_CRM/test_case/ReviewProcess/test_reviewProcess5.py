#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_case.Test_Login import *
import unittest
import pytest
from ReviewProcessTool import ReviewProcessTool

class reviewProcess5(ReviewProcessTool):
    # 多角色RO
    globals()["status"] = ""
    email = "9706onedi882636@qq.com"
    
    # @unittest.skipIf(globals()["status"].find("未处理") != -1, "状态不是未处理")
    # @skipIf("未处理")
    def test_01_Process5_aaron(self):
        # aaron 通过
        Test_Login.LoginCRM(self, user='aaron_chan')
        globals()["status"] = self.reviewPass(email=self.email, statusSel="待RO审批")


    # @unittest.skipIf(globals()["status"].find("未处理") != -1, "状态不是未处理")
    def test_02_Process5_roadmin(self):
        # 多角色通过

        if globals()["status"].find("待外汇RO审批") != -1:
            pytest.xfail("数据状态是 {}".format(globals()["status"]))

        Test_Login.LoginCRM(self, user='onedi.admin', psw="Abcd1234")      #先登录
        globals()["status"] = self.reviewPass(email=self.email, statusSel="待RO审批")

        self.assertEqual("待结算审批", globals()["status"], "onedi.admin审核后状态没有改变")

        


if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess5))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    pytest.main(['-k', "test_reviewProcess5"])