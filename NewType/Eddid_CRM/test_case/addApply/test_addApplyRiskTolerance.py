# usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest
from addApplyTool import addApplyTool
import time
# import addApplyTool


class Test_addApplyRiskTolerance(addApplyTool):
    # 校验风险承受能力,黄金,杠杆,结构性产品

    """
    # 用例: 账户类别分别选择金业,校验风险提示.
    #       风险提示选择 "低"
    """
    @addApplyTool.RiskTolerance(num=2)
    def test_apply_BullionRiskToleranceLow(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="艾德金业现货黄金账户(保证金)")
        self.applySublime()

    """
    # 用例: 账户类别选择黄金账户,校验风险提示.
    #       风险提示选择 "中"
    """
    @addApplyTool.RiskTolerance(num=1)
    def test_apply_BullionRiskToleranceMiddle(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="艾德金业现货黄金账户(保证金)")
        self.applySublime()

    """
    # 用例: 账户类别选择黄金账户,校验风险提示.
    #       风险提示选择 "高"
    """
    @addApplyTool.RiskTolerance(num=0)
    def test_apply_BullionRiskToleranceHigh(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="艾德金业现货黄金账户(保证金)")
        self.applySublime()

    """
    # 用例: 账户类别分别选择杠杆式外汇账户(保证金),校验风险提示.
    #       风险提示选择 "低"
    """
    @addApplyTool.RiskTolerance(num=2)
    def test_apply_LeveragedRiskToleranceLow(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="杠杆式外汇账户(保证金)")
        self.applySublime()

    """
    # 用例: 账户类别选择杠杆式外汇账户(保证金),校验风险提示.
    #       风险提示选择 "中"
    """
    @addApplyTool.RiskTolerance(num=1)
    def test_apply_LeveragedRiskToleranceMiddle(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="杠杆式外汇账户(保证金)")
        self.applySublime()

    """
    # 用例: 账户类别选择杠杆式外汇账户(保证金),校验风险提示.
    #       风险提示选择 "高"
    """
    @addApplyTool.RiskTolerance(num=0)
    def test_apply_LeveragedRiskToleranceHigh(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="杠杆式外汇账户(保证金)")
        self.applySublime()

    """
    # 用例: 选择衍生产品,校验风险提示.
    #       风险提示选择 "低"
    """
    @addApplyTool.RiskTolerance(num=2)
    def test_apply_BuyProductRiskToleranceLow(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="香港及环球证券账户(现金)", 
                           buyProduct=True)
        self.applySublime()

    """
    # 用例: 选择衍生产品,校验风险提示.
    #       风险提示选择 "中"
    """
    @addApplyTool.RiskTolerance(num=1)
    def test_apply_BuyProductRiskToleranceMiddle(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="香港及环球证券账户(现金)",
                           buyProduct=True)
        self.applySublime()

    """
    # 用例: 选择衍生产品,校验风险提示.
    #       风险提示选择 "高"
    """
    @addApplyTool.RiskTolerance(num=0)
    def test_apply_BuyProductRiskToleranceHigh(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户", 
                           type="香港及环球证券账户(现金)",
                           buyProduct=True)
        self.applySublime()


if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApplyRiskTolerance))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # pytest.main(["-s", "test_addApplyRiskTolerance.py", "--html=report.html"])
    pytest.main(["-s", "test_addApplyRiskTolerance.py"])
