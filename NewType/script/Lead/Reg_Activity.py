#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-07 11:21:37
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import datetime , time
import json
from selenium import webdriver

class Reg_Activity():

    def __init__(self):
        self.path = 'https://eddid-api.ntdev.be/eddid-api-feature'
        self.headers = {
            'Content-Type' : 'application/json' ,
            'x-api-key' : 'sTCVd81kAq2MgztGZuBLf8h2RDJ4Yvm38zVWUrYe'
        }

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.get('http://mail.tom.com/')
        self.driver.maximize_window()


    def get_List(self):
        url = self.path + '/public/leadDistribute/list'
        data = {
            "sortKey": "date",
            "sortVal": "ASC",
            "searchKey": "",
            "searchVal": "",
            "offset": 0,
            "limit": 10,
            "startDate": datetime.datetime.now().strftime("%Y-%m-%d"),
            "endDate": (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        }

        resp = requests.post(url, headers=self.headers, data=json.dumps(data)).json()
        print(resp)
        # print(resp['data']['rows'][0]['_id'])

        return resp['data']['rows'][0]['_id']


    def findSimilarLead(self, _id):
        url = self.path + '/public/lead/findSimilarLead'
        data = {
            "customerSource": "activity",
            "clientArr": [],
            "clientPhoneNumber": [],
            "phoneArr": [],
            "totalPeople": 1,
            "email": "onedi@qq.com",
            "lastName": "Test",
            "firstName": "Test",
            "phoneNumber": 15088886666,
            "activityId": [_id],
            "writtenApplicationMaterials": [],
            "otherInformation": []
        }
        resp = requests.post(url, headers=self.headers, data=json.dumps(data)).json()
        print(resp)

    def login(self, username, password):
        # 等待页面完全加载
        self.driver.implicitly_wait(30)

        # 使用driver将账号密码填进表单并提交
        user = self.driver.find_element_by_id("username").send_keys(username)
        # js = "document.getElementById('password').style.display='block';"
        # self.driver.execute_script(js)
        psw = self.driver.find_element_by_id("password").click()
        psw = self.driver.find_element_by_id("password").send_keys(password)


        # login = self.driver.find_element_by_class_name('.mail_login_btn4').click()



if __name__ == '__main__':

    reg = Reg_Activity()
    # _id = reg.get_List()
    # reg.findSimilarLead(_id)

    username = "sevencrime77"
    password = "abcd1234"
    reg.login(username, password)

