#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 15:45:32
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

# main/apply-list页面

import os
import sys

from Commons import BasePage

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("Eddid_CRM\\")+len("Eddid_CRM\\")]
sys.path.append(rootPath)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import datetime

class ActivityPage(BasePage.BasePage):
    # log = Logging.Logs()

    activityDate_loc = (By.XPATH, "//div[contains(text(), '活动日期')]/following-sibling::span//input")
    activityOpenTime_loc = (By.XPATH, "//div[contains(text(), '活动时间')]/following-sibling::span//input[@placeholder='开始时间']")
    activityEndTime_loc = (By.XPATH, "//div[contains(text(), '活动时间')]/following-sibling::span//input[@placeholder='截止时间']")
    activityTopic_loc = (By.XPATH, "//div[contains(text(), '讲题')]/following-sibling::span//input")
    activitySpeaker_loc = (By.XPATH, "//div[contains(text(), '讲者')]/following-sibling::span//input")
    activityLevel_loc = (By.XPATH, "//div[contains(text(), '等级')]/following-sibling::span//input")
    activityLocation_loc = (By.XPATH, "//div[contains(text(), '地点')]/following-sibling::span//input")
    Promotions_loc = (By.XPATH, "//textarea[@placeholder='请输入优惠活动']")
    BigActivity_loc = (By.XPATH, "//div[contains(text(), '大型活动')]/following-sibling::span//input")
    addressMap_loc = (By.XPATH, "//div[contains(text(), '讲座举办地址图')]/following-sibling::span//input")
    primary_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')
    default_loc = (By.XPATH, '//button[@class="el-button el-button--default"]')

    def get_select(self, text=False, randox=None):
        if not text:
            select_loc = (
                By.XPATH, "//div[contains(@style,'position: absolute;')]//li")

            selectlist = self.find_elements(*select_loc)
            if randox == None:
                randox = random.randint(0, len(selectlist)-1)

            for i in range(len(selectlist)):
                if i == randox:
                    while selectlist[i].is_displayed():
                        self.scrollinto(selectlist[i])
                        # self.script("arguments[0].click();", selectlist[i])

                        try:
                            tag_text = selectlist[i].get_attribute(
                                "textContent")
                            # print(tag_text)
                        except AttributeError:
                            continue

                    return selectlist[i].get_attribute("textContent")

        else:
            select_loc = (By.XPATH, "//span[contains(text(), '%s')]" % text)
            select_value = self.find_element(*select_loc)
            self.scrollinto(select_value)
            return select_value.get_attribute("textContent")


    def send_activityDate(self):
        # 活动日期
        activityDate = self.find_element(*self.activityDate_loc)
        # ,默认创建明天的讲座
        activityDate.send_keys((datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
        activityDate.send_keys(Keys.ENTER)
        assert activityDate.get_attribute("value") != ''
        return activityDate.get_attribute("value")

    def send_activityOpenTime(self):
        # 活动时间
        activityTime = self.find_element(*self.activityOpenTime_loc)
        activityTime.click()
        activityTime.send_keys(Keys.ENTER)
        assert activityTime.get_attribute("value") != ''
        return activityTime.get_attribute("value")

    def send_activityTopic(self):
        # 讲题
        activityTopic = self.find_element(*self.activityTopic_loc)
        activityTopic.send_keys("AUTO_test_Topic")
        assert activityTopic.get_attribute("value") != ''
        return activityTopic.get_attribute("value")

    def activitySpeaker(self):
        # 讲者
        activitySpeaker = self.find_element(*self.activitySpeaker_loc)
        activitySpeaker.send_keys("Auto Speaker")
        assert activitySpeaker.get_attribute("value") != ''
        return activitySpeaker.get_attribute("value")


    def activityLevel(self):
        # 等级
        activityLevel = self.find_element(*self.activityLevel_loc)
        activityLevel.click()
        tag_text = self.get_select()
        assert activityLevel.get_attribute("value") != ''
        return activityLevel.get_attribute("value")


    def activityLocation(self):
        # 地点
        activityLocation = self.find_element(*self.activityLocation_loc)
        activityLocation.send_keys("Auto_Location")
        assert activityLocation.get_attribute("value") != ''
        return activityLocation.get_attribute("value")

    def Promotions(self):
        # 优惠活动
        Promotions = self.find_element(*self.Promotions_loc)
        Promotions.send_keys("优惠活动")
        assert Promotions.get_attribute("value") != ''
        return Promotions.get_attribute("value")

    def BigActivity(self):
        # 大型活动
        BigActivity = self.find_element(*self.BigActivity_loc)
        BigActivity.click()
        tag_text = self.get_select()
        assert BigActivity.get_attribute("value") != ''
        return BigActivity.get_attribute("value")

    def addressMap(self):
        # 讲座举办地址图
        addressMap = self.find_element(*self.addressMap_loc)
        addressMap.send_keys(r"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1563186349289&di=684b3a3041b9d5da513f1430fbecdad8&imgtype=0&src=http%3A%2F%2Fpic39.nipic.com%2F20140319%2F10944729_103257651139_2.jpg")
        assert addressMap.get_attribute("value") != ''
        return addressMap.get_attribute("value")

    def primary(self):
        # 保存
        self.find_element(*self.primary_loc).click()

    def default(self):
        # 取消
        self.find_element(*self.default_loc).click()

