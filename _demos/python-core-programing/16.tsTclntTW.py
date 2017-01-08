#!/usr/bin/env python
# coding=utf-8
# Twisted Reactor TCP客户端
# No module

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = raw_input('>')
        if data:
            print '...sending %s ...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def dataReceived(self, data):
        print data
        self.sendData()


class TSClntFactory(protocol.ClientFatory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
    lambda self, connector, reason: stop()
    reactor.connectTCP(HOST, PORT, TSClntFactory())
    reactor.run()
