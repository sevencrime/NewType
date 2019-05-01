#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-22 15:36:51
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$


import poplib
import base64
from email.parser import Parser
import email
import time
import datetime
import os


class Analysis_Mail():

    pop_server = "imap.sina.cn"  # pop服务器
    username = "15089514626@sina.cn"
    password = "Abcd1234"

    def cmps(self, s):
        # base64用decode_header解码
        scode = email.header.decode_header(s)
        try:
            return scode[0][0].decode('utf-8')
        except AttributeError:
            return s

    def get_details(self, msg):
        # 处理邮件头
        fromstr = msg.get('From')
        from_name, from_url = email.utils.parseaddr(fromstr)

        date = msg.get('Date')
        timeReceive = (datetime.datetime.strptime(
            date[:-5], '%a, %d %b %Y %H:%M:%S ') + datetime.timedelta(hours=(8-int(date[-5:]))))

        tosrt = msg.get('To')

        subjectstr = msg.get('Subject')

        return self.cmps(from_name), self.cmps(from_url), self.cmps(timeReceive), self.cmps(tosrt), self.cmps(subjectstr)

    def login(self):
        server = poplib.POP3(self.pop_server)  # 链接服务器
        # server.set_debuglevel(1)    #可选项,打印客户端和服务端的交互信息
        print(server.getwelcome().decode('utf-8'))  # 打印服务器的欢迎信息,验证是否连接成功

        # 身份验证
        server.user(self.username)
        server.pass_(self.password)

        print(server.stat())  # star()返回邮件总数和总大小

        # server.list():
        resp, mails, octets = server.list() #返回响应信息, 所有邮件简要信息, 邮件大小, 返回tuple

        print("邮件总数为:", len(mails))

        for mail_index in reversed(range(1, len(mails)+1)):  # 从最新一封邮件开始遍历

            up_resp, up_mail, up_octets = server.retr(mail_index)   #拿到每一封邮件, 返回tuple

            msg_content = b'\r\n'.join(up_mail).decode('utf-8')    #up_mail存储原始邮件的每一行,通过\r\n连接
            # print(msg_content)

            msg = Parser().parsestr(text=msg_content)   #Parser解析邮件
            # print(msg)

            from_name, from_url, timeReceive, to, sub = self.get_details(msg)   #解析邮件信息头

            if timeReceive.strftime("%Y%m%d") != time.strftime("%Y%m%d", time.localtime(time.time())):
                # 只读取当天的邮件
                continue

            for par in msg.walk():  #以深度优先的遍历顺序迭代消息对象树的所有部分和子部分
                if not par.is_multipart():  #判断是否EmailMessage对象
                    print("111111111111111111111111111")
                    annex = par.get_param("name")  # 获取附件名
                    if annex:
                        h = email.header.Header(annex)
                        dh = email.header.decode_header(h)
                        fname = dh[0][0]
                        print("附件名:", fname)
                        data = par.get_payload(decode=True)
                        print(data, "333333333333333333333333333")

                    else:
                        print("elseesleelse")
                        data = par.get_payload(decode=True)
                        # print(data,"4444444444444444444444444")
                        print(data.decode('utf-8'), "55555555555555555555555")
                        if '<html>' in data.decode('utf-8'):

                            mik_dir = os.getcwd()+'\\mail_TMPL\\%s_now%s' % (
                                timeReceive.strftime("%Y_%m_%d"), time.strftime("%Y%m%d%H", time.localtime(time.time())))
                            if os.path.exists(mik_dir) is False:    # 判断文件目录是否存在
                                os.makedirs(mik_dir)

                            with open(os.getcwd()+'\\mail_TMPL\\%s_now%s\\%s_%s.html' % (
                                timeReceive.strftime("%Y_%m_%d"), time.strftime("%Y%m%d%H", time.localtime(time.time())), 
                                timeReceive.strftime("%Y-%m-%d %H-%M-%S"), sub), 'a', encoding='utf-8') as f:
                                # 写入文件
                                f.write("<!-- %s,  %s -->" % (from_name, from_url))
                                f.write("\n<!--DateTime : %s -->" % timeReceive)
                                f.write("\n<!--To : %s -->" % to)
                                f.write("\n<!--Subject : %s -->\n" % sub)
                                f.write(data.decode('utf-8'))

                                f.close()

        server.close()  # 关闭服务


if __name__ == '__main__':
    getmail = Analysis_Mail()
    getmail.login()
