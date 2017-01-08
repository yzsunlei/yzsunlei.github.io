#!/usr/bin/env python
# coding=utf-8
# 用read迭代每个字符

f = open('somefile.txt')

for line in f.readline():
    print '+:' + line
f.close()
