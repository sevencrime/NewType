#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

class Decoration:

    def LoginCRM(driver, user='admin', psw='abcd1234'):
        def wrapper(func):
            @functools.wraps(func)
            def inner_wrapper(self, *args, **kwargs):
                # login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")
                driver.open()
                driver.input_username(user)
                driver.input_password(psw)
                driver.click_submit()
                driver.wait_LoadingModal()
                self.assertEqual(user, driver.show_userid(), "userid与登录账户不一致")
                return func(self, *args, **kwargs)
            return inner_wrapper
        return wrapper


        
