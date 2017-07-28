---
layout: post
title: 《JavaScript异步编程》阅读记录
category: 阅读
tag: JavaScript
exception: JavaScript异步编程一书，深入讲解了JavaScript事件、Promise对象和Deferred对象、worker对象等常用但又让人陌生的知识，感觉受益匪浅
readtime: 15
---

# 深入理解javascript事件
* Javascript事件处理器在线程空闲之前不会运行
* 异步函数通常可以分为I/O函数和计时函数
* 现代浏览器中操作DOM对象时，从脚本角度看，更改是即时生效的，但从视效角度看，在返回事件队列之前不会渲染这些DOM对象更改
* setInterval触发频率大约为200次/秒，在node环境，大约能达到1000次/秒；while触发频率为400万次/秒，在node环境，会达到500万次/秒
* HTML规范推行的延时/间隔的最小值是4毫秒
* setTimeout和setInterval就是不精确的计时工具
* 要想产生短时延时，Node中process.nextTick,浏览器中，尝试垫片技术(shim)：支持requestAnimationFrame就用它，不支持就用setTimeout
* 利用try/catch语句块并不能捕获从异步回调中抛出的错误
* 只能在回调内部处理源自回调的异步错误
* 如果windows.onerror处理器返回true，则能阻止浏览器的默认错误处理行为
* 在Node环境中，window.onerror的类似物是process对象的uncaughtException事件(自Node 0.8.4起，该事件就被废弃了)
* Domain对象是事件化对象，它将throw转化为'error'事件，请仅在调试时才使用它
* npm的开发负责人就主张try/catch是一种“反模式”的方式，它只是包装着漂亮花括号的goto语句
* JavaScript中最常见的反模式的做法是，回调内部在嵌套回调

# 分布式事件
* PubSub（发布/订阅）模式来分发事件，具体表现：Node的EventEmitter对象，Backbone的事件话模型和jQuery的自定义事件
* jQuery的名称空间化事件(如绑定"click.tbb"和"hover.tbb"两个事件)，backbone.js允许向"all"事件类型绑定事件处理器，这样不管发生什么事，都会导致这些事件处理器的触发
* 老式的JavaScript依靠输入事件的处理器直接改变DOM，新式的JavaScript先改变模型，接着由模型出发事件而导致DOM的更新
* JavaScript确实没有一种每当对象变化时就触发事件的机制？Object.observe的ECMAScript提案已经获得广泛的接纳
* backbone中的两道保险：当新值等于旧值时，set方法不会导致触发change事件；模型正处于自身的change事件期间时，不会再去出发change事件(自保哲学)
* 事件化模型为我们带来一种将应用状态转换为事件的直观方式，运用事件化模型存储互斥数据？
* jQuery简化了强大分布式事件系统向任何web应用程序的移植，jQuery中可以使用trigger方法基于任意DOM元素触发任何想要的事件

# Promise对象和Deferred对象
* jQuery在用语上的不同之处，一是Deferred与Promise之间的区别，二是resolve用作reject的反义词
* Deffered是Promise的超集，它比Promise多一项关键特性，可以直接触发

# Async.js的工作流进程
* 为node.js设计的，直接而强大的JavaScript异步功能
* 函数map、reduce、filter、forEach等，异步流程控制模式：parallel、series、waterfall等

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
