#!/usr/bin/env python
# coding=utf-8
# 使用threading模块
# 报错：list index out of range

import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()


def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in loops: #start threads
        threads[i].start()

    for i in loops: #wait for all
        threads[i].join() #threads to finish

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
