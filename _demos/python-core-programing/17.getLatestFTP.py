#!/etc/bin/env python
# coding=utf-8
# FTP下载示例，FTP地址好像访问不到，待测试

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/webtools'
FILE = 'mozbot-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror), e:
        print 'ERROR: cannot reach "%s"' % HOST
        return
    print '*** Connected to host %s"' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anoymously'
        f.quit()
        return
    print '*** Logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Changed to "%s" folder' % DIRN

    try:
        f.retrbinary('PETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s" % FILE'
        os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE
        f.quit()
        return

if __name__ == '__main__':
    main()
