#!/usr.bin/env python
# coding=utf-8
# 单线程中运行的循环

from time import sleep, ctime


def loop0():
    print 'start loop0 at:', ctime()
    sleep(4)
    print 'loop0 done at:', ctime()


def loop1():
    print 'start loop1 at:', ctime()
    sleep(2)
    print 'loop1 done at:', ctime()


def main():
    print 'starting at:', ctime()
    loop0()
    loop1()
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
