#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-15 17:28:41
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

# import requests
# import json

# url = 'https://eddid-api.ntdev.be/eddid-api-uat/client/clientPortalNotification'
# headers = {
#     'Content-Type' : 'application/json' ,
#     'X-Token' : 'eyJraWQiOiJSejNcLzBrMzY0alZZK2NVVUQ4bWpjdEhYdHgrWTNROENNXC9FcG52OGhXbkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YWYzYWRhOS0yZmY5LTQ1MWQtODdkNy0xNjI5ZWVjZWQyNDMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV91OWZ6N2x5b04iLCJjb2duaXRvOnVzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo4MzI0MzE4NjQ2NjY6cm9sZVwvZGV2LWVkZGlkLWNvZ25pdG8tYWRtaW4tcm9sZSJdLCJhdWQiOiI1MTNqZmNrdHIxbTZldm9nZnF1N29zazdwYSIsImV2ZW50X2lkIjoiMGUwNDcxZTMtNGExZC0xMWU5LWE0NjAtYzM3N2M5MzRlYWU0IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NTI5ODI0MjYsImV4cCI6MTU1Mjk5NDIzMywiaWF0IjoxNTUyOTkwNjMzLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbjEyM0BxcS5jb20ifQ.ZbfZkl5R39wyAtOHqM4TMYDMW5Q0aI_HoSdewIlfPFwhWd_NbyvPbELPswvStEtpyRo3wJr1u7EOR9fu8gkGTbFm4E2RSLxboRAz1WmrZdtzQC3yEEOIS6fN9XbPbAVyW8KoEzEi71I5NyTXaQtNU5RwD1gt1aNvv_AfBJ-dOEjVhEfXwvMrQCutO1kqJKVazf4g8EpSC3JGDHpcMkLY5PqiIunMpPNDx7JiCDa_XqgMWkc71UgFoLDJlZWAf9tzSQ_Dgw0-rSPlRawI0PIH0c12xaznDcjvImNa0qCJuLQs0WdHf6FxG_oZpcAsgLj8jGOvNK9-I5SfaFLodQ9jjA'
# }


# resp = requests.post(url, headers = headers, verify=False)
# print(resp)
# print(resp.json())


import sys
import inspect
 
def my_name():
    print ('1' ,sys._getframe().f_code.co_name)
    print ('2' ,inspect.stack()[0][3])
 
def get_current_function_name():
    print ('5', sys._getframe().f_code.co_name)
    return inspect.stack()[1][3]
class MyClass:
    def function_one(self):
        print ('3',inspect.stack()[0][3])
        print ('4', sys._getframe().f_code.co_name)
        print ("6 %s.%s invoked"%(self.__class__.__name__, get_current_function_name()))
 
if __name__ == '__main__':
    my_name()
    myclass = MyClass()
    myclass.function_one()









