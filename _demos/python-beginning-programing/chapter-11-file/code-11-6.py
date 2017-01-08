#!/usr/bin/env python
# coding=utf-8
# 用read方法对每一个字符进行循环

f = open('somefile.txt')
char = f.read(1)
while char:
    print char
    char = f.read(1)
f.close()
