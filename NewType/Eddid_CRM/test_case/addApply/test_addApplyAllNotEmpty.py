# usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-03 13:56:31
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import time,os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
# import addApplyTool
from addApplyTool import addApplyTool
import unittest, pytest

class Test_addApplyAllNotEmpty(addApplyTool):

    @unittest.skip("暂时跳过")
    # 个人账户和联名账户, 必填项开户
    def test_apply_IndividualNotEmpty(self):
        # 用例: 个人账户--必填参数
        
        # 填写apply 必填项        
        self.RequiredField(applicationFor="个人账户", way="亲临开户", type="香港及环球期货账户(保证金)")
        # 点击提交按钮
        self.applySublime()

    def test_apply_JointNotEmpty(self):
        # 用例: 联名账户--必填参数
        
        self.RequiredField(applicationFor="联名账户", way="亲临开户", type="香港及环球期货账户(保证金)")
        # 点击提交按钮
        self.applypage.click_sublimeApply("提交")
        self.mainpage.wait_LoadingModal()   #loading

        self.JoinRequiredField()
        self.applySublime()


if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApplyRequired))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    pytest.main(["-s", "test_addApplyAllNotEmpty.py"])