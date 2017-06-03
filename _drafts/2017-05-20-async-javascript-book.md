---
layout: post
title: JavaScript异步编程
category: 编程
tag: JavaScript
exception: 描述
readtime: 15
---

# 深入理解javascript事件


# 分布式事件


# Promise对象和Deferred对象


# Async.js的工作流进程


# worker对象的多线程技术
* 事件能够代替一种特殊的多线程(或者通过中断技术虚拟实现，或者通过多个CPU内核真正实现)
* 生成worker对象时，只需以脚本URL为参数来调用全局Work构造函数即可
* 网页版worker对象的首要目标是在不损害DOM响应能力的情况下处理复杂的计算
* 网页版worker潜在用法：解码视频，加密通信，Ace编辑器
* work对象可以随意使用XMLHttpRequest
* 网页版worker只是一种性能增强工具，即便window.worker不可用，也可以使用垫片技术？保证目标脚本的正常运行
* 支持多个进程绑定至同一端口的标准API：cluster(群集)
* 运行中的脚本要知道自己是主进程还是worker对象，唯一的办法就是检查cluster.isMaster
* 使用child_process.fork也可以将外部脚本加载为独立的进程来运行
* 主进程必须承担起作为所有线程间通信之中转中心的重任
* 为了减少线程间通信的开销，线程间分享的状态应该存储在像Redis这样的外部数据库中

# 异步的脚本加载
* async/defer属性的作用
* document.write就像操控DOM时的Goto语句
* Async+Defer=？，在同时支持的浏览器中async会覆盖掉defer
* script.onload = function() {}属性，在脚本执行加载完执行
* yepnope条件加载(简单，轻量级)，require.js/AMD智能加载(require不会保证按照顺序运行目标脚本，只是保证他们的运行次序能满足依赖关系)
* 要求根据条件来加载脚本用yepnope，存在大量相互依赖的脚本用require.js
