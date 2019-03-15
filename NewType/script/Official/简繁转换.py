#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-12 15:41:42
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$


from hanziconv import HanziConv
from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import re


class Contrast:

    url_list = set()    #存放解析的链接

    def __init__(self):
        self.path = 'https://www.eddid.com.hk'
        self.url = '/zh-hant/fund-withdrawal/'
            # 'zh-hant' : 'https://www.eddid.com.hk/zh-hant/new-fund-withdrawal'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'content-type': 'application/x-javascript; charset=utf-8'
        }
        

    def request(self):

        resp = requests.get(self.path+self.url, headers = self.headers)
        # print(resp.text)

        soup = BeautifulSoup(resp.text, 'lxml')
        # 获取所有<a>标签
        tag_a = soup.find_all('a')

        self.Analysis(tag_a)
        # self.comparison(resp)


    # 解析()
    def Analysis(self, taglist):

        temp = []  # 存放筛选后的数据
        # 存放所有的链接
        for i in taglist:
            # 筛选出所有herf
            if i['href'] != '#' and i['href'] != '#top' and \
                i['href'] != self.path + self.url and i['href'] != self.url \
                    and i['href'] not in self.url_list and self.path + i['href'] not in self.url_list:

                if self.path in i['href'] and self.path + i['href']:
                    # print(i['href'])
                    self.url_list.add(i['href'])

                else :
                    # print(i['href'])
                    if 'https://' not in i['href'] and 'http://' not in i['href'] and i['href'] != '':
                        print(self.path + i['href'])
                        self.url_list.add(self.path + i['href'])

        print(self.url_list)

        return self.url_list


    # 对比
    def comparison(self, soup):

        Conversion = ''
        # 获取页面所有文字
        text = re.findall("[\u4e00-\u9fa5]", soup.text)
        # print(text)
        str_text = ''.join(text)
        print(str_text)

        print("\n当前请求为 %s, 执行对比\n" %key)

        # 判断是否简体繁体
        if key == 'zh-hans':
            # 转简体
            Conversion = HanziConv.toSimplified(str_text)

        elif key == 'zh-hant':
            # 转繁体
            Conversion = HanziConv.toTraditional(str_text)


        for i in range(len(str_text)):
            if str_text[i] not in Conversion[i]:
                print("原文字: %s , 翻译后: %s , 所在位置: %s" %(str_text[i], Conversion[i], str_text.find(str_text[i])))



if __name__ == '__main__':
    contrast = Contrast()
    contrast.request()
