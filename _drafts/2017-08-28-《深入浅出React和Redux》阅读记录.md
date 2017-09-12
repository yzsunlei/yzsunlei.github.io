---
layout: post
title: 《深入浅出React和Redux》阅读记录
category: 阅读
tag: React, Redux
exception: 
readtime: 18
---

# React组件
* React.createClass 是一种过时的方法

# 从Flux到Redux
* Flux：对数据的更严格的管理
* Flux应用包含四个部分：
   Dispatcher：处理动作分发，维持Store之间的依赖关系
   Store：负责存储数据和处理数据的相关逻辑
   Action：驱动Dispatcher的JavaScript对象
   View：视图部分，负责显示用户界面
* Flux的基本原则：单向数据流
* Redux的基本原则：
  唯一数据源(Single Source of Truth)
  保持状态只读(State is read-only)
  数据改变只能通过纯函数完成(Changes are made with pure functions)

* dispatcher、emit、on、broadcast区分
