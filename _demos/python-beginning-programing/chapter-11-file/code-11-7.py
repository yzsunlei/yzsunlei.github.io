#!/usr/bin/env python
# coding=utf-8
# 用不同的方式写循环

f = open('somefile.txt')
while True:
    char = f.read(1)
    if not char:
        break
    print char
f.close()
