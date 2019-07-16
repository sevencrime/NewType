#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("Eddid_CRM\\")+len("Eddid_CRM\\")]
sys.path.append(rootPath)

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Commons import *

class publicTool(BasePage.BasePage):

    # 等待CSS.Loading-modal加载完成,防止报错:"Element is not clickable at point (347, 104).
    #   Other element would receive the click: <div class="Loading-modal"></div>"
    def wait_LoadingModal(self):
        WebDriverWait(self.driver, 20).until_not(
            EC.presence_of_element_located(self.LoadingModal_loc))
