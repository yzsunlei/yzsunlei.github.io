---
layout: post
title: 《Web异步与实时交互》阅读记录
category: 阅读
tag: iFrame, Ajax, WebSocket
exception: 本书以介绍iFrame、AJAX和WebSocket三项Web异步交互技术为基本主线，进一步对iFrame、AJAX和WebSocket分别通过轮询、长轮询、长连接和推送方式，实现Web交互时的性能进行测试和深入分析，推荐前端进阶学习。
readtime: 16
---

# Web异步交互技术：iFrame、Ajax、WebSocket
* iFrame：将iFrame的src属性设置为另外一个页面的连接请求，并在当前页面中通过JavaScript动态更新iFrame的内容
* Ajax：通过异步通信和响应，来完成页面的局部刷新
* WebSocket：在浏览器和服务器之间构建一条全双工的通信连接，可以支持服务器端向客户端主动推送信息，实现实时刷新页面的功能

# Web实时交互方式：轮询、长轮询、长连接及推送
* 轮询：定时发送请求->马上进行响应->关闭连接
* 长轮询：发送请求->请求阻塞，保持连接->有数据时需要响应->关闭连接
* 长连接：发送请求->请求阻塞，保持连接->有数据时需要响应->保持住连接
* 推送：建立连接->有数据时就推送

# iFrame实现模拟异步交互
* 核心原理：通过iFrame框架可以在当前页面中显示其他页面的信息
* 具体过程：将iFrame的src属性设置为对另外一个页面的长连接请求，并在当前页面中通过JavaScript动态更新iFrame的内容，即可将服务器端响应的数据无刷新显示在主页面
* 应用场景：聊天室、实时状态监控、股票行情等
* 相关技术：DOM操作，iFrame标签，服务器请求
* 关键模块：定时向服务器发送请求，接受服务器端返回的信息，展示服务器端返回的信息
* 代码示例：[01.iframe-random.html](https://github.com/yzsunlei/yzsunlei.github.io/blob/master/_codes/Web%E5%BC%82%E6%AD%A5%E4%B8%8E%E5%AE%9E%E6%97%B6%E4%BA%A4%E4%BA%92/01.iframe-random.html)、[01.iframe-random.php](https://github.com/yzsunlei/yzsunlei.github.io/blob/master/_codes/Web%E5%BC%82%E6%AD%A5%E4%B8%8E%E5%AE%9E%E6%97%B6%E4%BA%A4%E4%BA%92/01.iframe-random.php)

# AJAX实现异步后台传输技术
* 核心原理：AJAX通过真正的异步通信和响应，来完成页面的局部刷新
* 具体过程：客户端通过XHR加载一个AJAX引擎；AJAX引擎创建一个异步调用的对象，并向Web服务器发出一个HTTP请求；Web服务器端接收到请求后，对该请求进行处理；Web服务器将处理结果以XML等形式返回给AJAX引擎；AJAX引擎接收到返回的结果后，通过JavaScript调用DOM模型显示在浏览器上
* 应用场景：大多数需要实时异步交互的场景
* 相关技术：XMLHttpRequest对象，jQuery库，Pushlet框架
* 关键模块：使用XHR对象异步发送请求至服务器；服务器接收请求处理好数据并返回结果；客户端通过DOM技术将结果局部更新于页面上
* 代码示例：[03.ajax-random.html](https://github.com/yzsunlei/yzsunlei.github.io/blob/master/_codes/Web%E5%BC%82%E6%AD%A5%E4%B8%8E%E5%AE%9E%E6%97%B6%E4%BA%A4%E4%BA%92/03.ajax-random.html)、[03.ajax-random.php](https://github.com/yzsunlei/yzsunlei.github.io/blob/master/_codes/Web%E5%BC%82%E6%AD%A5%E4%B8%8E%E5%AE%9E%E6%97%B6%E4%BA%A4%E4%BA%92/03.ajax-random.php)

# WebSocket实现主动推送交互
* 核心原理：WebSocket通过一个单一的套接字在Web上进行操作，以最小的开销高效地保持了Web连接
* 具体过程：浏览器端及时提交请求，服务器收到请求后阻塞，并保持连接，等待有消息需要发送时，及时向浏览器端进行响应推送
* 应用场景：媒体聊天，实时状态监控，股票行情，基于位置的应用等需要实时刷新的应用场景
* 相关技术：WebSocket协议
* 关键模块：使用onopen事件建立WebSocket连接后触发；使用sendMessage事件将数据发送到服务器端；使用Set集合处理所有的端点实例；使用broadcast事件将消息发送到Set集合中的所有人
* 代码示例：[05.websocket-random.html](https://github.com/yzsunlei/yzsunlei.github.io/blob/master/_codes/Web%E5%BC%82%E6%AD%A5%E4%B8%8E%E5%AE%9E%E6%97%B6%E4%BA%A4%E4%BA%92/05.websocket-random.html)、[05.websocket-random.php](https://github.com/yzsunlei/yzsunlei.github.io/blob/master/_codes/Web%E5%BC%82%E6%AD%A5%E4%B8%8E%E5%AE%9E%E6%97%B6%E4%BA%A4%E4%BA%92/05.websocket-random.php)

# 参考资料
* [Web异步与实时交互 iframe AJAX WebSocket开发实战](http://product.dangdang.com/1272638240.html)
* [HTML5数据推送应用开发](https://book.douban.com/subject/26148767/)
* [HTML5服务器推送消息的各种解决办法](http://www.cnblogs.com/Herzog3/p/5939144.html)
* [HTML5 服务器推送事件（Server-sent Events）实战开发](https://www.ibm.com/developerworks/cn/web/1307_chengfu_serversentevent/)
* [HTML5+规范：Push(管理推送消息功能)](http://blog.csdn.net/qq_27626333/article/details/51823302)
* [Web端即时通讯技术盘点：短轮询、Comet、Websocket、SSE](http://www.52im.net/thread-336-1-1.html)
* [SSE技术详解：一种全新的HTML5服务器推送事件技术](https://zhuanlan.zhihu.com/p/21639227)