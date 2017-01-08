#!/usr/etc/bin pyhton
# coding=utf-8
# 反序打印命令行参数

import sys

args = sys.argv[1:]
args.reverse()
print " ".join(args)

