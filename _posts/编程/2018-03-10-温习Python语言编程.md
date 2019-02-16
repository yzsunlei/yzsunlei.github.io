---
layout: post
title: 温习Python语言编程
category: 编程
tag: python
exception: 重看廖雪峰的Python教程，把之前没有理解到位的点整理出来，加深理解
readtime: 15
---

## 没有理解到位的点
* 函数参数的多种形式
* 尾递归优化防止造成栈溢出
* 汉诺塔的移动
* 生成器：(x * x for x in range(10))
* 使用generator生成杨辉三角
* 理解Iterable和Iterator
* 偏函数应用和函数柯里化
* min, max = max, min理解
* 筛选素数和回数实例
* nonlocal的应用
* yield和yield from
* 使用dir()获得一个str对象的所有属性和方法
* __slots__：限制实例的属性，不限制class动态绑定属性方法
* 自定制类：
* asyncio

## 函数参数的多种形式
```html
1、位置参数：func1(a, b, c)，根据位置做匹配，严格要求实参的数量与行参的数量位置相等
2、默认参数：func2(a, b=2, c=3)，根据键值对的形式做实参与行参的匹配，通过这种方式可以忽略参数的位置关系，直接根据关键字来进行赋值，不传则用默认值
3、可变参数：func3(*args)，可以传入任意个参数，若干个参数都被放到tuple元组中赋值给形参args，函数中直接操作args这个tuple元组就可以了
4、关键字参数：func4(**kw)：以键值对字典的形式向函数传参，含有第二种位置的灵活性的同时具有第三种方式的数量上的无限制
注：四种方式混用时要遵守args=须在args之后，*args须在args=value之后，**kw须在*args之后
```

## 尾递归优化防止造成栈溢出
```html
尾递归是指在函数返回的时候，调用自身本身，并且return语句不能包含表达式，这样编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次都只占用一个栈帧，不会出现栈溢出的情况
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```

## 生成器
```html
生成器不会把结果保存在一个系列中，而是保存生成器的状态，在每次进行迭代时返回一个值，直到遇到StopIteration异常结束
函数中出现yield关键字，那么该函数就不再是普通函数，而是生成器函数
def odd():
    n = 1
    while True:
        yield n
        n += 2
```

## 使用generator生成杨辉三角
```html
每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def triangles();
    nlist = [1]
    while True:
        yield nlist
        nlist.append(0)
        nlist = [nlist[i] + nlist[i - 1] for i in range(len(nlist))]
```

## 理解Iterable和Iterator
```html
凡是可以for循环的，都是Iterable；
凡是可以next()的，都是Iterator；
集合数据类型如list，dict，str，都是Iterable不是Iterator，但可以通过iter()函数获得一个Iterator对象
isinstance({}, Iterable) --> True
isinstance((), Iterable) --> True
isinstance({}, Iterator) --> False
isinstance((), Iterator) --> False
```

## 偏函数应用和函数柯里化
```html
偏函数应用指的是固化函数的一个或一些参数，从而产生一个新的函数
def log(level, message):
    print level + "：" + message
def logWarning(message):
    log("Warning", "this is one warning message")
以上是偏函数应用
def log(level):
    def logMessage(message):
        print level + "：" + message
    return logMessage
log("Warning")("this is one warning message")
```

## 未完待续

## 参考资料
* [廖雪峰的Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
* [Python官方文档](https://docs.python.org/3/)
