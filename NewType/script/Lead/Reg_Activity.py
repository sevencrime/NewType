#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-07 11:21:37
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import datetime
import json
from selenium import webdriver
import 

class Reg_Activity():

    def __init__(self):
        self.path = 'https://eddid-api.ntdev.be/eddid-api-feature'
        self.headers = {
            'Content-Type' : 'application/json' ,
            'x-api-key' : 'sTCVd81kAq2MgztGZuBLf8h2RDJ4Yvm38zVWUrYe'
        }

        self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.get('http://mail.163.com/')


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
            "lastName": "last",
            "firstName": "first",
            "phoneNumber": 15088886666,
            "activityId": ["5c808d499683f8309d18b972"],
            "writtenApplicationMaterials": [],
            "otherInformation": []
        }
        resp = requests.post(url, headers=self.headers, data=json.dumps(data)).json()
        print(resp)

    def login(self, username, password):
        # 等待页面完全加载
        self.driver.implicitly_wait(30)

        # 因为163登录入口在iframe里面，所以先要切换到iframe
        frame = self.driver.find_element_by_id('x-URS-iframe')
        self.driver.switch_to.frame(frame)

        # 使用driver将账号密码填进表单并提交
        email = self.driver.find_element_by_xpath("//input[@name='email']").send_keys(username)
        pwd = self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        login = self.driver.find_element_by_id('dologin').click()



if __name__ == '__main__':
    reg = Reg_Activity()
    _id = reg.get_List()
    reg.findSimilarLead(_id)

    username = "17620446727@163.com"
    password = ""
    reg.login(" ", " ")

