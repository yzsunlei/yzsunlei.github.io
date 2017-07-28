---
layout: post
title: 《深入浅出Node.js》阅读记录
category: 阅读
tag: node
exception: 这本书从不同的视角讲解了node内在的特点和结构，从Node的代码组织结构、运行结构到编程结构、内存结构再到单元测试、工程化、产品化都有细致的讲解，非常值得Node.js初学者花时间去阅读
readtime: 15
---

* 1、node.js的来源、发展做一个流程图
* 2、优势：V8的高性能和异步I/O模型
* 3、书籍结构：代码组织结构、运行结构、编程结构、内存结构、数据在I/O流中的结构或状态、网络服务角度、HTTP上的展现、单机集群结构、单元测试和性能测试、NODE编码产品化
* 4、Node特点：异步I/O、事件和回调函数、单线程、跨平台
* 5、I/O密集型和CPU密集型
* 6、CommonJS缺陷：没有模块系统，标准库较少，没有标准接口，缺乏包管理系统
* 7、CommonJS构建的这套模块导出exports和引入机制require使得用户不必考虑变量污染
* 8、Node中引入模块经历：路径分析，文件定位，编译执行
* 9、核心模块(Node提供的模块，部分被直接加载进内存中)、文件模块(用户编写的模块，引用时需经历8中的三个过程)
* 10、node查找模块的方式：沿路径向上逐级递归，直到根目录下的node_modules目录
* 11、引用文件不包含文件扩展名时，自动按.js、.json、.node的次序去补足扩展名
* 12、模块编译：
     .js文件-通过fs模块同步读取文件后编译执行
     .node文件-通过dlopen()方法加载最后编译生成的文件
     .json文件-通过fs模块同步读取文件后，用JSON.parse()解析返回结果
     其余扩展名文件-都会被当做.js文件载入
* 13、编译过程，头尾包装(function (exports, require, module, __filename, __dirname) {\n ... \n});
* 14、文件模块->核心模块(JavaScript)->内建模块(C/C++)
* 15、AMD规范和CMD规范

* 16、Node：利用单线程，远离多线程死锁、状态同步等问题；利用异步I/O，让单线程远离阻塞，以更好的使用CPU
* 17、Node在*nix平台下采用libeio配合libev实现I/O部分，Windows下的IOCP
* 18、从JavaScript调用Node的核心模块，核心模块调用C++内建模块，内建模块通过libuv进行系统调用，这是Node里经典的调用方式
* 19、事件循环、观察者、请求对象、I/O线程池四者共同构建了Node异步I/O模型的基本要素
* 20、非I/O的异步API：setTimeout、setInterval、setImmediate、process.nextTick
* 21、在每一轮循环检查中，idle观察者先于I/O观察者，I/O观察者先于check观察者。process.nextTick()属于idle观察者，setImmediate()属于check观察者
* 22、Node的异步I/O并非首创，类似的还有Ruby的Event Machine，Perl的AnyEvent，Python的Twisted

* 23、ES5中高阶函数：forEach、map、reduce、reduceRight、filter、every、some
* 24、偏函数？通过指定部分参数来产生一个新的定制函数的形式
* 25、Node带来的最大特性莫过于基于事件驱动的非阻塞I/O模型，这种模型可以使CPU与I/O并不相互依赖等待
* 26、Node在处理上形成的一种约定：将异常作为回调函数的第一个实参传回，如果为控制，则表明异步调用没有异常抛出
* 27、阻塞代码，没有sleep这样的线程沉睡功能，应该调用setTimeout()
* 28、多线程编程，web workers？
* 29、异步编程的主要解决方案：事件发布/订阅模式、Promise/Deferred模式、流程控制库
* 30、如果对一个事件添加了超过10个侦听器，将会得到一条警告，侦听器过多可能导致内存泄漏，可能存在过多占用CPU的情景
* 31、异步并发控制：同步I/O彼此阻塞，总是一个接一个的去调用，因此不会出现耗用文件描述符太多的情况，同时性能是低下的，异步I/O虽然并发容易实现，就需要控制避免系统过载
* 32、bagpipe：通过一个队列来控制并发量
* 33、async也提供了一个方法用于处理异步调用的限制：parallelLimit，没有bagpipe灵活
* 34、协程(coroutine)？ES5不支持
* 35、Promise/Deferred模式：先执行异步调用，延迟传递处理的方式
* 36、流程控制库：尾触发与Next(connect)、async、step

* 37、Node中通过JavaScript使用内存时就会发现只能使用部分内存（64位下约为1.4GB，32位系统下约为0.7GB）
* 38、Node在启动时可以传递--max-old-space-size或--max-new-space-size来调整内存限制的大小

* 40、全停顿：垃圾回收的3种基本算法都需要将应用逻辑暂停下来，待执行完回收后再回复执行应用逻辑
* 41、V8后续还引入延迟清理(lazy sweeping)与增量式整理(incremental compaction),让清理和整理动作也变成增量式的，同时还计划引入并行清理和并行整理
* 42、查看垃圾回收日志：node --trace_gc -e "var a = [];for (var i = 0; i < 1000000; i++) a.push(new Array(100));" > gc.log
* 43、通过赋值方式比delete操作解除引用更好，global.foo = undefined vs delete global.foo
* 44、无法立即回收的内存有闭包和全局变量引用这两种情况
* 45、堆外内存：不是通过V8分配的内存，利用堆外内存可以突破内存限制的问题
* 46、通常，造成内存泄漏的原因有缓存，队列消费不及时，作用域未释放
* 47、较好的缓存方式：redis，memchached
* 48、常用的定位Node应用的内存泄漏工具：v8-profier、node-heapdump、node-mtrace、dtrace、node-memwatch
* 49、Node中提供stream模块用于处理大文件，原生模块

* 50、Buffer对象类似于数组，他的元素是16进制的两位数
* 50、Node采用了slab分配机制，slab是一种动态内存管理机制
* 51、Buffer对象可以与字符串之间相互转换，支持的字符串编码类型：ASCII、UTF-8、UTF-16LE/UCS-2、Base64、Binary、Hex
* 52、使用setEncoding可以处理大部分的乱码问题，使用的string_decoder模块，目前只能处理UTF-8、Base64和UCS-2/UTF-16LE这3种编码
* 53、从根本上上解决Buffer拼接问题是用一个数组来存储接收到的所有片段并记录下所有片段的总长度，然后调用Buffer.concat()方法生成一个合并的Buffer对象
* 54、让客户端输出数据时，通过预先转换静态内容为Buffer对象，可以有效的减少CPU的重复使用，节省服务器资源
* 55、不要将Buffer当做字符串来理解，Buffer是二进制数据，传输效率比原生字符串高，字符串与Buff之间存在编关系

* 57、Node不需要专门的web服务器作为容器
* 58、Node提供了net、dgram、http、https这4个模块，分别用于处理TCP、UDP、HTTP、HTTPS，适用于服务器端和客户端
* 59、手工映射的优点在于路径可以很灵活，但项目越大，路由映射数量越多，难以管理
* 60、RestFul表现层状态转化，设计哲学主要将服务器提供发的内容实体看做一个资源，并表现在URL上
* 68、中间件：简化和隔离基础设施与业务逻辑自检 细节
* 69、开始、请求、访问日志、查询字符串、cookie、其他、业务逻辑
* 70、中间件性能提升点：编写高效的中间件，合理利用路由，避免不必要的中间件执行
* 71、内容响应过程中，响应爆头中的Content-*字段十分重要
* 72、常见响应：MIME指定({'Content-Type': 'text/html'})，附件下载(Content-Disposition: attachment; filename="filename.ext")、响应JSON、响应跳转(res.setHeader('Location', url))
* 73、模板技术：模板语言、模板文件、数据对象、模板引擎
* 74、模板引擎原理：语法分解、处理表达式、生成待执行的语句、与数据一起执行
* 75、Bigpipe几个重要的点：页面布局框架（无数据的）、后端持续性的数据输出、前端渲染

* 76、两个问题：如何充分利用多核服务器？如何保证进程的健壮性和稳定性
* 77、服务模型的变迁：同步(石器时代)、复制进程(青铜时代)、多线程(白银时代)、事件驱动(黄金时代)
* 78、child_process方法：spawn()启动进程来执行命令、exec()启动进程来执行命令，有一个回调函数、execFile()启动一个子进程来执行可执行文件、fork()复制进程
* 79、主线程与工作线程之间通过onmessage()和postMessage()进行通讯，子进程对象则由send()方法实现主进程向子进程发送数据，message事件实现收听子进程发来的数据
* 80、IPC的全称是Inter-Process Communication，即进程间通信
* 81、实现进程建通讯的技术有很多，命名管道、匿名管道、socket、信号量、共享内存、消息队列、Domain socket。
* 82、Node中实现IPC通道的是管道（pipe）技术
* 83、进程事件：error，exit，close，disconnect
* 84、实现状态同步的机制有两种：一种是各个子进程去向第三方进行实时轮询、一种是当数据发生更新，主动通知子进程
* 85、Cluster事件：fork、online、listening、disconnect、exit、setup

* 86、测试包含：单元测试、性能测试、安全测试、功能测试
* 87、单元测试主要包括断言、测试框架、测试用例、测试覆盖率、mock、持续集成等
* 88、探知测试用例对源代码的覆盖率，需要一种工具来统计每一行代码是否执行，相关工具是jscover模块
* 89、利用travis-ci实现持续集成
* 90、Connect或Express提供了supertest辅助库来简化单元测试的编写
* 91、压力测试考查的几个指标：吞吐率、响应时间和并发数，最常用的工具ab、siege、http_load

* 92、所谓的工程化，可以理解为项目的组织能力
* 93、项目工程化最基本的几步：目录结构、构建工具、编码规范、代码审查
* 94、编码规范的两种方式：一种是文档式的约定，一种是代码提交时的强制检查

* 95、Node调试工具：Debugger、Node Inspector



