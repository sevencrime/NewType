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
import re

class Analysis_Mail():

    sub_dict = {
       'approval' : ['開戶審批待辦事項 (UAT)', 'Account opening approval to-do list (UAT)'],
    }
    


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
            date[:-5], '%a, %d %b %Y %H:%M:%S ') + datetime.timedelta(hours=(8 - int(date[-5:-2]))))

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
        resp, mails, octets = server.list()  # 返回响应信息, 所有邮件简要信息, 邮件大小, 返回tuple

        print("邮件总数为:", len(mails))

        for mail_index in reversed(range(1, len(mails) + 1)):  # 从最新一封邮件开始遍历邮件

            self.num += 1
            up_resp, up_mail, up_octets = server.retr(mail_index)  # 拿到每一封邮件信息, 返回tuple

            msg_content = b'\r\n'.join(up_mail).decode('utf-8')  # 通过\r\n连接拼接原始邮件

            msg = Parser().parsestr(text=msg_content)  # emali.Parser解析邮件,返回Message Obj
            # print(msg)

            try:
                code = self.analysisMessage(msg)
                # code = True : 当天邮件已读取完成
                if code:
                    print("收件箱已经没有当天的邮件")
                    print('截止到 {time_now}, 当天邮件总数为: {num} 封'.format(
                        time_now=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())), num=self.num))
                    break

            except Exception as e:
                print('ERROR', e)
                continue

        print("退出邮件服务器,结束程序")
        server.close()



    # 解析email.message
    def analysisMessage(self, msg):

        from_name, from_url, timeReceive, to_name, to_url, sub = self.get_details(msg)  # 解析邮件信息头

        # 只读取当天的邮件
        if timeReceive.strftime("%Y%m%d") != time.strftime("%Y%m%d", time.localtime(time.time())):
            return True

        # 文件保存路径
        mik_dir = os.getcwd() + '\\mail_TMPL\\{timeReceive}_now{now}'.format(
            timeReceive=timeReceive.strftime("%Y_%m_%d"),
            now=time.strftime("%Y%m%d", time.localtime(time.time())))

        # 判断文件目录是否存在
        if os.path.exists(mik_dir) is False:
            os.makedirs(mik_dir)

        for part in msg.walk():  # 遍历邮件的每一部分,返回Ture表示可继续迭代

            if not part.is_multipart():  # 判断内容是否EmailMessage对象,fales为str对象

                annex = part.get_param("name")  # 获取附件名

                if annex:
                    h = email.header.Header(annex)
                    fname = self.cmps(h)
                    print("附件名:", fname)
                    data = part.get_payload(decode=True)
                    data_code = chardet.detect(data)
                    # print(data.decode(data_code['encoding']), "3333333333333333")

                    with open('{mik_dir}\\{receive_time}_{subject}.html'.format(
                        mik_dir=mik_dir,
                        receive_time=timeReceive.strftime("%H%M%S"),
                        subject=''.join(
                            title for title in sub if title.isalnum())
                        ), 'a+', encoding='utf-8') as f:

                        f.write('\n\n<!--附件名: {fileName}-->'.format(fileName=fname))
                        try:
                            f.write('\n<!--\n {fileNameContent} \n-->'.format(
                                fileNameContent=data.decode(data_code['encoding'])))
                        except UnicodeDecodeError:
                            if data_code['encoding'] == 'GB2312':
                                f.write(data.decode('gbk'))

                else:
                    # print("elseesleelse")
                    data = part.get_payload(decode=True)
                    data_code = chardet.detect(data)
                    # print(data.decode(data_code['encoding']), "555555555555")

                    if part.get_content_type() == 'text/html':
                        with open('{mik_dir}\\{receive_time}_{subject}.html'.format(
                            mik_dir=mik_dir,
                            receive_time=timeReceive.strftime("%H%M%S"),
                            subject=''.join(title for title in sub if title.isalnum())
                            ), 'a+', encoding='utf-8') as f:

                            # 写入文件
                            f.write("<!-- {from_name},  {from_url} -->".format(from_name=from_name, from_url=from_url))
                            f.write("\n<!--DateTime : {timeReceive} -->".format(timeReceive=timeReceive))
                            f.write("\n<!--To : {to_name} , {to_url} -->".format(to_name=to_name, to_url=to_url))
                            f.write("\n<!--Subject : {subject} -->\n".format(subject=sub))
                            # import pdb; pdb.set_trace()
                            try:
                                f.write(data.decode(data_code['encoding']))
                            except UnicodeDecodeError:
                                if data_code['encoding'] == 'GB2312':
                                    f.write(data.decode('gbk'))
                                
                            f.close()

                    elif part.get_content_type() == 'text/plain':

                        # import pdb; pdb.set_trace()

                        # 判断邮件标题
                        if [value for v in self.sub_dict.values() for value in v if sub == value]:

                            data = part.get_payload(decode=True)
                            data_code = chardet.detect(data)
                            try:
                                mContext = data.decode(data_code['encoding'])
                            except UnicodeDecodeError:
                                mContext = data.decode('gbk')

                            # 获取邮件的类型
                            mail_type = "".join([k for k,v in self.sub_dict.items() for value in v if sub == value])

                            if mail_type == 'approval': 
                                roleName = "".join(re.findall(',(.+):', mContext))  #角色名称
                            else:
                                pass

                                



if __name__ == '__main__':
    getmail=Analysis_Mail()
    getmail.login()
