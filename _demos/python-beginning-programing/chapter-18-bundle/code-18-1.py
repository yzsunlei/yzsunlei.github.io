#!/usr/bin/env python
# coding=utf-8
# 简单的Distutils的安装脚本, 可以实现Distutils的各种功能
# 使用时确保在同一个目录下存在名为hello.py的模块文件
# python setup.py build Distutils会创建一个名为build的子目录，其中包含名为lib的子目录

from distutils.core import setup

setup(name='Hello',
      version='1.0',
      description='A simple example',
      author='Magnus Lie Hetland',
      py_modules=['hello'])
