#!/usr/bin/env python
# coding=utf-8
# 简单的CGI脚本, 通过网络服务器打开，应该看到一个只包括内容为hello world的文本的网页

print 'Content-type: text/plain'
print #打印空行，以结束首部

print 'Hello World'

