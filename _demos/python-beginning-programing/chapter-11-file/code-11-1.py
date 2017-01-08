#!/usr/bin/env python
# coding=utf-8
# 统计sys.stdin中单词数的简单脚本，需要配合somefile.txt文本文件
# cat somefile.txt | python code-11-1.py

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'Wordcount: ', wordcount
