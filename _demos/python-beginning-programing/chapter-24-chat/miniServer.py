#!/usr/bin/env python
# coding=utf-8
# 迷你服务器程序

from asyncore import dispatcher
import asyncore

# 定义服务器类
class ChatServer(dispatcher):
    pass

s = ChatServer()
asyncore.loop()
