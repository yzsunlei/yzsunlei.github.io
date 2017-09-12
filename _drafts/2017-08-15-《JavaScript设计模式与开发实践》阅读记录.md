---
layout: post
title: 《JavaScript设计模式与开发实践》阅读记录
category: 阅读
tag: JavaScript, 设计模式
exception: 
readtime: 16
---

# 单例模式

# 策略模式

# 代理模式

# 迭代器模式

# 发布-订阅模式

# 命令模式

# 组合模式

# 模板方法模式

# 享元模式

# 职责链模式

# 中介者模式

# 装饰器模式
````javascript
Function.prototype.before = function( beforefn ){
 var __self = this; // 保存原函数的引用
 return function(){ // 返回包含了原函数和新函数的"代理"函数
 beforefn.apply( this, arguments ); // 执行新函数，且保证 this 不被劫持，新函数接受的参数
 // 也会被原封不动地传入原函数，新函数在原函数之前执行
 return __self.apply( this, arguments ); // 执行原函数并返回原函数的执行结果，
 // 并且保证 this 不被劫持
 }
} 
````

# 状态模式

# 适配器模式

