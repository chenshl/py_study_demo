#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
通过temp发送邮件
@author:chensl
"""

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input("From: ")
from_addr = "2227114227@qq.com"
# password = input("Password: ")
password = "ntdprerlrzyaebjb"
# to_addr = input("To: ")
to_addr = "prodiger2008@126.com"
# smtp_server = input("SMTP server: ")
smtp_server = "smtp.qq.com"

msg = MIMEText("hello, send by Python...", "plain", "utf-8")
msg["From"] = _format_addr("Python爱好者 <%s>" % from_addr)
msg["To"] = _format_addr("管理员 <%s>" % to_addr)
msg["Subject"] = Header("来自SMTP的问候。。。", "utf-8").encode()

server = smtplib.SMTP(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
print("end")
