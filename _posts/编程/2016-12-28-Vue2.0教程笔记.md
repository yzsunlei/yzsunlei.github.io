---
layout: post
title: Vue2.0教程笔记
category: 编程
tag: vue
exception: Vue.js是一套构建用户界面的渐进式框架，采用自底向上增量开发的设计。Vue的核心库只关注视图层，非常容易去学习，另外，vue完全有能力驱动采用单文件组件和vue生态系统支持的库开发的复杂单页应用。
readtime: 10
---

#  模板语法
* `v-once`执行一次性插值，当数据改变时，插值处的数据对象不会更新
* `v-html`输出真正的HTML，双大括号会将数据解释为纯文本
* 双大括号不能在HTML属性中使用，应使用`v-bind`
* `：`和`@`可以很好的替代`v-bind`和`v-on`

# 计算属性
* 计算缓存VS`Methods`：计算属性是基于它的依赖缓存的，依赖的变量没变，直接返回缓存的值，而`method`总会执行函数
* 计算属性VS`watch`：通常使用计算属性而不是使用命令式的`$watch`回调
* 计算属性默认只有`getter`，不过需要时也可以使用提供的`setter`

# Class与Style绑定
* `v-bind:style`使用需要特定前缀的CSS属性时，如`transform`，Vue会自动侦测并添加相应的前缀

# 数据渲染
* `v-for`中可以用`of`替代`in`作为分隔符，它最接近javascript迭代器的语法
* Vue不能检测到数组变动的两种情况：直接设置一个项的索引`vm.items[indexOfItem] = newValue`；修改数组长度时`vm.items.length = newLength`
* 在文本区域插值`<textarea></textarea>`并不会生效，应用`v-model`来代替

# 事件处理器
* 用特殊变量`$event`把原生DOM事件传入方法，如：`v-on:click="warn('!', $event)"`，在`warn`中就可以接受`event`参数，调用`event.preventDefault()`
* 事件修饰符：`.stop`阻止事件冒泡，`.prevent`阻止默认事件，`.capture`使用事件捕获模式，`.self`限制只当事件在该元素本身触发

# 表单控件绑定
* 修饰符：`v-model.lazy`转变为在`change`事件中同步，`v-model.number`自动转为数字，`.trim`自动过滤用户输入的首尾空格
* `{{selected}}`当值为数组时，会渲染出数组形式`["A"，“B”]`

# 组件
* 父子组件的关系可以总结为：`props down、events up`。父组件通过`props`向下传递数据给子组件，子组件通过`events`给组件发送消息
* 父子组件改为单向通讯，这意味着你不应该在子组件内部改变`prop`
* 组件可以为`props`指定验证要求，`type`可以是`String、Number、Boolean、Function、Object、Array`
* 在某个组件的根元素上监听一个原生事件，可以使用`.native`修饰`v-on`
* `keep-alive`可以把切换出去的组件保留在内存中，保留状态避免重新渲染
* Vue组件的API来自三部分：`Props`(允许外部环境传递数据给组件)、`Events`(允许组件触发外部环境的副作用)、`Slots`(允许外部环境将额外的内容组合在组件中)
* 使用`v-once`的低级静态组件：当组件中包含大量静态内容时，可以考虑使用`v-once`将渲染结果缓存起来

# 深入响应式原理
* 追踪变化：将普通的`javascript`对象传给Vue实例作为它的`data`选项，Vue将遍历它的属性，用`Object.defineProperty`将他们转为`getter/setter`，但这个不支持`IE8`（哈哈）
* 变化检测：Vue不能检测到对象属性的添加或删除，现在JavaScript的限制以及`Object.observe`的废弃
* 使用`Object.assign()`或`_.extend()`方法添加到对象上的新属性不会触发更新
* `Vue.nextTick(callback)`在数据变化之后等待Vue完成更新DOM之后调用回调；`this.$nextTick`在组件中使用，回调`this`将自动绑定到当前的Vue实例上

# 过渡效果
* 工具：在CSS过渡和动画中自动应用class；可以配合使用第三方CSS动画库（如`Animate.css`）；在过渡钩子函数中使用JavaScript直接操作DOM；可以配合使用第三方JavaScript动画库（如`Velocity.js`）

# 过渡状态
* Vue的过渡系统提供了非常多简单的方法设置进入、离开和列表的动效

# Render函数
* Vue的模板实际上是编译成了`render`函数

# 自定义指令
* 指令定义的钩子函数：`bind`（第一次绑定到元素时调用）、`inserted`（被绑定元素插入**父节点**时调用）、`update`（被绑定元素所在的模板更新时调用）、`componentUpdated`（被绑定模板完成一次更新周期时调用）、`unbind`（指令与元素解绑时调用）
* 钩子函数的参数：`el`、`binding`、`vnode`、`oldVnode`

# 混合
* 同名钩子函数混合成一个数组，都将被调用。混合对象的钩子将在组件自身钩子之前调用
* 混合对象可以包含任意组件选项
* 同名钩子函数将混合成数组，都将被调用，混合对象的钩子将在组件自身钩子之前调用，如`created`
* 可以全局注册混合对象(`Vue.mixin`)、也可以自定义选项混合策(`Vue.config.optionMergeStrategies`)

# 插件
* 插件通常会为Vue提供全局功能
* 插件分类：添加全局方法或者属性、添加全局资源（指令/过滤器/过渡等）、通过全局`mixin`方法添加组件选项、添加Vue实例方法（通过添加到`Vue.prototype`上实现）、一个提供自己API的库
* 插件应当有一个公开方法`install`
* 插件使用通过全局方法`Vue.use()`，自动阻止注册多次

# 单文件组件
* 弊端：全局定义（每个`component`命名不得重复）；字符串模板（缺乏模板高亮和使用丑陋的换行`\`）；不支持CSS（组件化时CSS被遗漏）；没有构建步骤（不能使用预处理器`Pug`和`Babel`等）

# 生产环境部署
* 为了减少文件大小，Vue精简独立版本已经删掉所有警告。当使用`Webpack`或`Browserify`等工具需要进行额外的配置
* 使用单文件组件时，`<style>`标签在开发过程中会被动态实时注入。生产环境需要从所有组件提取样式到单独的CSS文件中

# 路由
* 推荐使用官方的`vue-router`(https://github.com/vuejs/vue-router)
* 整合第三方路由：`Page.js`(https://github.com/visionmedia/page.js)、`Director`(https://github.com/flatiron/director)

# 状态管理
* 组件不允许直接修改属于某个实例的state，而应该执行action来分发(`duspatch`)事件通知实例去改变
* `Vuex`(https://github.com/vuejs/vuex)、`Flux`架构(https://facebook.github.io/flux/)

# 单元测试
* 简单的断言：当测试组件时，所要做的就是导入对象和Vue然后使用许多常见的断言
* 很多组件的渲染输出由它的`props`决定，这样会让测试变得很简单，就像断言不同参数的纯函数的返回值
* 由于Vue进行异步更新DOM，一些依赖DOM更新结果的断言必须在`Vue.nextTick`回调中进行

# 服务器渲染
* 需要服务端渲染（`SSR`）：`SEO`（搜索引擎优化）、客户端的网络比较慢、客户端运行在老的（或者直接没有）JavaScript引擎上、预渲染可以为了特定的路由生成特定的几个静态页面
* 不必担心：一个web服务器、流式响应、组件缓存、构建过程、路由、`Vuex`状态管理
