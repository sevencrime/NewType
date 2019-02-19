#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 15:45:32
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

# main/apply-list页面

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import BasePage, Logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MainPage(BasePage.BasePage):
    log = Logging.Logs()

    userid_loc = (By.CSS_SELECTOR, ".el-dropdown-link.el-dropdown-selfdefine ")
    submit_loc = (By.XPATH, "//button/span[contains(text(),'提交审核')]")
    add_loc = (By.XPATH, "//button/span[contains(text(),'新增')]")
    update_loc = (By.XPATH, "//button/span[contains(text(),'修改')]")
    select_loc = (By.XPATH, "//button/span[contains(text(),'查看')]")
    StatusSelect_loc = (By.XPATH, '//*[@id="main"]/div[1]/div[1]/div[1]/div/div/div/input')
    # StatusSelect_loc = (By.XPATH, "//input[@placeholder='请选择']")
    StatusOption_loc = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]')
    LoadingModal_loc = (By.CSS_SELECTOR, ".Loading-modal")
    
    #等待CSS.Loading-modal加载完成,防止报错:"Element is not clickable at point (347, 104). 
    #   Other element would receive the click: <div class="Loading-modal"></div>"
    def wait_LoadingModal(self):
        WebDriverWait(self.driver, 10, 0.5).until_not(
            EC.presence_of_element_located(self.LoadingModal_loc))

    def show_userid(self):
        return self.find_element(*self.userid_loc).text

    def click_StatusSelect(self):
        return self.find_element(*self.StatusSelect_loc).click()

    def click_StatusOption(self):
        return self.find_element(*self.StatusOption_loc).click()

    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

    def click_add(self):
        return self.find_element(*self.add_loc).click()

    def click_update(self):
        return self.find_element(*self.update_loc).click()

    def click_select(self):
        return self.find_element(*self.select_loc).click()

