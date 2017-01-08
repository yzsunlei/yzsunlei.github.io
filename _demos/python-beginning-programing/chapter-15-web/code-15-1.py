#!/usr/bin/env python
# coding=utf-8
# 简单的屏幕抓取程序，什么都没有输出

from urllib import urlopen
import re

p = re.compile('<a .*?><a .*? href="(.*?)">(.*?)</a>')
text = urlopen('http://python.org/community/jobs').read()
for url, name in p.findall(text):
    print '%s (%s)' % (name, url)
print 'end'
