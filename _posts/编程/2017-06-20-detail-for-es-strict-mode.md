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
* 变化分类：将问题直接转化为错误；简化了如何为给定名称的特定变量计算；简化了eval以及arguments，将写“安全”JavaScript的步骤变得更简单；改变了预测未来ECMAScript行为的方式
* 意外创建全局变量被抛出错误替代
* 会使静默失败的赋值操作抛出异常，如给不可写属性赋值，给只读属性赋值，给不可扩展对象的新属性赋值
* 试图删除不可删除的属性时会抛出异常
```javascript
"use strict";
delete Object.prototype; // 抛出TypeError错误
```
* 要求一个对象内的所有属性名在对象内必须唯一
* 要求函数的参数名必须唯一
* 禁止八进制数字语法，前导0很少有用并可能会错误使用
* 禁止设置primitive值得属性
```javascript
(function() {
    "use strict";
    
    false.true = "";              //TypeError
    (14).sailing = "home";        //TypeError
    "with".you = "far away";      //TypeError
})();
```
* 禁用with
* eval不再为上层范围引入新变量，函数eval被在严格模式下的eval(...)以表达式的形式调用时，其代码会被当作严格模式下的代码执行
* 严格模式禁止删除声明变量
```javascript
"use strict";

var x;
delete x; // !!! 语法错误

eval("var y; delete y;"); // !!! 语法错误
```
* eval和arguments不能通过程序语法被绑定或赋值
```javascript
"use strict";
eval = 17; // 语法错误
arguments++; // 语法错误
```
* 参数的值不会随着arguments对象的值的改变而变化
```javascript
function f(a){
    "use strict";
    a = 42;
    return [a, arguments[0]];
}
```
* 不在支持arguments.callee和arguments.caller，他们是一个不可删除属性，而且赋值和读取时都会抛出异常
* 通过this传递给一个函数的值不会被强制转换成一个对象
* 在严格模式中再也不能通过广泛实现的ECMAScript扩展“游走于”JavaScript的栈中
```javascript
function restricted()
{
    "use strict";
    restricted.caller;    // 抛出类型错误
    restricted.arguments; // 抛出类型错误
}
```
* 严格模式下的arguments不会再提供访问与调用这个函数相关的变量的途径
* 一部分字符变成了保留的关键字，包括implements、interface、let、package、private、protected、public、static和yield
* 禁止了不在脚本或者函数层面上的函数声明
```javascript
"use strict";
if (true){
    function f() { } // !!! 语法错误
    f();
}
```

# 注意
* 主流浏览器现在实现了严格模式，但不要盲目的依赖它
* 谨慎地使用严格模式，通过检测相关代码的功能保证严格模式不出问题
* 记得在支持或者不支持严格模式的浏览器中测试你的代码

# 参考
* [严格模式-JavaScript](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode)
* [向严格模式过渡](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode/Transitioning_to_strict_mode)
* [理解JavaScript中的严格模式](http://www.codesec.net/view/405985.html)