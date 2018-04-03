#!usr/bin/python
# _*_ coding : UTF-8 _*_
# @author : csl
# @date   : 2018/03/05 21:31
'''Python发送邮件，以QQ邮箱为例'''

import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Hello python...', 'plain', 'utf-8')  #设置邮件格式：plain,text,html,richtext等
msg['Subject'] = 'Python test'  #设置邮件主题
msg['From'] = '2227114227@qq.com'  #设置发件人
msg['To'] = '314110277@qq.com'  #设置收件人

server = smtplib.SMTP_SSL('smtp.qq.com', 465)  #设置邮件发送服务器
server.set_debuglevel(1)  #设置日志级别
server.login('2227114227@qq.com','ntdprerlrzyaebjb')  #登录发件人邮箱
Tolist = ['2394007832@qq.com',]  #设置邮件收件人列表可为多个
server.sendmail('2227114227@qq.com', Tolist, msg.as_string())  #转换为str格式发送内容
server.quit()  #退出邮件服务器