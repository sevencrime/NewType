#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time,os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from PageElement import *
from Commons import *
from test_case.Test_Login import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class addApplyTool(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        # self.driver.implicitly_wait(30)   

    def tearDown(self):
        time.sleep(20)
        print("结束用例")
        self.driver.quit()

    def precondition(self):
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(3)
        self.url = 'http://eddid-bos-uat.ntdev.be'

        self.MenuListPage = MenuListPage.MenuListPage(self.driver, self.url, "Eddid")
        self.mainpage = MainPage.MainPage(self.driver, self.url, "Eddid")
        self.applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")

        Test_Login.LoginCRM(self)
        self.MenuListPage.click_menulist("开户管理", "开户列表")
        #等待
        self.mainpage.wait_LoadingModal()
        #点击新增按钮
        self.mainpage.click_add()


    """
    开户方式装饰器
    用于校验开户方式所触发的隐藏框是否必填
    """
    def AccountOpeningWay(way):
        # 把开户方法变成装饰器实现
        def wrapper(func):
            def inner_wrapper(self):
                # 点击选择开户方法
                accountOpeningWay = self.applypage.send_accountOpeningWay(way)
                assert way in accountOpeningWay

                try:
                    return func(self)   #执行用例
                except AssertionError:
                    # 捕捉断言失败异常AssertionError
                    if way == "手机应用程式身份验证":
                        # 输入银行名称
                        self.applypage.send_appBankName()
                        # 输入银行账户号码
                        self.applypage.send_appBankAccount()
                    if way == "电子签名认证":
                        # 输入电子签名证书号码
                        self.applypage.send_appcertificateNb()

                    #点击提交
                    try:
                        # import pdb; pdb.set_trace()
                        self.applypage.click_sublimeApply("提交")
                        self.mainpage.wait_LoadingModal()   #loading
                        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交表单失败, 页面没有跳转")
                    except AssertionError:
                        # 断言失败, 数据提交失败
                        # 查找是否有数据为空,并打印出为空的栏位
                        self.applypage.apply_error()
                        raise AssertionError("断言失败(可能是接口报错)")

                    except Exception as e:
                        raise e

                except Exception as e:
                    # 查找出报错的位置
                    print(e, "用例 {} 执行失败".format(func.__name__))
                    raise e

                else:
                    print("风险承受能力为低或为中可以提交成功, 用例'{}'执行失败".format(func.__name__))
                    raise AttributeError("用例 {} , 测试结果为失败".format(func.__name__))   #只抛出异常

            return inner_wrapper
        return wrapper

    # 衍生产品隐藏框
    # 用于校验触发该隐藏框后是否必填
    def DerivativeProduct(num=None, linkTag=False, linknum=None):

        def wrapper(func):
            def inner_wrapper(self, *args, **kwargs):
                try:
                    return func(self, *args, **kwargs)
                except AssertionError:
                    # import pdb; pdb.set_trace()
                    # 断言错误,提交失败,输入衍生产品隐藏框后再次点击提交按钮
                    # 输入衍生产品隐藏框
                    # import pdb; pdb.set_trace()
                    self.applypage.buyProduct(num, linkTag, linknum)
                    try:
                        # import pdb; pdb.set_trace()
                        self.applypage.click_sublimeApply("提交")
                        self.mainpage.wait_LoadingModal()   #loading
                        self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交表单失败, 页面没有跳转")
                    except AssertionError:
                        # 断言失败, 数据提交失败
                        # 查找是否有数据为空,并打印出为空的栏位
                        self.applypage.apply_error()
                        raise AssertionError("断言失败(可能是接口报错)")


                    except Exception as e:
                        raise e

                except Exception as e:
                    # 查找出报错的位置
                    print(e, "用例 {} 执行失败".format(func.__name__))
                    raise e

                else:
                    print("风险承受能力为低或为中可以提交成功, 用例'{}'执行失败".format(func.__name__))
                    raise AttributeError("用例 {} , 测试结果为失败".format(func.__name__))   #只抛出异常

            return inner_wrapper
        return wrapper


    # 风险承受能力装饰器
    def RiskTolerance(num=None):

        def wrapper(func):
            def inner_wrapper(self, *args, **kwargs):
                try:
                    return func(self, *args, **kwargs)
                except AssertionError:
                    # 风险承受能力
                    try:
                        # 输入风险承受能力
                        riskTolerance = self.applypage.riskTolerance(num)
                        if num == 0:
                            # 风险承受能力选择为"高"
                            self.applypage.click_sublimeApply("提交")
                            self.mainpage.wait_LoadingModal()   #loading
                            self.assertEqual(self.driver.current_url, 'http://eddid-bos-uat.ntdev.be/main/apply-list', "提交表单失败, 页面没有跳转")

                    except AttributeError:
                        print("点击风险承受能力方法有异常, 请优化方法")
                        raise AttributeError

                    except AssertionError:
                        # 断言失败, 数据提交失败
                        # 查找是否有数据为空,并打印出为空的栏位
                        self.applypage.apply_error()
                        raise AssertionError("断言失败(可能是接口报错)")


                except Exception as e:
                    # 查找出报错的位置
                    print(e, "用例 {} 执行失败".format(func.__name__))
                    raise e

                else:
                    print("风险承受能力为低或为中可以提交成功, 用例'{}'执行失败".format(func.__name__))
                    raise AttributeError("用例 {} , 测试结果为失败".format(func.__name__))   #只抛出异常

            return inner_wrapper
        return wrapper





