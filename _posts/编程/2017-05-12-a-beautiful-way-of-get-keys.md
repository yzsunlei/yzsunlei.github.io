---
layout: post
title: 获取对象的所有key的一种巧妙方法
category: 编程
tag: JavaScript
exception: 
readtime: 2
---

```html
Object.keys || function() {
	var arr = [];
	// 很巧妙的方法
	for (arr[arr.length] in Object);
}
```
