# usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest
from addApplyTool import addApplyTool
import time
# import addApplyTool


class Test_addApplyDerivativeProduct(addApplyTool):
    # 校验衍生产品隐藏框是否必填

    """
    # 用例: 账户类别选择香港及环球证券账户(现金),校验衍生产品是否必填.
    #       衍生产品选择"否"
    """
    @addApplyTool.DerivativeProduct(num=1)
    def test_apply_CashNotDerivativeProduct(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type="香港及环球证券账户(现金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 账户类别选择香港及环球证券账户(现金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露不填
    """
    @addApplyTool.DerivativeProduct(num=0, linkTag=False)
    def test_apply_CashisDerivativeProductNone(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type="香港及环球证券账户(现金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 账户类别选择香港及环球证券账户(现金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露选 "是"
    """
    @addApplyTool.DerivativeProduct(num=0, linknum=0)
    def test_apply_CashisDerivativeProductyes(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type="香港及环球证券账户(现金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 账户类别选择香港及环球证券账户(现金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露选 "否"
    """
    @addApplyTool.DerivativeProduct(num=0, linknum=1)
    def test_apply_CashisDerivativeProductNo(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type="香港及环球证券账户(现金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 账户类别选择香港及环球证券账户(保证金),校验衍生产品是否必填.
    #       衍生产品选择"否"
    """
    @addApplyTool.DerivativeProduct(num=1)
    def test_apply_MarginNotDerivativeProduct(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type="香港及环球证券账户(保证金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 账户类别选择香港及环球证券账户(保证金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露不填
    """
    @addApplyTool.DerivativeProduct(num=0, linkTag=False)
    def test_apply_MarginisDerivativeProductNone(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type="香港及环球证券账户(保证金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 账户类别选择香港及环球证券账户(保证金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露选 "是"
    """
    @addApplyTool.DerivativeProduct(num=0, linknum=0)
    def test_apply_MarginisDerivativeProductyes(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type="香港及环球证券账户(保证金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 账户类别选择香港及环球证券账户(保证金),校验衍生产品是否必填.
    #       衍生产品选择"是", 风险声明披露选 "否"
    """
    @addApplyTool.DerivativeProduct(num=0, linknum=1)
    def test_apply_MarginisDerivativeProductNo(self):

        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type="香港及环球证券账户(保证金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 选择非外汇, 黄金, 不触发衍生产品 ,校验衍生产品是否必填.
    """
    def test_apply_PassDerivativeProduct(self):

        accounttype = ["香港股票期权账户(现金)", "香港证券即日买卖账户(保证金)",
                       "香港及环球期货账户(保证金)", "香港期货即日买卖账户(保证金)", "盈透证券综合户口(保证金)"]
        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type=accounttype)
        # 点击提交按钮
        self.applySublime()


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        addApplyDerivativeProduct))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
