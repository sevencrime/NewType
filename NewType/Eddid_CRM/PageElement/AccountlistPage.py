#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-18 17:49:03
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import BasePage, Logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AccountlistPage(BasePage.BasePage):
    log = Logging.Logs()

    LoadingModal_loc = (By.CSS_SELECTOR, ".Loading-modal")
    importAyers_loc = (By.XPATH, "//button/span[contains(text(),'导入Ayers')]")
    importeSunny_loc = (By.XPATH, "//button/span[contains(text(),'导入eSunny')]")
    importmain_loc = (By.XPATH, "//button/span[contains(text(),'导入主要信息')]")
    importserver_loc = (By.XPATH, "//button/span[contains(text(),'上传到服务器')]")
    uploadAyers_loc = (By.NAME, "file")
    uploadfilename_loc = (By.CSS_SELECTOR, ".el-upload-list__item-name")
    alerttext_loc = (By.CSS_SELECTOR,".el-message")
    dialog_close_loc = (By.CSS_SELECTOR, ".el-dialog__close")

    #等待CSS.Loading-modal加载完成,防止报错:"Element is not clickable at point (347, 104). 
    #   Other element would receive the click: <div class="Loading-modal"></div>"
    def wait_LoadingModal(self):
        WebDriverWait(self.driver, 10, 1).until_not(
            EC.presence_of_element_located(self.LoadingModal_loc))

    def click_importAyers(self):
        return self.find_element(*self.importAyers_loc).click()

    def click_importeSunny(self):
        return self.find_element(*self.importeSunny_loc).click()

    def click_importserver(self):
        return self.find_element(*self.importserver_loc).click()

    def uploadAyers(self):
        # 设置元素display属性
        js = "document.querySelector('.el-upload__input').style.display = 'block';"
        self.script(js)
        return self.find_element(*self.uploadAyers_loc).send_keys(os.path.abspath(os.path.dirname(os.getcwd()))+'/config/Ayers1.xlsx')

    def uploadfilename(self):
        return self.find_element(*self.uploadfilename_loc).text

    def alerttext(self):
        return self.find_element(*self.alerttext_loc).text

    def dialog_close(self):
        return self.find_element(*self.dialog_close_loc).click()


