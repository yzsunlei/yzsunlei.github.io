---
layout: post
title: JavaScript中history和hash使用小结
category: 编程
tag: Javascript hash
exception: JavaScript中history和hash使用原理：hash是通过链接#号后面的参数来记录当前页面的状态, 当改变链接#号后面的数据时页面是不会刷新的；pushstate是通过管理浏览器的历史记录来实现的，即将所需的页面状态动态的插入到浏览记录中而页面不刷新；
readtime: 5
---

# 遇到问题
1. 订单查询页面选定条件进行搜索后，刷新页面后又得重选条件进行搜索
2. 选定条件的搜索结果想发给别人看，只能把条件发过去，而不能直接通过发送链接

# 解决方法
HTML5中提供了两种技术进行解决，简要列一下:
1. hash
   * window.location.hash (存, 取)
   * onhashchange (监听事件)
2. pushstate
   * history.pushstate({}, '标题', 'xxx.html') (存, 取)
   * history.replacestate(null, '标题', 'xxx.html') (改)
   * onpopstate (监听事件)

# 原理介绍
* hash是通过链接#号后面的参数来记录当前页面的状态, 当改变链接#号后面的数据时页面是不会刷新的;
* pushstate是通过管理浏览器的历史记录来实现的，即将所需的页面状态动态的插入到浏览记录中而页面不刷新;

# 扩展的东西
* 单页应用、pjax、jquery.uriAnchor.js插件，这些后面再好好看一下

* 单页应用中经常用到ajax每次取数据时页面更新后浏览器并不产生历史记录, 也就是说后退和前进失去应用的效用, 这时可以结合hash和window.onhashchange来使用, 
注意ie6、7均不支持onhashchange, 但可以使用setInterval来定期的检查hash的改变, 或者onload中检查的方法

* 通过ajax异步请求, 同时页面的URL发生变化，并且能够很好的支持浏览器的前进和后退

HTML5有两种解决办法
1. hash
   * window.location.hash (存, 取)
   * onhashchange (监听事件)
2. pushstate
   * history.pushstate({}, '标题', 'xxx.html') (存, 取)
   * history.replacestate(null, '标题', 'xxx.html') (改)
   * onpopstate (监听事件)

* 点击一个站内的链接时, 不是做页面跳转, 而只是站内页面刷新
* ajax刷新是支持浏览器历史的, 刷新页面的同时, 浏览器地址栏上面的地址也是会更改, 用浏览器的回退功能也能够回退到上一个页面
