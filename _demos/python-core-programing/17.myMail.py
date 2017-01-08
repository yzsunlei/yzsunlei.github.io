#!/usr/bin/env python
# coding=utf-8
# SMTP和POP3示例,未测试

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.qq.com'
POP3SVR = 'pop.qq.com'

origHdrs = ['From: 846990846@qq.com', 'To: misigou@qq.com', 'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('misigou@qq.com', origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10) #wait for mail to be delivered

recvSvr = pop3(POP3SVR)
recvSvr.user('ray')
recvSvr.pass_('raysun')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep + 1:]
assert origBody == recvBody
