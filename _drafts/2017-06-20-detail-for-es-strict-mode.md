---
layout: post
title: 详解ES严格模式
category: 编程
tag: 严格模式
exception: 开启JavaScript代码的严格模式，让你的代码更规范，更高效，更安全，下面我们一起总结一下ES的严格模式
readtime: 10
---

# 是什么？
* 是可选择的一个限制JavaScript的变体的一种方式
* 它不仅仅是一个子集，它故意地具有与正常代码不同的语义
* 不支持它的浏览器与支持的会执行不同行为的代码
* 不要依靠它，在没有特性测试来支持它的相关方面

# 有什么用？
* 消除了一些JavaScript的静默错误，通过改变他们来抛出错误
* 修复了JavaScript引擎难以执行优化的错误，有时候可以比非严格模式相同代码运行的更快
* 禁用了在ECMAScript的5未来版本中可能会定义的一些语法

# 如何开启严格模式？
* 在eval代码，function代码，事件处理属性，传入setTimeout方法的字符串和包含整个脚本块中开启严格模式都会如预期一样工作
* 为某个script标签开启严格模式
```javascript
"use strict"; 
var v = "hello";
```
这种语法存在陷阱，不能盲目的合并冲突代码
* 为某个函数开启严格模式
```javascript
function strict() {
  'use strict';
  return "hello";
}
```

# 严格模式有哪些不同？


# 参考
* [严格模式-JavaScript|MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode)
* [向严格模式过渡](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode/Transitioning_to_strict_mode)
* [理解JavaScript中的严格模式](http://www.codesec.net/view/405985.html)