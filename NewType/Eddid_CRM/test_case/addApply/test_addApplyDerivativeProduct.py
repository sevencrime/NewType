# usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


# import addApplyTool
from test_case.addApply.addApplyTool import addApplyTool


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

        accounttype = ["香港股票期权账户(现金)", "香港及环球期货账户(保证金)",
                       "香港期货即日买卖账户(保证金)", "杠杆式外汇账户(保证金)", "艾德金业现货黄金账户(保证金)"]
        self.RequiredField(applicationFor="个人账户",
                           way="亲临开户",
                           type=accounttype)
        # 点击提交按钮
        self.applySublime()


    """
    # 用例: 个人账户 >>  客户是否申请开通买卖衍生权证、牛熊证及结构性等产品选择"是"
                        结构性产品相关风险声明披露选择"是"
    #       联名账户 >>  客户是否申请开通买卖衍生权证、牛熊证及结构性等产品选择"是"
                        结构性产品相关风险声明披露选择"是"

            结果: 开户成功, 不会弹出提示框
    """
    def test_apply_jointDerivativeProductsameyes(self):
        # 个人账户, 衍生产品选择是
        self.RequiredField(applicationFor="联名账户",
                           way="亲临开户",
                           type="香港及环球证券账户(保证金)", 
                           buyProduct = True, 
                           num = 0,
                           linknum = 0
                           )

        # 点击提交按钮
        self.applySublime(Jump=False)
        # 填写联名账户
        self.JointRequiredField(buyProduct=True, num=0, linknum=0)
        # 提交
        self.applySublime()


    """
    # 用例: 个人账户 >>  客户是否申请开通买卖衍生权证、牛熊证及结构性等产品选择"是"
                        结构性产品相关风险声明披露选择"是"
    #       联名账户 >>  客户是否申请开通买卖衍生权证、牛熊证及结构性等产品选择"否"

            结果: 联名账户弹出提示, 个人账户和联名账户应保持一致
    """
    def test_apply_jointDerivativeProductDiffyes(self):
        # 个人账户, 衍生产品选择是
        self.RequiredField(applicationFor="联名账户",
                           way="亲临开户",
                           type="香港及环球证券账户(保证金)", 
                           buyProduct = True, 
                           num = 0,
                           linknum = 0,
                           alert = True
                           )

        # 点击提交按钮
        self.applySublime(Jump=False)
        # 填写联名账户
        self.JointRequiredField(buyProduct=True, num=1, linknum=None)
        # 提交
        self.applySublime()


    """
    # 用例: 个人账户 >>  客户是否申请开通买卖衍生权证、牛熊证及结构性等产品选择"否"
                        结构性产品相关风险声明披露 不触发
    #       联名账户 >>  客户是否申请开通买卖衍生权证、牛熊证及结构性等产品选择"否"

            结果: 开户成功, 不会弹出提示框
    """
    def test_apply_jointDerivativeProductsameno(self):
        # 个人账户, 衍生产品选择是
        self.RequiredField(applicationFor="联名账户",
                           way="亲临开户",
                           type="香港及环球证券账户(保证金)", 
                           buyProduct = True, 
                           num = 1,
                           linknum = None
                           )

        # 点击提交按钮
        self.applySublime(Jump=False)
        # 填写联名账户
        self.JointRequiredField(buyProduct=True, num=1, linknum=None)
        # 提交
        self.applySublime()


    """
    # 用例: 个人账户 >>  客户是否申请开通买卖衍生权证、牛熊证及结构性等产品选择"否"
                        结构性产品相关风险声明披露 不触发
    #       联名账户 >>  客户是否申请开通买卖衍生权证、牛熊证及结构性等产品选择"是"

            结果: 联名账户弹出提示, 个人账户和联名账户应保持一致
    """
    def test_apply_jointDerivativeProductDiffno(self):
        # 个人账户, 衍生产品选择是
        self.RequiredField(applicationFor="联名账户",
                           way="亲临开户",
                           type="香港及环球证券账户(保证金)", 
                           buyProduct = True, 
                           num = 1,
                           linknum = None,
                           alert = True
                           )

        # 点击提交按钮
        self.applySublime(Jump=False)
        # 填写联名账户
        self.JointRequiredField(buyProduct=True, num=0, linknum=None)
        # 提交
        self.applySublime()




if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(addApplyDerivativeProduct))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    pytest.main("-v -s test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductsame")