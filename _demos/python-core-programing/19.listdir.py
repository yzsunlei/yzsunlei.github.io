#!/usr/bin/env python
# coding=utf-8
# GUI文件遍历系统

import os
from time import sleep
from Tkinter import *

class DirList(object):
    def __init__(self, initdir=None)
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister v1.1')
        self.label.pack()
        self.cwd = StringVar(self.top)
        self.dirl = Label(self.top, fg='blue', font=('Helvetical', 12, 'bold'))
        self.dirl.pack()

        self.dirfm = Fram(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side.RIGHT, fill=Y)
        self.dirs = ListBox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>, self.setDirAndGo')
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fillBOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width=50,textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
            activeforeground='white', activebackground='blue')
        self.ls = Button(self.bfm, text='List Directory', command=self.doLS,
            activeforeground='white', activebackgroud='green')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit,
            activeforeground='white', activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    def clrDir(self, ev=None):
        self.cwd.set('')

    def setDirAndGo(selfself, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir()
        1
        