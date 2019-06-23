---
layout: post
title: 用JavaScript来说数据结构
category: 编程
tag: JavaScript
exception: 
readtime: 12
---

## 什么是数据结构
* 在计算机科学中，数据结构（data structure）是计算机存储、组织数据的方式。
* 数据结构是指相互之间存在一种或多种特定关系的数据元素的集合。

## 数据结构概念定义
* 数据：是用来描述一种客观事物的符号，分为数据元素、数据对象、数据项等。
* 结构：数据元素相互之间的关系，分为逻辑结构和存储结构两大类。
* 数据逻辑结构：指数据元素之间的前后件关系，分为集合、线性结构、非线性结构等。
* 数据存储结构：指数据的逻辑结构在计算机存储空间的存放形式，分为顺序结构、链式结构、索引结构、散列结构等。

## 数据结构有哪些
* **列表**： 

一个存储元素的线性集合（collection），元素可以通过索引来任意存取，索引通常是数字，用来计算元素之间存储位置的偏移量。 

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/01.list.js)

* **队列**： 

用于存储按顺序排列的数据，先进先出。 

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/02.queue.js)

* **栈**： 

一种高效的数据结构，数据只能在栈顶添加或删除，先进后出。 

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/03.stack.js)

* **链表**： 

由一组节点组成的集合，每个节点都使用一个对象的引用指向它的后继。 

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/04.linkedlist.js)

* **字典**：

以键-值对形式存储数据的数据结构。

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/05.dictionary.js)

* **散列表**：

散列是一种常用的数据存储技术，散列后的数据可以快速地插入或取用。

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/06.hashtable.js)

* **集合**：

一种包含不同元素的数据结构。集合中的成员是无序的，集合中不允许相同成员存在。

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/07.set.js)

* **树**：

一种非线性的数据结构，以分层的方式存储数据，被用来存储具有层级关系的数据。

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/08.bst.js)

* **图**：

由边的集合及顶点的集合组成。

[示例代码](https://github.com/yzsunlei/javascript-data-structure/blob/master/09.graph.js)

* 上面对常用的9种数据结构做了一个简要的介绍。更好的理解数据结构，还是看图解、看示例源码比较好。

## 参考资料
* [https://book.douban.com/subject/25945449/](https://book.douban.com/subject/25945449/)
* [https://book.douban.com/subject/27129352/](https://book.douban.com/subject/27129352/)
* [https://www.cnblogs.com/shuoer/p/8424848.html](https://www.cnblogs.com/shuoer/p/8424848.html)
* [https://segmentfault.com/a/1190000010343508](https://segmentfault.com/a/1190000010343508)
