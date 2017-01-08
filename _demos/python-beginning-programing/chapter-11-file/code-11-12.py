#!/usr/bin/env python
# coding=utf-8
# 迭代文件：从2.2开始，文件对象是可迭代的

f = open('somefile.txt')

for line in f:
    print line
f.close()
