---
layout: post
title: JavaScript错误类型和处理方式
category: 编程
tag: JavaScript
exception: 总结一下JavaScript的几种错误类型，便于以后在debug的时候能够快速的定位错误的代码...
readtime: 10
---

# 六大错误类型
* 语法错误(SyntaxError)：JavaScript代码解析时发生语法错误
```javascript
var 1s; // 变量名命名错误，不允许数字开头
```
* 引用错误(ReferenceError)：引用一个不存在的变量时发生的错误或将值分配给无法分配的对象
```javascript
this = 100; // 对this进行赋值，报错
```
* 范围溢出错误(RangeError)：当一个值超出有效范围时发生的错误
```javascript
var arr = new Array(-1); // 数组长度为负数
```
* 类型错误(TypeError)：变量或者参数不是预期类型时发生的错误
```javascript
var obj = {};
obj.getName(); // 调用了不存在的方法
```
* URI解析错误(URIError)：URI相关函数的参数不正确时抛出的错误，主要涉及encodeURI()、decodeURI()、encodeURIComponent()、decodeURIComponent()、escape()和unescape()这六个函数
```javascript
decodeURI('%2'); // 传入无法解析的参数
```
* Eval错误(EvalError)：eval函数没有被正确的执行时，会抛出错误

# 常用处理方式
* onerror事件处理函数
```javascript
// 三个参数：错误消息message、出错文件url、出错行号line
window.onerror = function(message, url, line) {
   alert("发生错误！");
}
// 注：不光window支持onerror事件，img图片同样提供支持，当一个图像文件未能成功载入时，error事件就会触发，这点在实际应用中较多
```
* try...catch语句
```javascript
try {
    window.openFile();
    alert("成功调用openFile方法会执行");
} catch (error) {
    // 这里error对象的属性：name表示错误类型的字符串、message实际的错误信息
    alert("发生异常时会执行！");
} finally {
    alert("不管怎样，我都会执行!");
}
```

# 参考
* [js常见错误类型](http://blog.csdn.net/bing_javascript/article/details/52522749)
* [Error对象-MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)