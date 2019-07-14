# usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-03 13:56:31
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import pytest
import unittest
from addApplyTool import addApplyTool
import time
# import addApplyTool


class Test_addApplyAllNotEmpty(addApplyTool):

    # 个人账户和联名账户, 必填项开户
    def test_apply_IndividualNotEmpty(self):
        # 用例: 个人账户--必填参数

        # 填写apply 必填项
        self.RequiredField(applicationFor="个人账户")
        # 点击提交按钮
        self.applySublime()

    def test_apply_JointNotEmpty(self):
        # 用例: 联名账户--必填参数

        self.RequiredField(applicationFor="联名账户")

        # 点击个人账户-提交按钮
        self.applySublime(Jump=False)

        # 进入联名账户表单
        self.JointRequiredField()
        # 点击联名账户-提交
        self.applySublime()

    def test_apply_IndividualAll(self):
        # 用例: Apply开户表单全部字段, 随机输入
        self.RequiredField(applicationFor="个人账户")
        self.NonRequiredField()
        # 点击提交按钮
        self.applySublime()

    def test_apply_JointNotEmpty(self):
        # 用例: 联名账户--全部字段随机输入

        self.RequiredField(applicationFor="联名账户")
        self.NonRequiredField()
        # 点击个人账户-提交按钮
        self.applySublime(Jump=False)

        # 进入联名账户表单
        self.JointRequiredField()
        self.NonJointRequiredField()
        # 点击联名账户-提交
        self.applySublime()


if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApplyRequired))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    pytest.main(["-s", "test_addApplyAllNotEmpty.py"])

