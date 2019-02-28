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
        self.url = 'http://eddid-bos-uat.ntdev.be'

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
        file_url = os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xlsx'
        data = Modify_xls.Modifyxls(file_url).readxls()
        print(data[0]['id_code'], data[0]['email'])
        #导入数据库前先查询数据库,保证数据库没有该记录
        result = PyMongo.Pymongo().Find({'idNumber': str(data[0]['id_code']), 'email': str(data[0]['email'])})
        # res = [r for r in result]
        # print(res)
        if [r for r in result] != []:
            print("数据已存在,修改id_code和email数据")
            # id_code = Modify_xls.Modifyxls(file_url).writexls()
            # print("修改后的id_code为:" ,id_code)
            PyMongo.Pymongo().Del({'idNumber': str(data[0]['id_code']), 'email': str(data[0]['email'])})

        return data

    def test_importAyers(self):

        data = self.getNumber()
        print(data)
        applylistpage = ApplyListPage(self.driver, self.url, "Eddid")
        applylistpage.click_account_manager()
        applylistpage.click_accountlist()

        accountpage = AccountlistPage(self.driver, self.url, "Eddid")
        accountpage.wait_LoadingModal()
        accountpage.click_importAyers()
        accountpage.uploadAyers()
        self.assertEqual(accountpage.uploadfilename(),'Ayers1.xlsx','上传文件不一致')

        accountpage.click_importserver()
        alert_text = accountpage.alerttext()
        self.assertEqual(accountpage.alerttext(), '操作成功', '上传到服务器失败')
        accountpage.dialog_close()

        # 断言
        result = PyMongo.Pymongo().Find({'idNumber': str(data[0]['id_code']), 'email': str(data[0]['email'])})
        res = [r for r in result]
        print(res[0])

        self.assertIsNotNone(res[0], "数据已存入数据库")
        self.assertEqual(res[0]['chineseName'], data['big5_name'], "数据不一致")
        self.assertEqual(res[0]['idNumber'], data['id_code'], "数据不一致")
        self.assertEqual(res[0]['email'], data['email'], "数据不一致")
        self.assertEqual(res[0]['phone'], data['phone'], "数据不一致")
        self.assertEqual(res[0]['address'], data['addr'], "数据不一致")
        self.assertEqual(res[0]['nationality'], data['nationality'], "数据不一致")




if __name__ == '__main__':
    # print(os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xls')
    unittest.main()
