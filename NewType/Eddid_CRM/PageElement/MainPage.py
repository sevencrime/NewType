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
from Commons import *
import os
import sys
import time
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))


class MainPage(BasePage.BasePage):
    log = Logging.Logs()

    userid_loc = (By.CSS_SELECTOR, ".el-dropdown-link.el-dropdown-selfdefine ")
    submitbtn_loc = (By.XPATH, "//button/span[contains(text(),'提交审核')]")
    addbtn_loc = (By.XPATH, "//button/span[contains(text(),'新增')]")
    updatebtn_loc = (By.XPATH, "//button/span[contains(text(),'修改')]")
    selectbtn_loc = (By.XPATH, "//button/span[contains(text(),'查看')]")
    StatusSelect_loc = (
        By.XPATH, '//div[@class="el-row"]//div[@class="position-r"]//input')  # 状态下拉框
    LoadingModal_loc = (By.CSS_SELECTOR, ".Loading-modal")

    def get_select(self, text):
        select_loc = (
            By.XPATH, "//div[contains(@style,'position: absolute;')]//li[span[text()='{text}']]".format(text=text))
        select_text = self.find_element(*select_loc).click()
        assert text in select_text.get_attribute("textContent")
        return select_text.get_attribute("textContent")

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
        return tag_text

    def click_submit(self):
        return self.find_element(*self.submitbtn_loc).click()

    def click_add(self):
        return self.find_element(*self.addbtn_loc).click()

    def click_update(self):
        return self.find_element(*self.updatebtn_loc).click()

    def click_select(self):
        return self.find_element(*self.selectbtn_loc).click()

    def click_checkbox(self, email):
        # 点击checkbox
        check_loc = (By.XPATH, '//span[text()={email}]/ancestor::td/preceding-sibling::\
            td[@class="el-table_3_column_37  el-table-column--selection"]//input'.format(email=email))

        self.find_element(*check_loc).click()
