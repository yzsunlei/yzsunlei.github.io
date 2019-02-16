---
layout: post
title: 一起看一下Python2.x和Python3.x的重要区别
category: 编程
tag: python
exception: python2在2020年就停止支持了，之前写的项目都是用的python2.7，现在在用python3.5，今天花点时间整理了一下python2.x和python3.x的重要区别
readtime: 15
---

## 统一了字符编码支持
1. Python3.x源码文件默认使用utf-8编码
```python
# 现在可以这样写啦
中国 = 'china'
print(中国) # china
```

## 增加了新的语法
1. print和exec等成为了函数
```python
print 'Hello, World' # python2.x
print('Hello, World') # python3.x
```
2. [格式化字符串变量](https://link.zhihu.com/?target=https%3A//www.python.org/dev/peps/pep-0498/)
3. [类型标注](https://link.zhihu.com/?target=https%3A//www.python.org/dev/peps/pep-0484/)
4. 添加了`nonlocal`关键词，使用`nonlocal x`可以直接指派外围变量
5. 添加`yield from、async/await、yield for`关键词
6. 添加`__annotations__、__context__、__traceback__、__qualname__`等方法

## 修改了一些语法
1. `metaclass、raise、map、filter`以及dict的`items/keys/values`方法返回迭代器
2. 描述符协议
3. [保存类属性定义顺序](https://link.zhihu.com/?target=https%3A//www.python.org/dev/peps/pep-0520)
4. [保存关键字参数顺序](https://link.zhihu.com/?target=https%3A//www.python.org/dev/peps/pep-0468) 

## 去掉了一些语法
1. 去掉了cmp
2. `!=`代替了`<>`
3. `range`包含了`xrange`
4. 不再有经典类

## 增加了一些新的模块
1. `concurrent.futures`
2. `venv`
3. `unittest.mock`
4. `asyncio`
5. `selectors`
6. `typing`

## 修改了一些模块
1. 主要对模块添加函数、类、方法或者参数

## 模块改名
1. 把一些相关的模块放进同一个包里面
2. `httplib, BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, Cookie, cookielib`放进了http里面
3. `urllib, urllib2, urlparse, robotparser`放进了`urllib`里面
4. `SocketServer`改成了`socketserver`
5. `Queue`改成`queue`

## 去掉了一些模块或者函数
1. 去掉了`gopherlib, md5, contextlib.nested, inspect.getmoduleinfo`等

## 做了一些优化
1. 重新实现了dict可以减少20%-25%的内存使用
2. 提升pickle序列化和反序列化的效率
3. `collections.OrderedDict`改用C实现
4. 通过`os.scandir`对glob()及iglob()进行优化，使得大概快了3-6倍

## 其他不太需要关心的
1. 构建过程、C的API、安全性等方面的修改

## 参考资料
* [python2.7和Python3.5的区别](http://blog.csdn.net/Onlywangchao/article/details/71437682)
* [Python 2.7.x 和 3.x 版本的重要区别](http://blog.csdn.net/liushulin183/article/details/51493913)
* [Python 2 和 Python 3 有哪些主要区别？](https://www.zhihu.com/question/19698598)
* [10 awesome features of Python that you can't use because you refuse to upgrade to Python 3](https://www.asmeurer.com/python3-presentation/slides.html)
