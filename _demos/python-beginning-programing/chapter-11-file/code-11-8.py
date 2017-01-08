#!/usr/bin/env python
# coding=utf-8
# 在while循环中使用

f = open('somefile.txt')
while True:
    line = f.readline()
    if not line:
        break
    print line
f.close()
