#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2019-03-12 15:41:42
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$


from hanziconv import HanziConv
from googletrans import Translator
from bs4 import BeautifulSoup
from requests.packages import urllib3
from multiprocessing import Pool
import requests
import re


class Contrast:
    url_list = set()    #存放解析的链接
    existed_url = set() #存放已经爬过的链接
    num = 0

    def __init__(self, path):
        self.path = path
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'content-type': 'application/x-javascript; charset=utf-8'
        }
        

    def request(self, url):

        try:
            print("正在请求链接: ", url)
            urllib3.disable_warnings()  #忽略https没有ssl证书的警告
            self.resp = requests.get(url, headers = self.headers, verify=False)

            soup = BeautifulSoup(self.resp.content.decode('UTF-8', 'ignore'), 'lxml')
            print(soup.title.string)
            # self.comparison(soup, url)

            # 获取所有<a>标签
            tag_a = soup.find_all('a')
            self.Analysis(tag_a)

        except Exception as e:
            print(e,u"\n请求失败,跳过此链接")

    # 解析()
    def Analysis(self, taglist):

        temp = []  # 存放筛选后的数据
        # 存放所有的链接
        for i in taglist:
            # 筛选出所有herf
            if i['href'] != '#' and i['href'] != '#top' and i['href'] not in self.url_list and \
                self.path + i['href'] not in self.url_list:
                # print(i['href'])
                if self.path in i['href'] and re.findall("(.jpeg|.exe|.apk|.jpg|.png|.pdf)$", i['href']) == []:
                    # print(i['href'])
                    self.url_list.add(i['href'])

                else :
                    # print(i['href'])
                    if 'https://' not in i['href'] and 'http://' not in i['href'] and i['href'] != ''\
                        and re.findall("(.jpeg|.exe|.apk|.jpg|.png|.pdf)$", i['href']) == []:
                        # print(self.path + i['href'])
                        self.url_list.add(self.path + i['href'])

        print(len(self.url_list), "  url_list ")

        # for link in self.url_list:
        #     # print(link)
        #     if link not in self.existed_url:
        #         self.existed_url.add(link)  
        #         print(len(self.existed_url), "ssss")
        #         self.request(link)
        return self.url_list

    # 对比
    def comparison(self, soup, url):

        Conversion = ''
        # 获取页面所有文字
        text = re.findall("[\u4e00-\u9fa5]", soup.get_text())
        # print(text)
        str_text = ''.join(text)
        # print(str_text)

        # 判断是否简体繁体
        if 'zh-hans' in url:
            # 转简体
            Conversion = HanziConv.toSimplified(str_text)
        elif 'zh-hant' in url:
            # 转繁体
            Conversion = HanziConv.toTraditional(str_text)
        else:
            print("该链接没有简繁之分")

        for i in range(len(str_text)):
            if str_text[i] not in Conversion[i]:
                print("原文字: %s , 翻译后: %s , 所在位置: %s" %(str_text[i], Conversion[i], str_text.find(str_text[i])))


if __name__ == '__main__':
    path = 'https://www.eddid.com.hk'
    url = 'https://www.eddid.com.hk/zh-hant/fund-withdrawal/'
    existed_url = set()
    contrast = Contrast(path)
    url_list = contrast.request(url)

    p = Pool(6)
    for link in url_list:
        # print(link)
        if link not in existed_url:
            existed_url.add(link)  
            print(len(existed_url), "ssss")
            # request(link)
            p.apply_async(contrast.request,args=(link,))

    p.close()
    p.join()









