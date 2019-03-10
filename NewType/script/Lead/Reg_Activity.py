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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class Reg_Activity():

    def __init__(self):
        self.path = 'https://eddid-api.ntdev.be/eddid-api-uat'
        self.headers = {
            'Content-Type' : 'application/json' ,
            'x-api-key' : 'CCM4cuhy1e2r0XXkbzMuN1A5TiZ0tC6e6mJYKUez'
        }

        # self.driver = webdriver.Chrome(executable_path = 'chromedriver')
        # self.driver.implicitly_wait(30)
        # self.driver.get('http://mail.tom.com/')
        # self.driver.maximize_window()

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
        # print(resp)
        # print(resp['data']['rows'][0]['_id'])
        for lead in resp['data']['rows']:
            if lead['date'] >= datetime.datetime.now().strftime("%Y-%m-%d"):
                print(lead)
                return lead['_id']


    def findSimilarLead(self, _id):
        url = self.path + '/public/lead/findSimilarLead'
        data = {
            "customerSource": "activity",
            "clientArr": [],
            "clientPhoneNumber": [],
            "phoneArr": [],
            "totalPeople": 1,
            "email": "sevencrime77@tom.com",
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

        # 登录邮箱
        user = self.driver.find_element_by_id("username").send_keys(username)
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID, "pw"))).click()
        psw = self.driver.find_element_by_id("password").send_keys(password)
        login = self.driver.find_element_by_class_name('mail_login_btn4').click()
        assert self.driver.find_element_by_class_name('top-account').text == username+'@tom.com'

        # 进入收件箱
        self.driver.find_element_by_id('webmail_sys_readmail').click()

        # page = self.driver.page_source
        # print(page.replace(u'\xa0', u''))

        # 爬虫,抓取收件箱列表
        soup = BeautifulSoup(self.driver.page_source.replace(u'\xa0', u''), 'lxml')
        maillist = soup.select('#main_tmpl_INBOX > .m-maillist > table > tbody > tr')

        # 循环遍历列表,找到邮件
        for i in range(len(maillist)):
            print(maillist[i])
            print(maillist[i]['title'])
            # 通过title初步判断

            # if 活动名 in maillist[i]['title'] and 活动日期 in maillist[i]['title']:
            # 获取发件人和收件时间
            td_list = maillist[i].find_all('td')
            for n in range(len(td_list)):
                # if n == 2:
                #     assert td_list[n].get_text() == 'noreply'
                if n == 4:
                    print(td_list[n].get_text())
                    # 根据时间判断时候是刚收到的邮件

                    # 进入邮件
                    self.driver.find_element_by_xpath(
                        '//tr[@uid=%s]' %(maillist[i]['uid'])).click()

                    # 主题,讲者,日期,时间,预留名额断言
                    # 截图,对比信息
                    # 扫码



        time.sleep(5)
        print("quit driver")
        self.driver.quit()


if __name__ == '__main__':

    reg = Reg_Activity()
    _id = reg.get_List()
    print(_id)
    # reg.findSimilarLead(_id)

    username = "sevencrime77"
    password = "abcd1234"
    # reg.login(username, password)

