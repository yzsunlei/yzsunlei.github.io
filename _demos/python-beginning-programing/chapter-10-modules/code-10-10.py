#!/usr/bin/env python
# coding=utf-8
# 寻找Email发信人的程序

import fileinput, re

pat = re.compile('From: (.*) < .*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m: print m.group()
