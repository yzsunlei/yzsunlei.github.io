---
layout: post
title: 面向对象的CSS解读
category: 编程
tag: CSS
exception: 任何基于面向对象的代码方法，其主要目的都是鼓励代码的复用。OOCSS也是一样，讲究复用，并最终可以更快更高效的书写你的样式，同时方便日后的添加和维护...
readtime: 15
---

## 概念解读
* OO CSS将页面可重用元素抽象成一个类，用class加以描述，而与其对应的HTML即可看成是此类的一个实例
* OO CSS的作用：加强代码复用以便方便维护、减少CSS体积、提升渲染效率、组件库思想、栅格布局可共用、减少选择器、方便扩展
* 常用库：reset.css 、normalize.css 、 neat.css

## Less使用
* Less将css赋予了动态语言的特性，如变量、继承、运算、函数，less可以在客户端上运行，也可以借助node.js或者rhino在服务端运行
* 使用方式一：通过node.js，安装less(`npm install -g less`)，通过手动编译(`lessc style.less > style.css`)或grunt、gulp、webpack监控文件变化动态编译
* 使用方式二：通过引入less样式文件和less.js文件(`<link type="text/css href="index.less /> <script type="text/javascript" href="less.min.js"></script>`)

## Scss使用
* Scss是基于ruby的
* 安装方式：先安装ruby（mac系统自带ruby），然后通过`gem install sass`进行安装
* 使用方式：在node.js环境中通过手动编译（`sass index.sass index.css`）或者通过grunt、gulp、webpack监控文件变化动态编译

## stylus使用
* Stylus默认使用`.styl`作为文件扩展名
* 安装方式：通过`npm install stylus -g`安装
* 使用方式：在命令行中使用`stylus --compress src/`编译或者通过grunt、gulp、webpack前端自动化工具进行自动监控编译

## 参考资料
* [Less文档教程](http://less.bootcss.com/#)
* [Sass入门教程](http://www.w3cplus.com/sassguide/)
* [stylus中文文档](http://www.zhangxinxu.com/jq/stylus/)
* [详细比较三个CSS预处理器(框架)：Sass、Less、Stylus](http://www.oschina.net/question/12_44255?sort=default&p=4)