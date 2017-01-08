#!/usr/bin/env python
# coding=utf-8
# 可以接受连接的服务器
# 中断快捷键：UNIX内为Ctrl+C，Windows内为Ctrl+Break

from asyncore import dispatcher
import socket
import asyncore


class ChatServer(dispatcher):

    def handle_accept(self):
        conn, addr = self.accept()
        print 'Connection attempt from', addr[0]

s = ChatServer()
s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5005))
s.listen(5)
asyncore.loop()
