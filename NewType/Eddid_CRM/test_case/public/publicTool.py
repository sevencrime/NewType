#!/usr/bin/env python
# -*- coding: utf-8 -*-



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Commons import BasePage
from PageElement import LoginPage, MenuListPage, ApplyPage


class publicTool(BasePage.BasePage):

    # 等待CSS.Loading-modal加载完成,防止报错:"Element is not clickable at point (347, 104).
    #   Other element would receive the click: <div class="Loading-modal"></div>"
    def wait_LoadingModal(self):
        login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
        login_page.wait_LoadingModal()


    def LoginCRM(self, user='admin', psw='abcd1234'):

        # self.log.info("实例化LoginPage")
        login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
        # 打开浏览器
        # self.log.info("打开浏览器")
        login_page.open()
        # 输入用户名密码
        # self.log.info("输入用户名密码")
        login_page.input_username(user)
        login_page.input_password(psw)
        # 点击登录
        # self.log.info("点击登录")
        login_page.click_submit()
        publicTool.wait_LoadingModal(self)
        # 断言userid
        # self.assertEqual(user, login_page.show_userid(), "userid与登录账户不一致")
        assert user in login_page.show_userid(), "userid与登录账户不一致"


    def box_alert(self):
        # 买卖杠杆式外汇、黄金、结构性产品及衍生产品并不适合投资目标仅为「利息/股息收入」人士。
        # 校验弹框 alert
        applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")
        boxtext = applypage.box_alert()

        return boxtext


    def click_menulist(self, ul_text, li_text):

        menuListpage = MenuListPage.MenuListPage(self.driver, self.url, "Eddid")
        menuListpage.click_menulist(ul_text, li_text)


    # 警告提示框
    def alertNotification(self):
        applypage = ApplyPage.ApplyPage(self.driver, self.url, "Eddid")
        notificationtext = applypage.alertNotification()

        return notificationtext

