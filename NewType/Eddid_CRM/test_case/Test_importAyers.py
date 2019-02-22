#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-16 16:36:44
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import unittest
from selenium import webdriver
import time
import pymongo
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from PageElement.LoginPage import *
from PageElement.ApplyListPage import *
from PageElement.AccountlistPage import *
from Commons import Logging
from Commons import Modify_xls
from Commons import PyMongo

#交易账户列表导入Ayers数据
class importAyers(unittest.TestCase):

    def setUp(self):
        # self.log.info("正在执行Test_Login")

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        self.driver.implicitly_wait(30)
        self.url = 'http://eddid-bos-feature.ntdev.be'

        #在这里先登录
        login_page = LoginPage(self.driver, self.url, "Eddid")
        login_page.open()
        login_page.input_username("admin")
        login_page.input_password("abcd1234")
        login_page.click_submit()
        self.assertEqual("admin", login_page.show_userid(), "userid与登录账户不一致")

    def tearDown(self):
        time.sleep(10)
        print("结束driver")
        self.driver.quit()

    def getNumber(self):
        file_url = os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xls'
        Data = Modify_xls.Modifyxls(file_url).readxls()
        # 判断data,遍历
        if len(Data) == 1:
            for data in Data:
                #导入数据库前先查询数据库,保证数据库没有该记录
                # PyMongo.Pymongo('uat', 'client_info').Client(data['id_code'])
                PyMongo.Pymongo('uat', 'client_info', data).Client()
                # print(data)
                return data

        else:
            pass


    def test_importAyers(self):

        data = self.getNumber()

        applylistpage = ApplyListPage(self.driver, self.url, "Eddid")
        applylistpage.click_account_manager()
        applylistpage.click_accountlist()

        accountpage = AccountlistPage(self.driver, self.url, "Eddid")
        accountpage.wait_LoadingModal()
        accountpage.click_importAyers()
        accountpage.uploadAyers()
        self.assertEqual(accountpage.uploadfilename(),'Ayers1.xls','上传文件不一致')

        accountpage.click_importserver()
        alert_text = accountpage.alerttext()
        self.assertEqual(accountpage.alerttext(), '操作成功', '上传到服务器失败')
        accountpage.dialog_close()

        # 断言
        result = PyMongo.Pymongo('uat', 'client_info', data).Client()
        self.assertIsNotNone(result, "数据已存入数据库")




if __name__ == '__main__':
    # print(os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xls')
    unittest.main()
