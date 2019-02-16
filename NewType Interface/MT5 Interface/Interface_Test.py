#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-05 11:19:47
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ***
# @Version : $Id$

import requests



def ChangePassword():

    url = 'http://127.0.0.1:7070/Accounts/ChangePassword'
    data1 = {
        'login' : '266586' ,
        'type' : 'MAIN' , 
        'password' : 'onedi '
    }


    resp = requests.get(url, params=data1)

    # resp = requests.get('http://127.0.0.1:7070/Accounts/ChangePassword?login=266586&type=MAIN&password=onedi123')

    print(resp.status_code)
    print(resp.json())

def CheckPassword():

    url = 'http://127.0.0.1:7070/Accounts/CheckPassword'
    data = {
        'login' : '266586' ,
        'type' : 'MAIN' , 
        'password' : 'onedi123'
    }


    resp = requests.get(url, params=data)

    print(resp.status_code)
    print(resp.json())

def FundWithdraw():

    url = 'http://127.0.0.1:7070/Accounts/FundWithdraw'

    data = {
        'login' : '266586' ,
        'type' : '2' , 
        'money' : '100' ,
        'comment' : '这是备注'
    }

    resp = requests.get(url, params = data)

    print(resp.status_code)
    print(resp.json())


def Register():

    # url = 'http://127.0.0.1:7070/Accounts/Register'
    url = 'http://52.76.254.163:6060/Accounts/Register'

    data = {
        "group": "demo\\test",
        "leverage": 100,
        "name": "abc@123",
        "password": "test12345",
        "passwordInvestor": "test12345",
        "login" : "abc" ,
        "balance" : 10000 , #忽略该参数
        "comment" : "这是注释123@，！" ,
        "address" : "广东省深圳市南山区桑达科技大厦802" ,
        "city" : "广东省深圳市" , 
        "country" : "abc one-123" , 
        "email" : "123" , 
        "isEnabled" : 1 ,
        "isEnabledChangePassword" : True ,
        "isReadOnly" :True ,
        "colorBlue" : 0 , 
        "colorGreen" : 0 ,
        "colorRed" : 255 , 
        "agentAccount" : "onedi" , 
        "phone" : 15089514626 ,
        "phonePassword" : "abc123" ,
        "sendReports" : True,
        "state" : "华南地区" ,
        "status" : "正常" , 
        "zipCode" : "中文可用吗" , 
        "id" : "123456" ,
    }
    proxies = {"http": "127.0.0.1:7070"}
    resp = requests.post(url , data = data, proxies = proxies)

    print(resp.status_code)
    print(resp.json())


if __name__ == "__main__":

    # ChangePassword()
    # CheckPassword()
    # FundWithdraw()
    Register()
