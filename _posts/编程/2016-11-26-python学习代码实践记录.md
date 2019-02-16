---
layout: post
title: python学习代码实践记录
category: 编程
tag: python
exception: 公司的新项目后端使用python来写的，我这个小前端有空的时候也来学习实践了一些
readtime: 12
---

## 过滤偶数
```python
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, [1, 2, 3, 4, 5]))
print(L)
```

## 用filter求素数
```python
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n >0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个对象
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

## 写一个hello的模块
```python
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
```

## 以_或__开头的函数默认内部使用
```python
def _private_1():
    return 'Hello, %s' % name

def _private_2():
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting('Michael'))
```

## 缩略图生成
```python
from PIL import Image

def thumbnail_generator(mdic):
    im = Image.open(mdic)
    size = 128, 128 #定义一个元组
    print(im.format, im.size, im.mode) #png (540, 258) P
    if im.mode != 'RGB':
        im = im.convert('RGB') #mode!='RGB'时要转化为RGB,否则生成JPG缩略图报错
    im.thumbnail(size)
    im.save('thumb.jpg', 'JPEG')

thumbnail_generator('test.jpg')
```

## 函数实现
```python
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}

def print_score(std):
    print('%s: %s' %(std['name'], std['score']))

print_score(std2)
```

## 面向对象实现
```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score # __表示类私有的

    def print_score(self):
        print('%s: %s' %(self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()
```

## 类的继承和多态
```python
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running..')

class Cat(Animal):
    def run(self):
        print('Cat is running..')

dog = Dog()
dog.run()

cat = Cat()
cat.run()
```

## 从文件流中读取图像
```python
def readImg(fp):
    if(hasattr()):
        print(readData(fp))
    print(None)

readImg('test.jpg')
```

## 使用get和set
```python
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())
s.set_score(9999) # 报错
```

## 多重继承
```python
class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrish(Bird):
    pass

# 再加上Runnable和Flyable功能
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(self):
    def fly(self):
        print('Flying...')

# 对于需要Runnable功能的
class Bat(Mammal, Runnable):
    pass
```

## 使用错误码来表示是否出错, 其实十分不便
```python
def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r = (-1):
        print('Error')
    else:
        pass
```

## try...except...finally...错误处理机制
```python
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
```

## 多个except来捕获不同类型的错误
```python
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
finally:
    print('finally...')
print('END')
```

## 调用堆栈, 错误一直往上抛
```python
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
```

## 执行错误抛出后，继续运行
```python
class FooEffor(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value:%s' % s)
    return 10 /n

foo('0')

# 1. 简单直接粗暴, 把可能有问题的变量打印出来
def foo(s):
    n = int(s)
    print('>>> n = %d' %n)
    print 10 / n

def main():
    foo('0')

main()

# 2.凡是print()来辅助查看的地方, 都可以用断言(assert)来替代s
def foo(s):
    assert n != 0, 'n is zero'
    return 10 / n
def main():
    foo('0')

main()

# 3.logging不会抛出错误,而且可以输出到文件
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
```

## 编写单元测试
```python
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        self.assertEqual(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d['key'] = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
```

## 访问数据库
```python
SQLlite

# mysql
# 导入mysql驱动
import mysql.connector
# 注意把password设为你的root口令
conn = mysql.connector.connect(user='root', password='123456', database='test')
cursor = conn.cursor()
# 创建user表
cursor.excute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录, 记住mysql的占位符是%s
cursor.excute('insert into user(id, name) value(%s, %s)', ['1', 'lei.sun'])
cursor.rowcount
# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.excute('select * from user where id = %s', ('1', ))
values = cursor.fetchall()
values
```

## 参考资料
* [Python基础教程(第3版)](https://amazon.cn/gp/product/B079BJPVFL/ref=as_li_tl?ie=UTF8&tag=jishu88-23&camp=536&creative=3200&linkCode=as2&creativeASIN=B079BJPVFL&linkId=2d299f23aa26710278388fbc9f807383)
* [	Python核心编程(第3版)](https://amazon.cn/gp/product/B01FQAS0KK/ref=as_li_tl?ie=UTF8&tag=jishu88-23&camp=536&creative=3200&linkCode=as2&creativeASIN=B01FQAS0KK&linkId=10488e6e34b8a0a2b4657f58e3fd9e3f)
