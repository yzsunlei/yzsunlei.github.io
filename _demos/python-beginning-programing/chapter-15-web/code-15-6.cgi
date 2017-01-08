#!/usr/bin/env python
# coding=utf-8
# 利用FieldStorage获取一个值的CGI脚本

import cgi
form = cgi.FieldStorage()

name = form.getvalue('name', 'world')

print 'Content-type: text/plain'
print #打印空行，以结束首部

print 1/0
print 'Hello, %s' % name

