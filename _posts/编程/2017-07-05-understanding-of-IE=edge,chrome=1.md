---
layout: post
title: 关于content=IE=edge,chrome=1的理解
category: 编程
tag: html
exception: 关于content=IE=edge,chrome=1的理解
readtime: 5
---
## GCF的定义
* 可使用开放式网络技术（如 HTML5 canvas 标记）立即启动，甚至包括 Internet Explorer 6、7 或 8 尚不支持的技术。
* 利用 JavaScript 性能增强功能，使应用程序速度更快，响应更灵敏。

## 具体介绍
1. 如果支持Google Chrome Frame：GCF，则使用GCF渲染；
2. 如果系统安装ie8或以上版本，则使用最高版本ie渲染；
3. 否则，这个设定可以忽略。

## 参考资料
* [content = "IE=edge,chrome=1" 详解](http://www.cnblogs.com/alwaysfly/p/metachome1.html)
* [关于content=”IE=edge,chrome=1″介绍-让网页优先采用Chrome渲染](http://blog.csdn.net/u014398624/article/details/51252268)