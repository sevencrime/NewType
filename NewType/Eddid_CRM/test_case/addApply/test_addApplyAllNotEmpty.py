# usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-03 13:56:31
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$
import sys

import pytest

# import addApplyTool
from test_case.addApply.addApplyTool import addApplyTool


class Test_addApplyAllNotEmpty(addApplyTool):
    # 个人账户和联名账户, 必填项开户

    # 用例: 个人账户--必填参数
    def test_apply_IndividualNotEmpty(self):
        self.log.info("正在执行{}函数".format(sys._getframe().f_code.co_name))

        # 填写apply 必填项
        self.RequiredField(applicationFor="个人账户",
                           type=["香港及环球证券账户(现金)", "香港及环球期货账户(保证金)", "杠杆式外汇账户(保证金)"])
        # 点击提交按钮
        self.applySublime()

    # 用例: 联名账户--必填参数
    def test_apply_JointNotEmpty(self):
        self.log.info("正在执行{}函数".format(sys._getframe().f_code.co_name))

        self.RequiredField(applicationFor="联名账户",
                           type=["香港及环球证券账户(现金)", "香港及环球期货账户(保证金)", "杠杆式外汇账户(保证金)"])

        # 点击个人账户-提交按钮
        self.applySublime(Jump=False)

        # 进入联名账户表单
        self.JointRequiredField()
        # 点击联名账户-提交
        self.applySublime()

    # 用例: Apply开户表单全部字段, 随机输入
    def test_apply_IndividualAll(self):
        self.log.info("正在执行{}函数".format(sys._getframe().f_code.co_name))
        self.RequiredField(applicationFor="个人账户",
                           type=["香港及环球证券账户(现金)", "香港及环球期货账户(保证金)", "杠杆式外汇账户(保证金)"])
        self.NonRequiredField()
        # 点击提交按钮
        self.applySublime()

    # 用例: 联名账户--全部字段随机输入
    def test_apply_JointNotEmpty(self):
        self.log.info("正在执行{}函数".format(sys._getframe().f_code.co_name))
        self.RequiredField(applicationFor = "联名账户",
                           type = ["香港及环球证券账户(现金)", "香港及环球期货账户(保证金)", "杠杆式外汇账户(保证金)"],
                           buyProduct = True)
        self.NonRequiredField()
        # 点击个人账户-提交按钮
        self.applySublime(Jump=False)

        # 进入联名账户表单
        self.JointRequiredField(buyProduct = True)
        self.NonJointRequiredField()
        # 点击联名账户-提交
        self.applySublime()


if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApplyRequired))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    pytest.main("-s -v --pdb test_addApplyAllNotEmpty.py::Test_addApplyAllNotEmpty::test_apply_IndividualNotEmpty")
