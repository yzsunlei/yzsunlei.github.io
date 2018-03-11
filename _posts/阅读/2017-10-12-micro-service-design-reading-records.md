---
layout: post
title: 《微服务设计》阅读记录
category: 编程
tag: 架构
exception: 国庆的第五天跟朋友一起吃饭，聊到了微服务设计，主要是服务集成和拆分方面的，还是很皮毛吧。于是花了些时间看了《微服务设计》这本书，下面记录一下
readtime: 15
---

# 内容
* 以架构师的角度开始
* 围绕项目的建模、集成、拆分、部署、测试、监控等整个生命周期一一展开
* 还讲了项目安全、缓存、持续集成、规模化等专题
* 整体上感觉就是系统化的一个脉络，每个点都是浅浅额的带过

# 不够精深
* 要深入理解微服务，还得去读《领域驱动设计》等
* 要懂得如何应用大量服务的快速发布，还得去阅读《持续交付》等
* 要玩转测试，还需要去阅读《敏捷软件测试》
* 要保证大量服务交付的稳定性，还需要去阅读《Release It！》
* 反正这本书只是让你有个了解

# 接触到的工具或系统
* ssh-multiplexers工具，在多个主机上运行相同的命令
* logstash可以解析多种日志文件格式
* Kibana是一个基于ElasticSearch查看日志的系统
* Graphite允许你实时发送指标数据给他
* 安装Collectd，发现系统生成大量的指标
* Metrics库帮助服务发送指标到一个标准系统中
* Zipkin可以跨多个系统边界跟踪调用
* Riemann事件服务器，允许高级的聚合和事件路由

# 杂七杂八
* 高类聚、低耦合
* Misic Corp
* 领域驱动设计
* 通信方式的选择：SOAP、XML-RPC、REST、Protocol Buffers
* varnish Http缓存代理、mod_proxy负载均衡器
* 《企业集成模式》
* 版本号格式：MAIJOR、MINIMOR、PATCH
* Cassandra
* 使用构建流水线建模的标准发布流程：编译及快速测试、耗时测试、用户验收测试、性能测试、生产环境
* Heroku
* 《持续交付》
* 《敏捷软件测试》
* Pact消费者驱动的测试工具
* 单元测试、服务测试、端到端测试

# 参考
* [《微服务设计》豆瓣读书](https://book.douban.com/subject/26772677/)
* [微服务架构设计](http://www.cnblogs.com/wintersun/p/6219259.html)
* [什么时候你不应该使用微服务](http://www.ituring.com.cn/article/217430)