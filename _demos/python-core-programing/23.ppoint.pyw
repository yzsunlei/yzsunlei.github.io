#!/usr/bin/env python
# coding=utf-8
# 启动PowerPoint, 并在幻灯片写入一些数据

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)


def ppoint():
    app = "PowerPoint"
    ppoint = win32.gencache.EnsureDispatch("%s.Application" % app)
    pres = word.Documents.Add()
    pres.Visible = True

    s1 = pres.Slides.Add(1, win32.constants.ppLayoutText)
    sleep(1)
    sla = s1.Shapes[0].TextFrame.TextRange
    sla.Text = 'Python-to-%s Demo' % app
    sleep(1)
    slb = s1.Shapes[1].TextFrame.TextRange
    for i in RANGE:
        slb.InsertAfter("Line %d\r\n" % i)
        sleep(1)
        slb.InsertAfter("\r\nTh-th-th-that is all folks!")

    warn(app)
    pres.Close()
    ppoint.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    ppoint()
