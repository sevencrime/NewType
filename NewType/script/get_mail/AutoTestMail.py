#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-22 15:36:51
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$


import poplib
import smtplib
import base64
import email
from email.parser import Parser
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
import time
import datetime
import os
import chardet
import re
from apscheduler.schedulers.blocking import BlockingScheduler   # apscheduler定时任务框架
from prettytable import PrettyTable     #输出表格库


class AutoTestMail():

    sub_dict = {
        'AccountOpeningApproval': ['开户审批待办事项', '開戶審批待辦事項', 'Account opening approval to-do list'],
        'DailyReport': ['每日开户表汇总', ],
        'LeadForm': ['[電子入場門票]'],
        'LeadFormRemind': ['[講座提醒]'],
        'accountAudit': ['开户申请通知 Account Application Notification', '開戶申請通知 Account Application Notification'],
        'applyemail': ['Online Account Application Approved', '艾德網上開戶申請批核確認', '艾德网上开户申请批核确认'],
        'forCs1Notify': ['Account opening application notice', '开户申请通知书', '開戶申請通知書']
    }

    Role = []  # 存放角色
    DailyReportGB = []  # 每日报表邮件
    LeadFormGB = []  # 登记讲座邮件
    LeadFormRemindGB = []    # 讲座提醒邮件

    num = 0
    pop_server = "imap.sina.cn"  # pop服务器
    smtp_server = "smtp.sina.cn"
    username = "15089514626@sina.cn"
    password = "Abcd1234"
    sendaddr = "onedi@qq.com"

    def cmps(self, s):
        # base64用decode_header解码
        scode = email.header.decode_header(s)
        try:
            return scode[0][0].decode('utf-8')
        except AttributeError:
            return s
        except UnicodeDecodeError:
            return scode[0][0].decode('gbk')

    def set_details(self, s):
        # 转码邮件头
        name, addr = parseaddr(s)
        try:
            return formataddr((Header(name, 'utf-8').encode(), addr))
        except UnicodeDecodeError:
            return formataddr((Header(name, 'gbk')).encode(), addr)

    def get_details(self, msg):
        # 解析处理邮件头
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
            up_resp, up_mail, up_octets = server.retr(
                mail_index)  # 拿到每一封邮件信息, 返回tuple

            msg_content = b'\r\n'.join(up_mail).decode(
                'utf-8')  # 通过\r\n连接拼接原始邮件

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

        from_name, from_url, timeReceive, to_name, to_url, sub = self.get_details(
            msg)  # 解析邮件信息头

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
                    fname = self.cmps(Header(annex))
                    print("附件名:", fname)
                    data = part.get_payload(decode=True)
                    data_code = chardet.detect(data)

                    with open('{mik_dir}\\{receive_time}_{subject}.html'.format(
                        mik_dir=mik_dir,
                        receive_time=timeReceive.strftime("%H%M%S"),
                        subject=''.join(
                            title for title in sub if title.isalnum())
                    ), 'a+', encoding='utf-8') as f:

                        f.write(
                            '\n\n<!--附件名: {fileName}-->'.format(fileName=fname))
                        try:
                            f.write('\n<!--\n {fileNameContent} \n-->'.format(
                                fileNameContent=data.decode(data_code['encoding'])))
                        except UnicodeDecodeError:
                            print("ERROE: UnicodeDecodeError")
                            if data_code['encoding'] == 'GB2312':
                                f.write(data.decode('gbk'))

                else:
                    data = part.get_payload(decode=True)
                    data_code = chardet.detect(data)

                    if part.get_content_type() == 'text/html':
                        with open('{mik_dir}\\{receive_time}_{subject}.html'.format(
                            mik_dir=mik_dir,
                            receive_time=timeReceive.strftime("%H%M%S"),
                            subject=''.join(
                                title for title in sub if title.isalnum())
                        ), 'a+', encoding='utf-8') as f:

                            # 写入文件
                            f.write(
                                "<!-- {from_name},  {from_url} -->".format(from_name=from_name, from_url=from_url))
                            f.write(
                                "\n<!--DateTime : {timeReceive} -->".format(timeReceive=timeReceive))
                            f.write(
                                "\n<!--To : {to_name} , {to_url} -->".format(to_name=to_name, to_url=to_url))
                            f.write(
                                "\n<!--Subject : {subject} -->\n".format(subject=sub))
                            # import pdb; pdb.set_trace()
                            try:
                                f.write(data.decode(data_code['encoding']))
                            except UnicodeDecodeError:
                                print("ERROE: UnicodeDecodeError")
                                if data_code['encoding'] == 'GB2312':
                                    f.write(data.decode('gbk'))

                            f.close()

                    elif part.get_content_type() == 'text/plain':

                        # 判断邮件标题
                        if [value for v in self.sub_dict.values() for value in v if value in sub] and from_name == 'noreply':

                            data = part.get_payload(decode=True)
                            data_code = chardet.detect(data)
                            try:
                                mContext = data.decode(data_code['encoding'])
                            except UnicodeDecodeError:
                                print("ERROE: UnicodeDecodeError")
                                mContext = data.decode('gbk')

                            # 获取邮件的类型
                            mail_type = "".join(
                                [k for k, v in self.sub_dict.items() for value in v if value in sub])

                            if mail_type == 'AccountOpeningApproval' or mail_type == 'forCs1Notify':
                                roleName = "".join(re.findall(',(.+):', mContext))  # 角色名称
                                self.Role.append(roleName)
                            elif mail_type == 'DailyReport':
                                self.DailyReportGB.append(True)
                            elif mail_type == 'LeadForm':
                                self.LeadFormGB.append(True)
                            elif mail_type == 'LeadFormRemind':
                                self.LeadFormRemindGB.append(True)
                            else:
                                pass

    def send_mail(self):
        # mailContext = """
        #     <html>
        #     <body>
        #         <table border="1">
        #             <caption>邮件接收统计</caption>
        #             <tr>
        #                 <th>邮件类型</th>
        #                 <th>是否收到</th>
        #                 <th>数量</th>
        #             </tr>
        #             <tr>
        #                 <th>定时邮件({account})</th>
        #                 <th>{isSend}</th>
        #                 <th>{count}</th>
        #             </tr>
        #         </table>
        #     </body>
        #     </html>

        # """.format(account=self.Role)
        import pdb;pdb.set_trace()
        isRepeat = False
        table = PrettyTable(['邮件类型', '是否收到', '数量'])
        for col in self.sub_dict.keys():
            if col == 'AccountOpeningApproval' or col == 'forCs1Notify':
                if not isRepeat:
                    for accName in set(self.Role):
                        table.add_row([col+'>>'+accName, '是', '2'])
                    isRepeat = True

            else:
                table.add_row([col, '否', '5'])

        print(table)



        msg = MIMEText(mailContext, 'html', 'utf-8')
        msg['From'] = self.set_details(
            "Onedi<{from_name}>".format(from_name=self.username))
        msg['To'] = self.set_details(
            "onedi<{to_url}>".format(to_url=self.sendaddr))
        msg['Subject'] = Header("每日接收邮件统计", 'utf-8').encode()

        smtpServer = smtplib.SMTP(self.smtp_server, 25)
        # smtpServer.set_debuglevel(1)
        smtpServer.login(self.username, self.password)
        smtpServer.sendmail(self.username, self.sendaddr, msg.as_string())
        smtpServer.quit()


if __name__ == '__main__':
    testmail = AutoTestMail()
    testmail.login()
    testmail.send_mail()
    # apscheduler = BlockingScheduler()
    # apscheduler.add_job(
    #     func=testmail.login, trigger='cron', day_of_week='0-6', hour=16, minute=2)
    # apscheduler.start()
