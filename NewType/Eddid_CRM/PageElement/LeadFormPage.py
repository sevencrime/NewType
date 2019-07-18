#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 15:45:32
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

# main/apply-list页面

import os
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Commons import Logging
from Commons.BasePage import BasePage


class LeadFormPage(BasePage.BasePage):
    log = Logging.Logs()

    leadUser = (By.XPATH, '//input[@placeholder="请输入姓氏"]')

