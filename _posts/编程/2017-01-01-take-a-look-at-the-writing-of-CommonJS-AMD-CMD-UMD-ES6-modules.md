---
layout: post
title: 来看看CommonJS、AMD、CMD、UMD、ES6模块的写法
category: 编程
tag: javascript
exception: Javascript模块化编程已经越来越流行了，现在主要是用ES6的import,export方式了。实际上除了ES6，JavaScript模块化导出还有几种不同的方式。
readtime: 15
---

## CommonJS
1. 简单的写法
```javascript
// 依赖
var $ = require('jquery');
// 方法
function myFunc() {};
// 暴露公共方法
module.exports = myFunc;
```
2. 复杂的例子
```javascript
// 依赖
var $ = require('jquery');
var _ = require('underscore');
// 方法
function a() {}; // 私有方法
function b() {}; // 公共方法
function c() {}; // 公共方法
// 暴露公共方法
module.exports = {
    b: b,
    c: c
}
```

## AMD
1. 简单的例子
```javascript
define(['jquery'], function($) {
  // 方法
  function myFunc() {};
  // 暴露公共方法
  return myFunc;
});
```
2. 复杂的例子
```javascript
define(['jquery', 'underscore'], function($, _) {
  // 方法
  function a() {}; // 私有方法
  function b() {}; // 公共方法
  function c() {}; // 公共方法
  // 暴露公共方法
  return {
      b: b,
      c: c,
  }
});
```
3. AMD提前执行，依赖前置，一个当多个用

## CMD
1. 简单的例子
```javascript
define(function(require, exports, module) {
  var a = require('./a.js');
  a.do();
  var b = require('./b.js');
  b.do();
});
```
2. CMD是延迟执行，依赖就近，职责单一

## UMD
1. CommonJS和AMD风格一样流行，于是又产生了一个统一的规范
2. 简单的例子
```javascript
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
      // AMD
      define(['jquery'], factory);
  } else if (typeof exports === 'object') {
      // Node, CommonJS类的
      module.exports = factory(require('jquery'));
  } else {
      // 浏览器全局变量(root 即window)
      root.returnExports = factory(root.jQuery);
  }
}(this, function($) {
    // 方法
    function myFunc() {};
    // 暴露公共方法
    return myFunc;
}));
```
3. 复杂的例子
```javascript
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD
        define(['jquery', 'underscore'], factory);
    } else if (typeof exports === 'object') {
        // Node, CommonJS之类的
        module.exports = factory(require('jquery'), require('underscore'));
    } else {
        // 浏览器全局变量(root 即 window)
        root.returnExports = factory(root.jQuery, root._);
    }
}(this, function ($, _) {
    // 方法
    function a(){}; // 私有方法
    function b(){}; // 公共方法
    function c(){}; // 公共方法
 
    // 暴露公共方法
    return {
        b: b,
        c: c
    }
}));
```

## ES6
1. import 实现模块的导入
```javascript
import { a } from './a.js';
import a from './a.js';
import { default as aa } from './a.js';
```
2. export 实现模块的导出
```javascript
export var a = 1; // 导出变量
export function foo() {}; // 导出方法
export default class {}; // 导出类
```

## 参考阅读
* [AMD、CMD、UMD 模块的写法](http://web.jobbole.com/82238/)
* [javascript模块化之CommonJS、AMD、CMD、UMD、ES6](http://blog.csdn.net/Real_Bird/article/details/54869066)
* [该如何理解AMD ，CMD，CommonJS规范--javascript模块化加载学习总结](https://www.tuicool.com/articles/MVrMBrI)