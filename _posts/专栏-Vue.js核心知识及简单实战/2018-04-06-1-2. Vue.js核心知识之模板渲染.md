---
layout: post
title: 1-2. Vue.js核心知识之模板渲染
category: Vue.js核心知识及简单实战
tag: vue
exception: Vue.js 使用了基于 HTML 的模板语法，允许开发者声明式地将 DOM 绑定至底层 Vue 实例的数据。所有 Vue.js 的模板都是合法的 HTML ，所以能被遵循规范的浏览器和 HTML 解析器解析。
readtime: 8
---

## 插值
```html
<!-- 随变量msg的值进行更新 -->
<p>普通文本，双向绑定: {{ msg }}</p>
<!-- 不随msg的值进行更新 -->
<p v-once>普通文本，单次绑定: {{ msg }}</p>
<!-- 可以输出带html标签的富文本 -->
<p>输出html代码: <span v-html="rawHtml"></span></p>
<!-- 按钮是否可用取决于变量isDisabled转换的布尔取值 -->
<button v-bind:disabled="isDisabled">动态改变属性值</button>
<!-- 显示'是'还是'否'取决于变量value的布尔取值 -->
<p>{{ value ? '是' : '否' }}</p>
<!-- 字符串反转，如果message的值是123，则显示321 -->
<p>{{ message.split('').reverse().join('') }}</p>
```

## 条件
`vue`中使用`v-if`、`v-else`和`v-else-if`来实现条件渲染
```html
<!-- 当isOk为真时显示是，为假时显示否-->
<p>
 <span v-if="isOk">是</span>
 <span v-else>否</span>
</p>
<!-- 条件渲染分组，当isRender为真时，才会去渲染里面的DOM内容 -->
<template v-if="isRender">
 <h1>标题</h1>
 <p>段落 1</p>
 <p>段落 2</p>
</template>
```
另一个用于根据条件展示元素的方法是使用`v-show`
```html
<!-- 当isShow为真时，显示DOM内容 -->
<h1 v-show="isShow">显示内容</h1>
```
`v-if` 是惰性的，如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块。
`v-show` 就简单得多，不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。

## 列表
`vue`中使用 `v-for` 把数组渲染成选项列表。`v-for` 指令需要使用 `item in items` 形式的特殊语法，`items` 是源数据数组，`item` 是数组元素迭代的别名。
```html
<!-- 把items数组渲染成列表 -->
<ul id="list">
 <li v-for="item in items">
  {{ item.message }}
 </li>
</ul>
<!-- items数组中的数据 -->
<script>
  new Vue({
   el: '#list',
   data: {
    items: [
     { message: '列表项1' },
     { message: '列表项2' },
     { message: '列表项3' },
    ]
   }
  })
</script>
```
也可以用 `v-for` 通过一个对象的属性来迭代。
```html
<!-- 将object对象的属性渲染成列表 -->
<ul id="object">
 <li v-for="value in object">
  {{ value }}
 </li>
</ul>
<!-- object对象中的数据渲染成列表 -->
new Vue({
 el: '#object',
 data: {
  object: {
   firstName: 'John',
   lastName: 'Doe',
   age: 30
  }
 }
}
```

## 指令
指令 (`Directives`) 是带有 `v-` 前缀的特殊属性。当指令对应的表达式的值改变时，将其产生的连带影响，响应式地作用于 `DOM`。
```html
<!-- 变量seen的值影响p标签的渲染 -->
<p v-if="seen">现在你看到我了</p>
<!-- 变量url的值就是a标签的链接地址 -->
<a v-bind:href="url">这里是个链接</a>
<!-- 变量doSomething是一个函数，a标签点击时会触发运行doSomething函数 -->
<a v-on:click="doSomething">点击触发事件</a>
<!-- prevent修饰符作用是阻止默认表单提交事件 -->
<form v-on:submit.prevent="onSubmit">修饰符作用</form>
```

## 小结
本节主要学习了`vue`模板渲染的几种形式：文本插值、属性渲染、条件渲染、列表渲染和指令改变渲染。我们通过这些渲染方式就可以轻松的通过数据控制页面的显示内容了。