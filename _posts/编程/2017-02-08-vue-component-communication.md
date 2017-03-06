---
layout: post
title: Vue组件通信方式总结
category: 编程
tag: vue
exception: 现在在做vue构建的项目时候，我们都知道要灵活使用vue的组件特性，将公用的代码提取出来，放在组件中，以提高代码的复用率。但组件与组件之间需要传递数据时，如果没有弄清vue组件通信的方法，就显得很吃力了。最近我总结了下这方面的知识，下面归类分享一下..
readtime: 5
---

## props绑定
* 最常用的props属性绑定，不仅能实现父组件向子组件的传递数据，也能实现子组件向父组件传递数据的双向绑定。
{% highlight bash lineno %}
<children :msg="将数据传递到子组件"></children> //简单的值传递
<children :msg="parentMsg"></children> //动态值传递
<children :msg.once="parentMsg"></children> //只传递一次，当parentMsg变化时，不会再次传递
<children :msg.sync="parentMsg"></children> //双向绑定，父组件中的parentMsg变化时，子组件中的msg会随之变化，同样，子组件中的msg变化，父组件中的parentMsg值也会随之变化
{% endhighlight %}
## 自定义事件
* 使用$on()在它上面监听事件
* 使用$emit()在它上面触发事件
* 使用$dispatch()派发事件，事件沿着父链冒泡
* 使用$broadcast()广播事件，事件向下传导给所有的后代
* 派发事件实例如下：
{% highlight bash lineno %}
<!-- 子组件模板 -->
<template id="child-template">
  <input v-model="msg">
  <button v-on:click="notify">派发事件</button>
</template>
<!-- 父组件模板 -->
<div id="events-parent">
  <p>获得的值: {{ messages | json }}</p>
  <child></child>
</div>
<!-- 具体实现 -->
// 注册子组件
// 将当前消息派发出去
Vue.component('child', {
  template: '#child-template',
  data: function () {
    return { msg: 'hello' }
  },
  methods: {
    notify: function () {
      if (this.msg.trim()) {
        this.$dispatch('child-msg', this.msg)
        this.msg = ''
      }
    }
  }
})
// 初始化父组件
// 将收到消息时将事件推入一个数组
var parent = new Vue({
  el: '#events-parent',
  data: {
    messages: []
  },
  // 在创建实例时 `events` 选项简单地调用 `$on`
  events: {
    'child-msg': function (msg) {
      // 事件回调内的 `this` 自动绑定到注册它的实例上
      this.messages.push(msg)
    }
  }
})
{% endhighlight %}
* 以上实例，当按钮被点击时，会执行notify方法，notify方法中会携带msg变量的值触发自定义事件child-msg，并沿着父链传递，父组件中定义了child-msg事件，此时，该事件触发函数执行将msg的值加入messages数组

* 广播事件实例如下：
{% highlight bash lineno %}
<!-- 父组件代码(parent.vue) -->
<template>
<div id="app">
	<input v-model="newItem" @keyup.enter="addNew"/>
</div>
</template>
<script>
export default {
	new Vue({
	    el: '#app',
		methods: {
		  addNew: function() {
		    this.$broadcast('onAddnew', this.items)
		  }
		}
	})
}
</script>
<!-- 子组件1中代码(child1.vue) -->
<script>
export default {
	events: {
	    'onAddnew': function(items){
	      console.log("子组件1中获得数据：" + items)
	    }
	}
}
</script>
<!-- 子组件2中代码(child2.vue) -->
<script>
export default {
	events: {
	    'onAddnew': function(items){
	      console.log("子组件2中获得数据：" + items)
	    }
	}
}
</script>
{% endhighlight %}
* 以上实例中，当父组件按enter触发addNew方法后，addNew方法会广播onAddnew自定义事件，并携带items变量，这时事件会通知到当前实例的全部后代，当子组件1和子组件2收到onAddnew事件，就会触发对应的函数，输出收到的变量值

## 通过实例来访问
* this.$parent访问它的父组件，根实例的后代可以用$root访问它，父组件有一个数组this.$children包含它所有的子元素

## 子组件索引
* 在父组件上通过v-ref注册一个子组件的索引，就可以直接方便的访问子组件的数据
* 实例代码如下：
{% highlight bash lineno %}
<template>
<div id="parent">
    <child v-ref:child03></child>
    <child v-ref=child04></child>
</div>
<template>
<script>
export default {
    new vue({
        el: "",
        data: function() {
            return {
                msg: ""
            }
        },
        method: {
            getChildInfo: function() {
                var child03 = this.$refs.child03; // 获取子组件child03对象
                var child04 = this.$refs.child04; // 获取子组件child04对象
            }
        }
    })
}
</script>
{% endhighlight %}
* 以上代码就可以直接获取child03组件和child04组件对象

## 总结一下
* 实际项目中，我们一般都是使用前两种方式，即通过props绑定和自定义事件来完成父子组件之间的数据传递，后两种方式，即通过实例和通过索引ref虽然操作起来更简单，但违背了vue组件化的思想，即组件的状态需要自身来维护或变更，最好不要让其他组件也能修改当前组件的数据或状态，这样容易造成混乱

## 资料参考
* [vue官方教程-组件](http://v1-cn.vuejs.org/guide/components.html)
* [vue跨组件通信的几种方法](http://www.tuicool.com/articles/jyM32mA)
* [vue.js组件与组件之间的通信](http://blog.csdn.net/qq_24122593/article/details/53010758)