#!/etc/bin/env python
# coding=utf-8
# NNTP下载示例：下载并显示Python新闻组comp.lang.python最后一片文章的前20个词
# 未完

import nntplib
import socket

HOST = 'your.nntp.server'
GRNM = 'copm.lang.python'
USER = 'wesley'
PASS = "you will Nerver Guess"

def main():
    try:
        n = nntplib.NNTP(HOST, user = USER, password=PASS)
    except socket.gaierror, e:
        print 'ERROR: cannot reach host "%s"' % HOST
        print '("%s")' % eval(str(e))[1]
        return
    except nntplib.NNTPPermanentError, e:
        print 'ERROR: access denied on "%s"' % HOST
        prnt '("%s")' % str(e)
        return
    print '*** Connected to host "%s" % HOST'

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError, e:
        print 'ERROR:cannot load group "%s"' % GRNM
        print '("%s")' % str(e)
        print 'Server may require authentication'
        print 'Uncomment/edit login line above'
        n.quit()
        return
    except nntplib.NNTPTemporaryError, e:
        print 'ERROR: group "%s" unavailable' % GRNM
        print '("%s")' % str(e)
        n.quit()
        return
    print '*** Found newsgroup %s"' % GRNM

    rng = '%s-%s' % (fst, lst)
        rsp, frm = n.xhdr('from', rng)rsp, sub = n.xhdr('subject', rng)
