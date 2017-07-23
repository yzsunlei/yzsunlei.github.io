---
layout: post
title: 获取对象的所有key的一种巧妙方法
category: 编程: 标签
exception: 获取对象的所有key的一种巧妙方法
readtime: 2
---

```html
// 获取对象的所有key的方法
Object.keys || function() {
	var arr = [];
	// 很巧妙的方法
	for (arr[arr.length] in Object);
}
```
