#!/usr/bin/env python
# coding=utf-8
# 标签、按钮和进度条组件演示

from Tkinter import *
import Tkinter


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())


top = Tk()
top.geometry('250x150')

label = Tkinter.Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=40,
              orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit = Button(top, text="QUIT",
              command=top.quit, activeforeground='white', activebackground='red')
quit.pack()

Tkinter.mainloop()
