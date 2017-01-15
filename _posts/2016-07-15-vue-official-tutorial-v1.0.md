---
layout: post
title: Vue1.0学习笔记
---

# 安装
* 兼容性：不支持IE8及其以下版本，因为Vue使用了IE8不能实现的ECMAScript特性，Vue支持所有兼容ECMAScript 5的浏览器
* 使用方式：独立版本、CDN、NPM、命令行、Bower

# 起步
* Vue的目标是通过尽可能简单的API实现响应的数据绑定和组合的视图组件
* jQuery手工操作DOM时，我们的代码常常是命令式、重复的与易错的
* Vue的核心是一个响应的数据绑定系统，它让数据与DOM保持同步非常简单
* 如果在实例创建之后添加新的属性实例上，它不会触发新的视图更新
* 钩子的`this`指向调用它的Vue实例
* Vue没有控制器概念，组件的自定义逻辑可以分割在这些钩子中
* Vue模板从根本上不同于基于字符串的模板
* Vue指令和特殊特性内不能用插值
* 计算属性(`computed`) VS. `$watch`
* 我们可以传给`v-bind`一个对象，以动态的切换`class`

# 数据绑定
* 文本插值,使用`Mustache`语法(双大括号) `{{msg}}`
* 也可只处理单次插值，今后的数据变化就不会引起更新了`{{* msg}}`
* 为了输出真的HTML字符串，需要用三`Mustache`标签`{{{raw_html}}}`
* 标签可以绑定表达式，也可以使用过滤器;一个限制是每个绑定只能包含单个表达式
* 两种最常用的指令提供缩写: `v-bind:href => :href` `v-on:click => @click`

# 计算属性
* 将绑定限于一个表达式，当需要多个表达式的逻辑时，应当使用计算属性`computed`
* 计算属性默认只是个单向，在需要时也可以提供一个`setter`(双向依赖计算属性)

# Class、Style样式绑定
* 数据绑定一个常见需求是操作元素的`class`列表和它的内联样式
* 不推荐使用`class="{{ className }}"`来绑定class
* 推荐传给`v-bind:class`一个对象,以动态的切换`class`;`v-bind`指令可以与普通的class特性共存
* 传数组给`v-bind:class`，以应用一个class列表 eg: `v-bind:class="[classA, classB]"`
* 直接绑定样式对象：`v-bind:style="styleObject"`
* `v-bind:style` 使用厂商前缀的CSS属性,Vue会自动侦测并添加相应的前缀

# 条件渲染
* 多个元素: 在`<template>`元素作为包装元素，并在上面使用`v-if`
* `v-show`的元素会始终渲染并保持在DOM中，它是简单的切换元素的CSS属性display
* 将`v-show`用在组件上时，因为指令的优先级`v-else`会出现问题；解决:用另一个`v-show`替换`v-else` eg: `v-show="!condition"`
* `v-if` VS. `v-show`：
* `v-if`有更高的切换消耗而`v-show`有更高的初始渲染消耗
* `v-if`是惰性的：如果在初始化渲染时条件为假，则什么也不做，在条件第一次变为真时才开始局部编译(编译会缓存起来)
* `v-show`简单的多，元素始终被编译与保留，只是简单的基于CSS切换

# 列表渲染
* `v-for` 基于一个数组渲染一个列表，`template v-for`以渲染一个包含多个元素的块
* 数组变动检测 Vue包装的方法:`push` `pop` `shift` `unshift` `splice` `sort` `reverse`，会触发视图更新
* 变异方法，修改了原始数组，也有非变异方法(`filter`,`concat`,`slice`)不会修改原始数组
* 因为JavaScript的限制，Vue不能检测到下面数组变化：直接用索引设置元素，解决它Vue扩展了观察数组,为它添加了`$set`方法；修改数据的长度，解决他，只需要用一个空数组替换
* 添加的`$set`和`$remove`方法用于从目标数组中添加和移除元素，在内部实现上调用的是`splice`
* 对象`v-for`除了`$index`外，作用域内还可以访问`$key`变量
* 值域`v-for`:重复遍历 `v-for="n in 10"`

# 方法、事件处理
* `v-on`指令监听DOM事件 eg: `v-on:click="say('hi')"`
* 有时需要在内联语句处理器中访问原生DOM事件，可以用特殊的`$event`把它传入方法
* 提供两个事件修饰符: `.prevent`(取消默认)与`.stop`(阻止冒泡)
* 侦听键盘事件，经常需要检测`keyCode`
* Vue允许为`v-on`添加按键修饰符 `v-on:keyup.13="submit"`
* 记住`keyCode`比较困难，常用的按键提供别名:`enter,tab,delete,esc,space,up,down,left,right`
* V1.08+支持单字母按键别名;V1.0.17+可以自定义按键别名`Vue.directive('on').keyCodes.f1 = 112`
    
# 表单控件绑定
* 默认情况下，`v-model`在`input`事件中同步输入框值与数据，可以添加一个特性`lazy`，从而改到`change`事件中同步
* `debounce`设置延时，在每次敲击之后延时同步输入框的值和数据(不会延迟`input`事件，延迟"写入"底层数据)

# 过渡
* 过渡系统：可以在元素从DOM中插入或移除时自动应用过渡效果
* `transition`特性可与下面资源一起使用:
* `v-if`; `v-show`;  `v-for`(只在插入和删除时触发); 动态组件; 在组件的根节点上,并被Vue实例DOM方法触发
* 过渡的CSS类名的添加和切换取决于`transtion`特性的值 

# 组件
* 组件可以扩展HTML元素,封装可重用的代码
* 在较高层面,组件是自定义元素,Vue的编译器为它添加特殊功能
* 组件实例的作用是孤立的
* `prop`默认是单向绑定的:当父组件的属性变化时，将传导给子组件，但反过来不会
* 这是为了防止子组件无意修改父组件的状态，也可以使用`.sync`或`.once`绑定修饰符显式地强制双向或单次绑定
* `<child :msg="parentMsg"></child>` //默认单向绑定
* `<child :msg.sync="parentMsg"></child>` //双向绑定
* `<child :msg.once="parentMsg"></child>` //单次绑定
* 子组件可以用`this.$parent`访问它的父组件;
* 根实例的后代可以用`this.$root`访问它
* 父组件有一个数组`this.$children`包含它的所有子元素
* 每一个Vue实例都是一个事件触发器
* 使用`$on()`监听事件; 
* 使用`$emit()`在它上面触发事件; 
* 使用`$dispatch()`派发事件,事件沿着父链冒泡;
* 使用`$broadcast()`广播事件,事件向下传导给所有的后代
* 不同于DOM事件,Vue事件在冒泡过程中第一次触发回调之后自动停止冒泡,除非回调明确返回true

# 响应式原理
* Vue.js最显著的一个功能是响应系统--模型只是普通对象，修改它则更新视图
* 受ES5的限制,Vue.js不能检测到对象属性的添加或删除;属性必须在data对象上才能让vue.js转换它,才能让它是响应的
* 有办法在实例创建后添加属性并且让它是响应的 `$set(key, value)`
* 对于普通数据对象，可以使用全局方法`Vue.set(object, key, value)`
* 有时想向已有对象上添加一些属性,比如使用`Object.assign()`或者`_.extend()`添加属性。这样添加的不会触发更新
* //不使用 `Object.assign(this.someObject, {a: 1, b: 2})`
* //使用 `this.someObject = Object.assign({}, this.someObject, {a: 1, b: 2});`
* Vue默认异步更新DOM，每当观察到数据变化时，Vue就开始一个队列，将同一事件循环内所有的数据缓存起来
* 为了在数据变化之后等待Vue.js完成更新DOM，可以在数据变化之后立即使用`Vue.nextTick(callback)`

# 自定义指令
* 自定义指令提供一种机制将数据的变化映射为DOM行为
* `vue.directive(id, definition)` 方法注册一个全局自定义指令，接收两个参数，指令ID和定义对象
* 也可以用组件的directives选项注册一个局部自定义指令
* 定义对象可以提供几个钩子函数：`bind`, `update`, `unbind`
* vue通过递归遍历DOM树来编译模块

# 自定义过滤器
* 使用全局方法`Vue.filter()`注册一个自定义过滤器，接收两个参数：过滤器ID和过滤器函数
* 可以接收任意数量的函数
* 双向过滤器 `read: function(val){} write: function(val, oldVal){}`
* 如果过滤器参数没有用引号包起来，则它会在当前的vm作用域内动态计算

# 混合
* 混合对象可以包含任意的组件选项，当组件使用了混合对象时，混合对象的所有选项都将被"混入"组件自己的选项中
* 当混合对象与组件包含同名选项时，这些选项将以适当的策略合并
* 同名钩子函数被并入一个数组，因而都会被调用
* 值为对象的选项(`methods`,`components`,`directives`)将合并到同一个对象中，如果键冲突则组件的选项优先
* 注意vue.extend()使用同样的合并策略
* 自定义选项合并，向`Vue.config.optionMergeStrategies`添加一个函数

# 插件
* Vue.js插件应当有一个公开方法install，方法的第一个参数是vue构造器
* 通过Vue.use方法全局使用插件
* vue-router：官方路由，与Vue.js内核深度整合，让构建单页应用易如反掌
* vue-resource：通过XMLHttpRequest或JSONP发起请求并处理响应
* vue-async-data：异步加载数据插件
* vue-validator：表单验证插件
* vue-devtools：Chrome开发者工具扩展，用于调试vue.js应用
* vue-touch：使用Hammer.js添加触摸手势指令
* vue-element：使用vue.js注册自定义元素
* vue-animated-list：方便的为v-for渲染的列表添加动画

# 大型应用
* 使用脚手架工具vue-cli可以快速地构建项目：单文件vue组件，热加载，保存时检查代码，单元测试

# 框架对比
* Angular
  在API与设计方面vue都比angular简单的多;
  vue更加灵活开放;
  Angular使用双向绑定，vue也支持双向绑定，不过默认是单向绑定是，数据从父组件单向传给子组件;
  vue中指令和组件分的更清晰;
  vue有更好的性能，非常容易优化，因为不使用脏检查

* React
  一些相似：都提供数据驱动、可组合搭建的视图组件
  许多不同：n内部实现本质不同

  React团队计划让React成为通用平台的UI开发工具，而Vue专注于为web提供实用的解决方案；
  React函数式特质，可以很好的使用函数式编程模式，初级开发难度
  vue有自己的状态管理方案vuex，而且也可以与Re读写一起用；
  React的开发趋势是将所有东西都放在JavaScript中，包括CSS，有问题，脱离了标准的CSS开发经验

* Ember
  全能框架，提供大量的约定，一旦熟悉，开发会很高效，学习曲线较高，而且不灵活

* Polymer
  实际上也是Vue.js的灵感来源之一，vue.js组件可以类比为polymer中的自定义元素
  最大的不同在于，Polymer依赖最新的web组件特性，在不支持的浏览器中，需要加载笨重的polyfill
  性能受到影响，相对的，vue.js无需任何依赖，最低兼容到IE9

* Riot
  Riot 2.0提供类似的基于组件的开发模式(Riot称之为"标签"),API小而美，在设计思路上与Vue有许多相同点

# 不太清楚的API
* [Vue.mixin](http://cn.vuejs.org/api/#Vue-mixin)
* [props](http://cn.vuejs.org/api/#props)
* [vm.$refs](http://cn.vuejs.org/api/#vm-refs)
* [vm.$interpolate](http://cn.vuejs.org/api/#vm-interpolate)
* [vm.$emit](http://cn.vuejs.org/api/#vm-emit)
* [vm.dispatch](http://cn.vuejs.org/api/#vm-dispatch)
* [vm.broadcast](http://cn.vuejs.org/api/#vm-broadcast)
* [vm.$mount](http://cn.vuejs.org/api/#vm-mount)
* [v-cloak](http://cn.vuejs.org/api/#v-cloak)
* [slot](http://cn.vuejs.org/api/#slot)
* [partial](http://cn.vuejs.org/api/#partial)