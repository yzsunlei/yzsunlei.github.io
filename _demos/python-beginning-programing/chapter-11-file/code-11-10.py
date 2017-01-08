#!/usr/bin/env python
# coding=utf-8
# 用readlines迭代行

f = open('somefile.txt')

for line in f.readlines():
    print '+:' + line
f.close()
