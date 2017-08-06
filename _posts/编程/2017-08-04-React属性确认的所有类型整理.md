---
layout: post
title: React属性确认的所有类型整理
category: 编程
tag: react
exception: React Native创建的自定义组件可以复用，一个项目组可能有多个人同时开发，为了统一规范或避免出错，我们需要在自定义组件中声明一些属性。
readtime: 10
---

- 属性为任意类型
```javascript
React.PropTypes.any;
```

- 属性为JavaScript基本类型
```javascript
React.PropTypes.array;
React.PropTypes.string;
React.PropTypes.bool;
React.PropTypes.func;
React.PropTypes.number;
React.PropTypes.object;
```

- 属性为某个元素
```javascript
React.PropTypes.element;
```

- 属性为几个特定的值
```javascript
React.PropTypes.oneOf(['val1', 'val2', 'valn'])
```

- 属性为可渲染的节点
```javascript
Reat.PropTypes.node;
```

- 属性为指定类型中的一个
```javascript
React.PropTypes.oneOfType([
  React.PropTypes.node,
  React.PropTypes.string,
  React.PropTypes.number
])
```

- 属性为某一个指定类的实例
```javascript
React.PropTypes.instanceOf(nameOfClass)
```

- 属性为一个指定构成方式的对象
```javascript
React.PropTypes.shape({
   fontSize: React.PropTypes.number,
   color: React.PropTypes.string
})
```

- 属性为指定类型的数组
```javascript
React.PropTypes.arrayOf(React.PropTypes.string);
```

- 属性有一个指定的成员对象
```javascript
React.PropTypes.objectOf(React.PropTypes.number)
```

