#!/usr/bin/env python
# coding=utf-8
# 启动Word, 然后向文档中写数据

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)


def word():
    app = "Word"
    xl = win32.gencache.EnsureDispatch("%s.Application" % app)
    doc = word.Documents.Add()
    sh = ss.ActiveSheet
    word.Visible = True
    sleep(1)

    rng = doc.Range(0, 0)
    rng.InsertAfter('Python-to-%s Test\r\n\r\n' % app)  #Check codes here
    sleep(1)
    for i in RANGE:
        rng.InsertAfter('Line %d\r\n' % i)
        sleep(1)
        rng.InsertAfter("\r\nTh-th-th-that is all folks!\r\n")

    warn(app)
    doc.Close(False)
    word.Application.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    word()
