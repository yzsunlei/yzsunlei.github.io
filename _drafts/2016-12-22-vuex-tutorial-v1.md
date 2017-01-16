# Vuex 教程(v1.0)
* Author：RaySun
* Date：2016/12/22

# 简介
* 专为vue.js应用所设计的集中式状态管理架构
* 单独使用vue的时候，通常会把状态储存在在组件的内部。为了解决大型应用中状态的共用问题，需要对组件的组件本地状态和应用层级状态进行区分
* 核心：State(状态)、Mutations(变更)、Actions(动作)
* 组件不允许直接修改store实例的状态（vuex状态的所有改变都必须在store的mutation handle-变更句柄中管理）
* Mutations本质上是一个事件系统：每个mutation都有一个事件名(name)和一个回调函数(handle)
* vuex store可以接受`middlewares`选项来加载中间件，vuex中自带logger中间件用于debugging
* 实例时传入`strict:true`，每当vuex state在mutayion handlers外部被改变时都会抛出错误(不要在生产环境开启)
* 

