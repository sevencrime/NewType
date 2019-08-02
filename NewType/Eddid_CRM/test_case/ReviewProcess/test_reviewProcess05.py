#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from Interface import apply_create
from test_case.ReviewProcess.ReviewProcessTool import ReviewProcessTool
from test_case.public.publicTool import publicTool
from Commons import Logging, GlobalMap


class Test_reviewProcess5(ReviewProcessTool):
    # 多角色RO
    globals()["status"] = ""

    def test_01_Process5_aaron(self):
        # aaron 通过
        self.gm.set_value(apiStatus="processing")
        self.gm.set_List("accountType", ["leveragedForeignExchangeAccountMargin", "securitiesCash", "futuresMargin"])
        self.gm.set_value(email=apply_create.apply_create_api())
        publicTool.LoginCRM(self, user='aaron_chan')
        globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")


    def test_02_Process5_roadmin(self):
        # 多角色通过
        if globals()["status"].find("待外汇RO审批") != -1:
            pytest.xfail("数据状态是 {}".format(globals()["status"]))

        publicTool.LoginCRM(self, user='onedi.admin', psw="Abcd1234")      #先登录
        globals()["status"] = self.reviewPass(email=self.gm.get_value("email"), statusSel="待RO审批")

        self.assertEqual("待结算审批", globals()["status"], "onedi.admin审核后状态没有改变")

        


if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(reviewProcess5))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    pytest.main(['-k', "test_reviewProcess5"])