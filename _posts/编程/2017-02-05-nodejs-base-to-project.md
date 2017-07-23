---
layout: post
title: nodejs从入门到项目
category: 编程
tag: nodejs
exception: nodejs从入门到项目视频学习记录
readtime: 20
---

## 简介
* 易扩展、适用于现代web应用通信的服务器平台

## 主要应用领域
* RESTFul API
* 实时通信：如消息推送
* 高并发
* I/O阻塞

## 国内外的应用情况
* Linkedin移动版
* Paypal
* Twitter的队列
* 知乎的推送
* 阿里

## 知名度较高的开源项目
* express：有名的web开发框架
* PM2：管理进程
* jade：流行的模板引擎
* socket.io：实时通讯
* mongoose：mongo数据库处理
* mocha：功能强大的测试框架

## Node.js的优点
* 部署简单方便
* 事件驱动
* 异步编程
* 高效与性能
* 单线程与多线程

## Node.js的缺点
* 大量采用匿名函数，使得抛出的异常不易阅读
* try/catch限于同步代码，使得异常捕获较为复杂
* 单线程：可靠性
* 不适合CPU密集型的场景
* 回调的代码习惯影响阅读

## web全栈
* HTML/CSS页面的构建
* 浏览器端的开发
* 服务器端的开发
* 数据库的管理
* 服务器运维

## node.js的执行环境
* Google V8
* 文件系统
* 网络功能(HTTP/TCP/UDP/DNS/TLS/SSL)
* 二进制数据
* 数据流
* 加密与解密

## node.js开发环境构建
* Mac OS上：Xcode、homebrew、nodejs、mongodb、redis、sublime、webstorm
* Windows上：VirtualBox、虚拟机CentOS安装、xShell与xFtp、node.js、MongoDB、Redis、sublime、webstorm

## 使用loopback快速搭建用户系统
* express是内核：不应该直接使用在商业项目、粒度太小、使用者需要handle太多细节
* loopback是工具：mvc框架、loopback组件

## koa入门到应用
* 简介：express原班人马打造、致力于成为更小、更具有表现力、更健壮的web框架
* koa VS express（共同点）：都是对HTTP Request和HTTP Response两个对象进行封装和处理，应用的生命周期维护以及视图的处理等；
* koa VS express（不同点）：Express主要基于Connect中间件框架，功能丰富，随取随用，并且框架自身封装了大量便利的功能。而Koa主要基于co中间件框架，框架自身并没有集成太多功能，大部分功能需要用户自行require中间件去解决，基于ES6 generator特性的中间件机制，解决了长期诟病的"callback hell"和麻烦的错误处理问题
* 官网地址：[koa-基于node.js平台下一代web开发框架](http://koa.bootcss.com/)

## 简单的node.js爬虫系统
* 所需要的模块：express、request、cheerio
* 项目实例：[实现爬取极客学院课程目录](https://github.com/yzsunlei/nodejs-demo/tree/easy-spider)

















