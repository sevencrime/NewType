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
import chardet


class Analysis_Mail():

    num = 0

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
        except UnicodeDecodeError:
            return scode[0][0].decode('gbk')

    def get_details(self, msg):
        # import pdb
        # pdb.set_trace()
        # 处理邮件头
        fromstr = msg.get('From')
        from_name, from_url = email.utils.parseaddr(fromstr)

        date = msg.get('Date')
        timeReceive = (datetime.datetime.strptime(
            date[:-5], '%a, %d %b %Y %H:%M:%S ') + datetime.timedelta(hours=(8-int(date[-5:-2]))))

        tosrt = msg.get('To')
        to_name, to_url = email.utils.parseaddr(tosrt)

        subjectstr = msg.get('Subject')

        return self.cmps(from_name), self.cmps(from_url), timeReceive, self.cmps(to_name), self.cmps(to_url), self.cmps(subjectstr)

    def login(self):
        server = poplib.POP3(self.pop_server)  # 链接服务器
        # server.set_debuglevel(1)    #可选项,打印客户端和服务端的交互信息
        print(server.getwelcome().decode('utf-8'))  # 打印服务器的欢迎信息,验证是否连接成功

        # 身份验证
        server.user(self.username)
        server.pass_(self.password)

        # print(server.stat())  # star()返回邮件总数和总大小

        # server.list():
        resp, mails, octets = server.list() #返回响应信息, 所有邮件简要信息, 邮件大小, 返回tuple

        print("邮件总数为:", len(mails))

        for mail_index in reversed(range(1, len(mails)+1)):  # 从最新一封邮件开始遍历邮件

            self.num += 1
            if self.num > 1 :
                print("一个一个一个一个")
                break

            up_resp, up_mail, up_octets = server.retr(mail_index)   #拿到每一封邮件信息, 返回tuple

            msg_content = b'\r\n'.join(up_mail).decode('utf-8')    #通过\r\n连接拼接原始邮件

            msg = Parser().parsestr(text=msg_content)   #emali.Parser解析邮件,返回Message Obj
            # print(msg)

            code = self.analysisMessage(msg)   
            # code = True : 当天邮件已读取完成

            if code:
                break


        server.close()  # 关闭服务

    # 解析email.message
    def analysisMessage(self, msg):

        from_name, from_url, timeReceive, to_name, to_url, sub = self.get_details(msg)   #解析邮件信息头

        if timeReceive.strftime("%Y%m%d") != time.strftime("%Y%m%d", time.localtime(time.time())):
            # 只读取当天的邮件
            print("收件箱已经没有当天的邮件,结束程序")
            return True

        for part in msg.walk():  # 遍历邮件的每一部分,返回Ture表示可继续迭代

            if not part.is_multipart():  # 判断内容是否EmailMessage对象,fales为str对象
                annex = part.get_param("name")  # 获取附件名
                if annex:
                    h = email.header.Header(annex)
                    fname = self.cmps(h)
                    print("附件名:", fname)
                    data = part.get_payload(decode=True)
                    data_code = chardet.detect(data)
                    print(data.decode(data_code['encoding']), "333333333333333333333333333")
                    with open(os.getcwd()+'\\mail_TMPL\\%s_now%s\\%s_%s.html' % (
                        timeReceive.strftime("%Y_%m_%d"), time.strftime("%Y%m%d", time.localtime(time.time())), 
                        timeReceive.strftime("%H%M%S"), ''.join(title for title in sub if title.isalnum())), 
                        'a+', encoding='utf-8') as f:
                        f.write('\n\n<!--附件名: %s-->' %fname)
                        f.write('\n<!--\n %s \n-->' %data.decode(data_code['encoding']))


                else:
                    print("elseesleelse")
                    # import pdb
                    # pdb.set_trace()
                    data = part.get_payload(decode=True)
                    # print(data,"4444444444444444444444444")
                    data_code = chardet.detect(data)
                    print(data.decode(data_code['encoding']), "55555555555555555555555")
                    # if '<html>' in data.decode('utf-8'):
                    if part.get_content_type() == 'text/html':

                        mik_dir = os.getcwd()+'\\mail_TMPL\\%s_now%s' % (
                            timeReceive.strftime("%Y_%m_%d"), time.strftime("%Y%m%d", time.localtime(time.time())))
                        if os.path.exists(mik_dir) is False:    # 判断文件目录是否存在
                            os.makedirs(mik_dir)

                        # import pdb 
                        # pdb.set_trace()
                        with open(os.getcwd()+'\\mail_TMPL\\%s_now%s\\%s_%s.html' % (
                            timeReceive.strftime("%Y_%m_%d"), time.strftime("%Y%m%d", time.localtime(time.time())), 
                            timeReceive.strftime("%H%M%S"), ''.join(title for title in sub if title.isalnum())), 
                            'a+', encoding='utf-8') as f:
                            # 写入文件
                            f.write("<!-- %s,  %s -->" % (from_name, from_url))
                            f.write("\n<!--DateTime : %s -->" % timeReceive)
                            f.write("\n<!--To : %s , %s -->" % (to_name, to_url))
                            f.write("\n<!--Subject : %s -->\n" % sub)
                            f.write(data.decode(data_code['encoding']))
                            f.close()
            else:
                # EmailMessage对象,重新解析
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")




if __name__ == '__main__':
    getmail = Analysis_Mail()
    getmail.login()
