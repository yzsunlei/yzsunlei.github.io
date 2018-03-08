---
layout: post
title: 怎样避免重复发送Ajax请求的总结
category: 编程
tag: Ajax
exception: 在软件开发工作中，经常会遇到后台接口慢，用户在前台连续点击按钮请求数据导致系统问题的情况，今天一起总结整理一下如何处理重复发送Ajax请求的问题
readtime: 12
---

## 分析说明
* 最原始的防止重复提交的方式是点击之后让按钮不可点，还有使用定时器器或变量来记录Ajax请求的状态以用来判断重复点击时是否发送请求
* 具体处理效果需要根据实际场景，像评论post请求需要限制只允许请求一次，像获取列表get请求有的需要第一次请求的结果后面的请求抛弃，有的需要最后一次请求结果等情况

## 解决方案整理
* 只允许同时存在一次提交，并且直到本次完成才能进行下一次提交(缺点：可能导致长时间等待)
```javascript
module.submit = function() {
  if (this.promise_.state() === 'pending') {
    return
  }
  return this.promise_ = $.post('/api/save')
}
```
* 无限制的提交，但以最后一次操作为准（点赞、取消点赞操作，tab切换请求接口场景）
```javascript
module.submit = function() {
  if (this.promise_.state() === 'pending') {
    this.promise_.abort()
  }
  // todo
}
```
* 以一定频率提交，任意两次有效提交的间隔时间必定会大于或等于某一时间间隔(应用于频繁触发的事件，如resize、scroll、mousemove)
```javascript
module.submit = throttle(150, function() {
  // todo
})
```
* 任何两次提交的间隔时间，必须大于一个指定时间
```javascript
module.submit = debounce(150, function() {
  // todo
})
```
* 对于同样的参数，返回始终结果是恒等的，每次返回同一个对象(知乎人士写的，先记着，不太明白)
```javascript
var scrape = memoize(function(url) {
  return $.post('/scraper', { 'url': url })
})
```

* 把连续的多次提交合并为一个提交
```javascript
var makePile = function(count, onfilter, onvalue) {
  var values = [], id = function(value) { return value }
  return function(value) {
    values.push((onvalue || id).apply(this, arguments))
    if (values.length === count) {
      onfilter.apply(this, values)
      values = []
    }
  }
}
```

# 参考资料
* [怎样防止重复发送 Ajax 请求？](https://www.zhihu.com/question/19805411)
* [AJAX防重复提交的办法总结](https://www.cnblogs.com/qinxingnet/p/5748171.html)
* [防止重复发送 Ajax 请求的解决方案](http://www.hollischuang.com/archives/931)
* [ajax防止重复提交的办法](https://my.oschina.net/u/1540325/blog/486308)