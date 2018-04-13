---
layout: post
title: 1-5. Vue.js核心知识之组件化
category: Vue.js核心知识及简单实战
tag: vue
exception: 组件 (Component) 是 Vue.js 最强大的功能之一。组件可以扩展 HTML 元素，封装可重用的代码。
readtime: 12
---

## 组件的创建和注册
我们可以使用 `Vue.component(tagName, options)`注册一个全局组件。
```html
<!--全局注册-->
<template>
  <div id="app">
    <my-component></my-component>
  </div>
</template>

<script>
  // 全局注册组件
  Vue.component('my-component', {
    template: '<div>我的组件</div>'
  })

  // 创建根实例
  new Vue({
    el: '#app'
  })
</script>

<!--渲染后的HTML-->
<div id="app">
  <div>我的组件</div>
</div>
```
我们还可以通过某个 `Vue` 实例/组件的实例选项 `components` 注册仅在其作用域中可用的组件，即局部组件。
```html
<!--局部注册-->
<template>
  <div id="app">
    <my-component></my-component>
  </div>
</template>
<script>
  var Child = {
    template: '<div>我的组件</div>'
  }

  new Vue({
    el: '#app',
    components: {
      // 局部注册组件，<my-component> 将只在父组件模板中可用
      'my-component': Child
    }
  })
</script>

<!--渲染后的HTML-->
<div id="app">
  <div>我的组件</div>
</div>
使用prop
组件实例的作用域是孤立的。父组件的数据需要通过 prop 才能下发到子组件中。

<!--静态prop-->
<template>
  <child message="哈喽"></child>
</template>
<script>
  Vue.component('child', {
    // 声明 props
    props: ['message'],
    // 就像 data 一样，prop 也可以在模板中使用
    // 同样也可以在 vm 实例中通过 this.message 来使用
    template: '<span>{{ message }}</span>'
  })
</script>
```
如果想要传递一个变量到子组件中去，即传给子组件的值会跟随父组件中该变量的值的变化而变化，我们可以用 `v-bind` 来动态地将 `prop` 绑定到父组件的数据。
```html
<!--动态prop-->
<template>
  <div id="dynamic-prop">
    <input v-model="parentMsg">
    <br>
    <child v-bind:my-message="parentMsg"></child>
  </div>
</template>
<script>
  new Vue({
    el: '#dynamic-prop',
    data: {
      parentMsg: '父组件发过来的消息'
    }
  })
</script>
```
我们还可以为组件的 `prop` 指定验证规则。如果传入的数据不符合要求，`Vue` 会发出警告。这对于开发给他人使用的组件非常有用。
```html
<!--prop验证-->
<script>
  Vue.component('example', {
    props: {
      // 基础类型检测 (`null` 指允许任何类型)
      propA: Number,
      // 可能是多种类型
      propB: [String, Number],
      // 必传且是字符串
      propC: {
        type: String,
        required: true
      },
      // 数值且有默认值
      propD: {
        type: Number,
        default: 100
      },
      // 数组/对象的默认值应当由一个工厂函数返回
      propE: {
        type: Object,
        default: function () {
          return { message: 'hello' }
        }
      },
      // 自定义验证函数
      propF: {
        validator: function (value) {
          return value > 10
        }
      }
    }
  })
</script>
```

## 自定义事件进行组件通讯
现在我们父组件可以使用 `prop` 传递数据给子组件。但子组件怎么跟父组件进行通信呢？这里我们可以通过自定义事件来实现。

具体点说就是使用 `$on(eventName)` 监听事件，使用 `$emit(eventName, optionalPayload)` 触发事件。
```html
<template>
  <div id="message-event">
    <p v-for="msg in messages">{{ msg }}</p>
    <button-message v-on:message="handleMessage"></button-message>
  </div>
</template>
<script>
  Vue.component('button-message', {
    template: `<div>
    <input type="text" v-model="message" />
    <button v-on:click="handleSendMessage">发送消息</button>
  </div>`,
    data: function () {
      return {
        message: '哈喽'
      }
    },
    methods: {
      handleSendMessage: function () {
        this.$emit('message', { message: this.message })
      }
    }
  })

  new Vue({
    el: '#message-event',
    data: {
      messages: []
    },
    methods: {
      handleMessage: function (payload) {
        this.messages.push(payload.message)
      }
    }
  })
</script>
```

## 使用插槽分发内容
为了让组件可以自由组合，我们需要一种方式来混合父组件的内容与子组件自己的模板。这个过程被称为内容分发。我们可以使用特殊的 `<slot>` 元素作为原始内容的插槽，从而实现内容分发。

如果子组件模板包含一个 `<slot>` 插口，那么父组件的内容将会被渲染到插槽中。
```html
<!--子组件模板-->
<templalte>
  <div>
    <h2>子组件的标题</h2>
    <slot>
      只有在没有要分发的内容时才会显示。
    </slot>
  </div>
</templalte>

<!--父组件模板-->
<template>
  <div>
    <h1>父组件的标题</h1>
    <my-component>
      <p>这是将会分发到子组件的一些初始内容</p>
    </my-component>
  </div>
</template>

<!--渲染后的HTML-->
<div>
  <h1>父组件的标题</h1>
  <div>
    <h2>子组件的标题</h2>
    <p>这是将会分发到子组件的一些初始内容</p>
  </div>
</div>
```
当需要有多个插槽时，我们可以在`<slot>` 元素上用一个特殊的特性 `name` 来进一步配置如何分发内容。多个插槽配置不同的名字，这时具名插槽将匹配内容片段中有对应 `slot` 特性 `name` 的元素。
```html
<!--layout 子组件模板-->
<template>
  <div class="container">
    <header>
      <slot name="header"></slot>
    </header>
    <main>
      <slot></slot>
    </main>
    <footer>
      <slot name="footer"></slot>
    </footer>
  </div>
</template>

<!--父组件模板-->
<template>
  <layout>
    <h1 slot="header">头部标题</h1>

    <p>主体内容的一个段落。</p>

    <p slot="footer">尾部版权信息</p>
  </layout>
</template>

<!--渲染后的HTML-->
<div class="container">
  <header>
    <h1>头部标题</h1>
  </header>
  <main>
    <p>主体内容的一个段落。</p>
  </main>
  <footer>
    <p>尾部版权信息</p>
  </footer>
</div>
```

## 总结
本节主要知识点是`vue.js`中组件的创建和注册，父组件使用`prop`向子组件传递数据并进行数据验证，使用自定义事件进行组件间的通讯，使用插槽来使组件可以自由组合。`vue.js`组件是`vue`框架中最强大的功能，学完后相信你对web组件化也会有一定的了解了。

