#!/usr/bin/env python
# coding=utf-8
# 找出行


def lines(file):
    for line in file: yield line
    yield '\n'


# 找出块的一个简单方法就是收集遇到的所有行，直到遇到空行，然后返回已经收集的行，那个返回的行就是一个块
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []