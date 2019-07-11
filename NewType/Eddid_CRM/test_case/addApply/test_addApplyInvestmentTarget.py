# usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest
from addApplyTool import addApplyTool
import time
# import addApplyTool


class Test_addApplyInvestmentTarget(addApplyTool):
    # 校验投资目标: 选择杠杆式外汇, 黄金, 结构性衍生产品后, 投资目标不能单独选利息/股息收入

    """
    # 用例: 账户类别分别选择金业,校验投资目标为利息/股息收入是否校验
    """
    addApplyTool.InvestmentTarget()
    def test_apply_BullionInvestmentTarget(self):
        # 填写Apply表单必填项
        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="艾德金业现货黄金账户(保证金)", 
                           investmentTarget="利息/股息收入")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 账户类别分别选择杠杆式外汇账户(保证金,校验投资目标为利息/股息收入是否校验
    """
    addApplyTool.InvestmentTarget()
    def test_apply_BullionInvestmentTarget(self):
        # 填写Apply表单必填项
        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="杠杆式外汇账户(保证金", 
                           investmentTarget="利息/股息收入")
        # 点击提交按钮
        self.applySublime()

   """
    # 用例: 账户类别分别选择衍生产品,校验投资目标为利息/股息收入是否校验
    """
    addApplyTool.InvestmentTarget()
    def test_apply_BullionInvestmentTarget(self):
        # 填写Apply表单必填项
        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="香港及环球证券账户(现金)", 
                           buyProduct = True,
                           investmentTarget="利息/股息收入")
        # 点击提交按钮
        self.applySublime()



if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApplyRiskTolerance))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # pytest.main(["-s", "test_addApplyRiskTolerance.py", "--html=report.html"])
    pytest.main(["-s", "test_addApplyInvestmentTarget.py"])
