---
layout: post
title: 怎么用js将网页保存成图片
category: 编程
tag: JavaScript
exception: 最近需要做的一个功能，就是能够通过程序将网页截取下来保存为图片，一时不知道怎么做，就在网上学习了一下，总结如下
readtime: 15
---

## 实现简介(两种方法)
1. 使用html2canvas.js，原理是通过脚本收集所有元素的信息，然后用它来构建页面的表示，换句话说，实际上并没有截取页面的截图，而是基于它从DOM中读取的属性来构建它的表示
2. 使用PhantomJS.js，PhantomJS是一款JavaScript API的无头WebKit脚本。它具有对各种web标准的快速和本地支持：DOM处理，CSS选择器，JSON，Canvas和SVG

## 使用html2canvas.js
* 简单实例
```javascript
html2canvas(document.body).then(function(canvas) {
    document.body.appendChild(canvas);
});
```
* 限制：脚本使用的所有图像需要在同一个位置；脚本不能呈现插件内容，如Flash或Java小程序

## 使用PhantomJS.js
* 简单实例
```javascript
var page = require('webpage').create();

page.settings.userAgent = 'WebKit/534.46 Safari/7534.48.3';
page.settings.viewportSize = { width: 400, height: 600 };

var s_url = "";

page.open(s_url, function (status) {
    if (status !== 'success') {
    console.log('Unable to load!');
    phantom.exit();
  } else {
    window.setTimeout(function () {
      page.render("a.jpg");
        phantom.exit();
    }, 5000);
  }
});
```

## 参考资料
* [NodeJS + PhantomJS 抓取页面信息以及截图](http://www.cnblogs.com/justany/p/3279717.html)
* [js将html生成为图片，并保存在本地](https://blog.csdn.net/yyhlichao/article/details/51889161)
* [PhantomJS将网页保存为图片](https://blog.csdn.net/magic_wings/article/details/54764268)
* [JS如何导出Div的内容为图片](https://blog.csdn.net/fengyao1995/article/details/51842486)