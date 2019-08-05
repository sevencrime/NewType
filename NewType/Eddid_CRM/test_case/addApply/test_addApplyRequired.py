# usr/bin/env python
# -*- coding: utf-8 -*-

import unittest



# import addApplyTool
from test_case.addApply.addApplyTool import addApplyTool


class Test_addApplyRequired(addApplyTool):
    # 开户方式必填框校验

    """
    # 用例: 手机应用程式身份认证--校验银行名称和银行账户号码是否必填
    """
    # @unittest.skip("跳过")
    @addApplyTool.AccountOpeningWay(way="手机应用程式身份验证")
    def test_apply_MobileAuthentication(self):
        self.log.info("正在执行{}函数".format(sys._getframe().f_code.co_name))
        # 填写apply 必填项
        self.RequiredField(applicationFor="个人账户",
                           way="手机应用程式身份验证",
                           type="香港及环球期货账户(保证金)")
        # 点击提交按钮
        self.applySublime()

    """
    # 用例: 电子签名认证--校验电子签名证书栏位是否必填
    """
    @addApplyTool.AccountOpeningWay(way="电子签名认证")
    def test_apply_certificateNb(self):
        self.log.info("正在执行{}函数".format(sys._getframe().f_code.co_name))
        # 填写apply 必填项
        self.RequiredField(applicationFor="个人账户",
                           way="电子签名认证",
                           type="香港及环球期货账户(保证金)")
        # 点击提交按钮
        self.applySublime()

if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader(
    ).loadTestsFromTestCase(addApplyRequired))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
