---
layout: post
title: React生命周期详解
category: 编程
tag: react
exception: 所谓生命周期，就是一个对象从开始生成到最后消亡所经历的状态，理解生命周期，是合理开发的关键...
readtime: 15
---

## React生命周期解读
* 所谓生命周期，就是一个对象从开始生成到最后消亡所经历的状态，理解生命周期，是合理开发的关键
* 一个React组件的生命周期分为三个部分：实例化、存在期和销毁时

## 初始化阶段函数介绍
* getDefaultProps：只调用一次，实例之间共享引用
* getInitialState：初始化每一个实例特有的状态
* componentWillMount：render之前的最后一次修改状态的机会
* render：只能访问this.props和this.state，只有一个顶层组件，不允许修改状态和DOM输出
* componentDidMount：成功render并渲染完成真实DOM之后触发，可以修改DOM

##  运行中阶段函数介绍
* componentWillReceiveProps：父组件修改属性触发，可以修改新属性、修改状态
* shouldComponentUpdate：返回false会阻止render调用
* componentWillUpdate：不能修改属性和状态
* render：只能访问this.props和this.state，只有一个顶层组件，不允许修改状态和DOM输出
* componentDidUpdate：可以修改DOM

## 销毁阶段函数介绍
* componentWillUnmount：在删除组件之前进行清理操作，比如定时器和事件监听函数

## 参考资料
* [React.Component - facebook官方文档](https://facebook.github.io/react/docs/react-component.html)
* [理解React生命周期](https://csspod.com/understanding-reactjs-lifecycle-methods/)
* [React源码剖析系列-生命周期的管理艺术](https://www.w3ctech.com/topic/1596)