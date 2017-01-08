#!/usr/bin/env python
# coding=utf-8
# 为Python脚本添加行号（要小心使用inplace，false时会打印到控制台，true时才会修改文件）

import fileinput

for line in fileinput.input(inplace=False):
    line = line.rstrip()
    num = fileinput.lineno()
    print '%-40s # %2i' % (line, num)
