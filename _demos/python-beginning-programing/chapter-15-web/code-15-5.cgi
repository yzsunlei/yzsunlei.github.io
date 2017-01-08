#!/usr/bin/env python
# coding=utf-8
# 调用回溯的CGI脚本，在浏览器访问显示错误结果和代码原因

print 'Content-type: text/plain'
print #打印空行，以结束首部

print 1/0
print 'Hello World'

