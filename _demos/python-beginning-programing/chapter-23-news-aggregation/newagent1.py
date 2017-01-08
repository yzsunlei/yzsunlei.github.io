#!/usr/bin/env python
# coding=utf-8
# 简单的新闻收集代理程序

from nntplib import NNTP
from time import strftime, time, localtime

# Number of seconds in one day
day = 24 * 60 * 60

# calculate the date and hours of yesterday
yesterday = localtime(time() - day)
date = strftime('%y%m%d', yesterday)
hour = strftime('%H%M%S', yesterday)

# define the server info
servername = 'news.foo.bar'
group = 'comp.lang.python.announce'
server = NNTP(servername)

# get all the news
ids = server.newnews(group, date, hour)[1]


for id in ids:
    head = server.head(id)[3]
    for line in head:
        if line.lower().startswith('subject:'):
            subject = line[9:]
            break

    body = server.body(id)[3]

    print subject
    print '-'*len(subject)
    print '\n'.join(body)

server.quit()
