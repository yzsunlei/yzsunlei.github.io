---
layout: post
title: 如何减少页面重排和重绘
category: 编程
tag: html
exception: 页面重排和重绘指的是什么？为了性能优化，我们如何减少页面的重排和重绘，下面看一看吧
readtime: 10
---

## 什么是重排和重绘
* 页面加载的过程中，HTML标记、JavaScript、CSS、图片加载之后会解析生成两个内部数据结构——DOM树和渲染树
* DOM树表示页面结构，渲染树表示DOM节点如何显示
* 一旦DOM和渲染树构建完成，浏览器就开始显示（绘制）页面元素
* 重排：当DOM的变化影响了元素的几何属性（宽或高），浏览器需要重新计算元素的几何属性，渲染树中受到影响的部分失效，并重新构造渲染树
* 重绘：完成重排后，浏览器会重新绘制受影响的部分到屏幕，或者DOM元素的样式属性发生变化了，浏览器也会重新绘制受影响的部分到屏幕
* 重排一定导致重绘，重绘不一定会有重排

## 看看重排和重绘的消耗性能
以下示例可以看出重排重绘的性能消耗的严重
```html
var times = 15000;
 
// 1 每次过桥+重排+重绘
console.time(1);
for(var i = 0; i < times; i++) {
  document.getElementById('myDiv1').innerHTML += 'a';
}
console.timeEnd(1);
 
// code2 只过桥
console.time(2);
var str = '';
for(var i = 0; i < times; i++) {
  var tmp = document.getElementById('myDiv2').innerHTML;
  str += 'a';
}
document.getElementById('myDiv2').innerHTML = str;
console.timeEnd(2);
 
// code3 
console.time(3);
var _str = '';
for(var i = 0; i < times; i++) {
  _str += 'a';
}
document.getElementById('myDiv3').innerHTML = _str;
console.timeEnd(3);
 
// 1: 2874.619ms
// 2: 11.154ms
// 3: 1.282ms
```

## 哪些情况下会发生重排
1. 添加或者删除可见的DOM元素
2. 元素位置改变
3. 元素尺寸改变
4. 元素内容改变（例如：一个文本被另一个不同尺寸的图片替代）
5. 页面渲染初始化（这个无法避免）
6. 浏览器窗口尺寸改变

## 浏览器的渲染优化排队和刷新
* 大多数浏览器通过队列化修改并批量执行来优化重排过程，如下的三次修改就会保存到一起一次性完成渲染
```javascript
var ele = document.getElementById('myDiv');
ele.style.borderLeft = '1px';
ele.style.borderRight = '2px';
ele.style.padding = '5px';
```
* 但是有时获取布局信息的操作会导致队列刷新
```html
1. offsetTop, offsetLeft, offsetWidth, offsetHeight
2. scrollTop, scrollLeft, scrollWidth, scrollHeight
3. clientTop, clientLeft, clientWidth, clientHeight
4. getComputedStyle() (currentStyle in IE)
```

## 优化、减少重排和重绘
1. 直接改变className，如果动态改变样式，则使用cssText
```javascript
// 比较好的写法
el.style.cssText += "left: 10px; top: 20px";
```
2. 让要操作的元素进行”离线处理”，处理完后一起更新
```html
a) 使用DocumentFragment进行缓存操作,引发一次回流和重绘；
b) 使用display:none技术，只引发两次回流和重绘；
c) 使用cloneNode(true or false) 和 replaceChild 技术，引发一次回流和重绘；
```
3. 不要经常访问会引起浏览器flush队列的属性，如果你确实要访问，利用缓存
```html
// 别这样写，把el.offsetLeft、el.offsetTop的值缓存起来
for(循环) {
el.style.left = el.offsetLeft + 5 + "px";
el.style.top = el.offsetTop + 5 + "px";
}
```

## 总结一下
* 尽量不要在布局信息改变时做查询（会导致渲染队列强制刷新）
* 同一个DOM的多个属性改变可以写在一起（减少DOM访问，同时把强制渲染队列刷新的风险降为0）
* 如果要批量添加DOM，可以先让元素脱离文档流，操作完后再带入文档流，这样只会触发一次重排（fragment元素的应用）
* 将需要多次重排的元素，position属性设为absolute或fixed，这样此元素就脱离了文档流，它的变化不会影响到其他元素。例如有动画效果的元素就最好设置为绝对定位。

## 参考资料
* [高性能JavaScript 重排与重绘](http://web.jobbole.com/83164/)
* [高性能WEB开发](https://kb.cnblogs.com/page/64064/)
* [页面重绘和回流以及优化](http://www.css88.com/archives/4996)
* [从重绘重排角度讲解transform的动画性能](https://segmentfault.com/a/1190000008650975)