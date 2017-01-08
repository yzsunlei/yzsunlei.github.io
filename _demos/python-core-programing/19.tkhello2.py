#!/usr/bin/env python
# coding=utf-8
# 按钮组件演示

import Tkinter

top = Tkinter.Tk()
quit = Tkinter.Button(top, text='Hello World!', command=top.quit)
quit.pack()
Tkinter.mainloop()
