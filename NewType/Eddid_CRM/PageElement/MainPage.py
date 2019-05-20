#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 15:45:32
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

# main/apply-list页面

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Commons import *
import os
import sys
import time
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))


class MainPage(BasePage.BasePage):
    # log = Logging.Logs()

    userid_loc = (By.CSS_SELECTOR, ".el-dropdown-link.el-dropdown-selfdefine ")
    submitbtn_loc = (By.XPATH, "//button/span[contains(text(),'提交审核')]")
    addbtn_loc = (By.XPATH, "//button/span[contains(text(),'新增')]")
    updatebtn_loc = (By.XPATH, "//button/span[contains(text(),'修改')]")
    selectbtn_loc = (By.XPATH, "//button/span[contains(text(),'查看')]")
    StatusSelect_loc = (By.XPATH, '//div[@class="el-row"]//div[@class="position-r"]//input')  # 状态下拉框
    LoadingModal_loc = (By.CSS_SELECTOR, ".Loading-modal")

    def get_select(self, text):
        select_loc = (
            By.XPATH, "//div[contains(@style,'position: absolute;')]//li[span[contains(text(), '{text}')]]".format(text=text))
        select_text = self.find_element(*select_loc)

        self.scrollinto(select_text)
        assert text in select_text.get_attribute("textContent")
        return select_text.get_attribute("textContent")

    # def scrollinto(self, loc):
    #     self.script("arguments[0].scrollIntoView();", loc)
    #     self.script("arguments[0].click();", loc)

    def Action(self, loc):
        ActionChains(self.driver).double_click(loc).perform()

    def click_checkbox(self, email):
        # 点击checkbox
        check_loc = (By.XPATH, '//span[text()="{email}"]/ancestor::td/preceding-sibling::td[contains(@class, "el-table-column--selection")]//span'.format(email=email))
        self.scrollinto(self.find_element(*check_loc))

    def get_apply(self, email):
        #  双击进入apply详情
        applylistEmali_loc = (By.XPATH, '//span[text()="{email}"]/ancestor::td'.format(email=email))
        applylistEmail = self.find_element(*applylistEmali_loc)
        self.script("arguments[0].scrollIntoView();", applylistEmail)
        self.Action(applylistEmail)

    # 等待CSS.Loading-modal加载完成,防止报错:"Element is not clickable at point (347, 104).
    #   Other element would receive the click: <div class="Loading-modal"></div>"
    def wait_LoadingModal(self):
        WebDriverWait(self.driver, 20).until_not(
            EC.presence_of_element_located(self.LoadingModal_loc))

    def show_userid(self):
        return self.find_element(*self.userid_loc).text

    def click_StatusSelect(self, text):
        statusselect = self.find_element(*self.StatusSelect_loc).click()
        tag_text = self.get_select(text)
        if text == tag_text.strip():
            return tag_text.strip()
        else: 
            self.click_StatusSelect(textt)   

    def click_submitreview(self):
        return self.scrollinto(self.find_element(*self.submitbtn_loc))

    def click_add(self):
        return self.find_element(*self.addbtn_loc).click()

    def click_update(self):
        return self.find_element(*self.updatebtn_loc).click()

    def click_select(self):
        return self.find_element(*self.selectbtn_loc).click()

    def get_status(self, email):
        status_loc = (By.XPATH, '//span[text()="{email}"]/ancestor::td/following-sibling::td[contains(@class, "table-column-status")]//span'.format(email=email))
        return self.find_element(*status_loc).get_attribute("textContent").strip()
        





