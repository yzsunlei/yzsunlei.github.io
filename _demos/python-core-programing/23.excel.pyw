#!/usr/bin/env python
# coding=utf-8
# 启动excel, 然后将数据填到电子表格的空格中
# No matching distribution found for win32com.client

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)


def excel():
    app = "Excel"
    xl = win32.gencache.EnsureDispatch("%s.Application" % app)
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True
    sleep(1)

    sh.Cells(1, 1).Value = "Python-to-%s Demo" % app
    sleep(1)
    for i in RANGE:
        sh.Cells(i, 1).Value = "Line %d" % i
        sleep(1)
        sh.Cells(i+2, 1).Value = "Th-th-th-that is all folks!"

    warn(app)
    ss.close(False)
    xl.Application.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    excel()
