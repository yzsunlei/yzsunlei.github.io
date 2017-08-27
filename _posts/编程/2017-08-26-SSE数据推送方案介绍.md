---
layout: post
title: SSE数据推送方案介绍
category: 编程
tag: SSE, WebSocket
exception: 传统的网页都是浏览器向服务器“查询”数据，但是很多场合，最有效的方式是服务器向浏览器“发送”数据。今天我们来了解一些HTML5中的一种数据推送方法
readtime: 15
---

# SSE原理
* WebSocket 的一种轻量代替方案，使用 HTTP 协议
* HTTP 协议是没有办法做服务器推送的，但是当服务器向客户端声明接下来要发送流信息时，客户端就会保持连接打开

# SSE用途
* 更新频繁、低延迟的场景，统计数据实时情况的应用
* 邮箱服务的新邮件提醒，微博的新消息推送、管理后台的一些操作实时同步等

# SSE相对于WebSocket的优势
* 实现一个完整的服务仅需要少量的代码；
* 可以在现有的服务中使用，不需要启动一个新的服务；
* 可以用任何一种服务端语言中使用；
* 基于 HTTP／HTTPS 协议，可以直接运行于现有的代理服务器和认证技术。

# 简单的实例
* 客户端代码
```html
<div id="x">Initializing...</div>
```
```javascript
  var es = new EventSource("http://127.0.0.1:1234");
  var es = new EventSource("01.basic_sse.php");
  es.addEventListener("message", function (e) {
    document.getElementById('x').innerHTML += "\n" + e.data;
  }, false);
```
* 服务端代码
```php
// php后端
header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');

$time = date('r');
// data:前缀和\n\n后缀是SSE协议规范所要求的
echo "data: The server time is: {$time}\n\n";
flush();
```

# 向下兼容
* 请参考实例：[数据推送应用开发实例](https://github.com/yzsunlei/yzsunlei.github.io/tree/master/_codes/%E6%95%B0%E6%8D%AE%E6%8E%A8%E9%80%81%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91)

# 参考资料
* [《HTML5数据推送应用开发》](https://book.douban.com/subject/26148767/)
* [SSE：使用 HTTP 做数据推送应用](https://segmentfault.com/a/1190000010427711)
* [使用服务器发送事件](https://developer.mozilla.org/zh-CN/docs/Server-sent_events/Using_server-sent_events)
* [使用“个推”实现手机应用的消息推送](https://segmentfault.com/a/1190000006776809)