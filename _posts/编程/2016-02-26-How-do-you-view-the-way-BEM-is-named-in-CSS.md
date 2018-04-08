---
layout: post
title: 如何看待 CSS 中 BEM 的命名方式
category: 编程
tag: css
exception: 现代的Web应用可以执行强大的操作和提供丰富的交互性，很多逻辑从服务器端迁移到浏览器端，那组织和管理大量的JavaScript和CSS代码就是一个复杂的问题了。下面我们看看CSS的一种方法学
readtime: 8
---

## BEM的定义
* 最早Yandex公司推出时的官方描述：BEM是一种让你可以快速开发网站并对此进行多年维护的技术
* BEM最新的推广页中，对其的描述：BEM是一种命名方法，能够帮助你在前端开发中实现可复用的组件和代码共享

## BEM的组成部分
* BEM的名称来源于三个组成部分的英文首字母，分别是块(Block)、元素(Element)、修饰符(Modifier)

## 块
* 块即通常所说的Web应用开发中的组件或模块
* 每个块在逻辑上和功能上都是相互独立的，可以在应用开发中进行复用
* 块可以放置在页面上的任何位置，也可以互相嵌套
* 同一个块可以在页面上存在多个实例

## 元素
* 元素是块中的组成部分
* 元素不能离开块来使用
* 不推荐在元素中嵌套其他元素

## 修饰符
* 修饰符用来定义块或元素的外观和行为
* 同样的块在应用不同的修饰符之后，会有不同的外观

## 实例
```css
.menu {
 list-style: none;
}
.menu__item {
 font-weight: bold;
}
.menu__item--selected {
 color: red;
}
```

## 命名规则
* BEM实体名称全部是小写字母或数字。名称中的不同单词用单个连字符(-)分隔
* BEM元素名称和块名称之间通过两个下划线(__)分隔
* 布尔修饰符和其所修饰的实体名称之间通过两个连字符(--)来分隔。不使用名值对修饰符

## 解决的问题
* 开发的组件，在现有页面中测试都没有问题，在新页面使用这个组件时，页面样式都变了，原因是弹窗组件和该页面的样式相互覆盖了
* 新同事接手跟进需求，对样式进行修改，由于选择器是一连串的结构逻辑，看不过来，嫌麻烦，就干脆在样式文件最后用另一套选择器，加上了覆盖样式，最后导致一个元素对应多套样式

## 参考资料
* [BEM开发模式](http://www.ayqy.net/blog/bem%E5%BC%80%E5%8F%91%E6%A8%A1%E5%BC%8F/)
* [从 BEM 谈大型项目中 CSS 的组织和管理](https://www.ibm.com/developerworks/cn/web/1512_chengfu_bem/)
* [CSS命名规范-BEM](https://www.cnblogs.com/coder-zyz/p/6749295.html)
* [如何看待 CSS 中 BEM 的命名方式？](https://www.zhihu.com/question/21935157)
* [BEM: A New Front-End Methodology](https://coding.smashingmagazine.com/2012/04/a-new-front-end-methodology-bem/)
* [CSS with BEM](https://en.bem.info/methodology/css/)