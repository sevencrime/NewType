#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-15 10:52:09
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$



import pytest

from Commons import Logging
from PageElement import ActivityPage
from test_case.test_Login import *
from test_case.public.publicTool import publicTool

# 创建讲座
class Test_createActivity:

    log = Logging.Logs()

    def setup(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver') 
        # self.driver = webdriver.Firefox(executable_path = 'geckodriver')
        # self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(3)
        self.url = 'http://eddid-bos-uat.ntdev.be'

        self.activity = ActivityPage.ActivityPage(self.driver, self.url, "Eddid")

        publicTool.LoginCRM(self)
        
        publicTool.click_menulist(self, "活动管理", "创建讲座")
        # 等待
        publicTool.wait_LoadingModal(self)

    def teardown(self):
        print("用例执行完成")
        self.driver.quit()


    def test_AllCreateActivity(self):
        # 创建活动,全部字段
        # 活动日期
        self.activity.send_activityDate()
        # 活动时间
        self.activity.send_activityOpenTime()
        # 讲题
        self.activity.send_activityTopic()
        # 讲者
        self.activity.activitySpeaker()
        # 等级
        self.activity.activityLevel()
        # 地点
        self.activity.activityLocation()
        # 优惠活动
        self.activity.Promotions()
        # 大型活动
        self.activity.BigActivity()
        # 讲座举办地址图
        self.activity.addressMap()
        # 保存
        self.activity.primary()

        publicTool.box_alert(self)
        publicTool.wait_LoadingModal(self)
        assert self.driver.current_url in "http://eddid-bos-uat.ntdev.be/main/activity-list", "创建活动失败"

    def test_RequiredCreate(self):
        # 创建活动,必填字段
        # 活动日期
        self.activity.send_activityDate()
        # 活动时间
        self.activity.send_activityOpenTime()
        # 讲题
        self.activity.send_activityTopic()
        # 保存提交
        self.activity.primary()
        publicTool.box_alert(self)
        publicTool.wait_LoadingModal(self)
        assert self.driver.current_url in "http://eddid-bos-uat.ntdev.be/main/activity-list", "创建活动失败"

    def test_NonCreateActivity(self):
        # 创建活动,直接点击保存
        self.activity.primary()
        assert self.driver.current_url in "http://eddid-bos-uat.ntdev.be/main/seminar-create", "创建讲座空字段可以提交成功"

if __name__ == '__main__':
    pytest.main("-s -v --pdb test_createActivity.py::Test_createActivity::test_AllCreateActivity")