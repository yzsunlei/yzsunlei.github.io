#!/usr/bin/env python
# coding=utf-8
# 使用fileinput对行进行迭代

import fileinput
for line in fileinput.input('somefile.txt'):
    print ':' + line
