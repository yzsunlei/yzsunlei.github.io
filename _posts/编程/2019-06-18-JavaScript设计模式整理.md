---
layout: post
title: JavaScript设计模式整理
category: 编程
tag: JavaScript
exception: 
readtime: 15
---

## 写在前面
设计模式是程序员通识知识，熟练掌握并使用各种设计模式，可以体现一个程序员的工程开发水平。我花了几天时间，重温并整理了30多种设计模式，以JavaScript为示例语言。下面我会列出一些常用的设计模式说明及示例，更全面的内容见：[https://github.com/yzsunlei/javascript-design-mode](https://github.com/yzsunlei/javascript-design-mode)

## 什么是设计模式？
一个模式就是一个可重用的方案，可应用于在软件设计中的常见问题。另一种解释就是一个我们如何解决问题的模板 - 那些可以在许多不同的情况里使用的模板。 

## 设计模式的分类：
**创建型设计模式：**
1、简单工厂模式 
2、工厂方法模式 
3、抽象工厂模式 
4、建造者模式 
5、原型模式 
6、单例模式 

**结构型设计模式：**
7、外观模式
8、适配器模式
9、代理模式
10、装饰者模式
11、桥接模式
12、组合模式
13、享元模式

**行为型设计模式：**
14、模板方法模式
15、观察者模式
16、状态模式
17、策略模式
18、职责链模式
19、命令模式
20、访问者模式
21、中介者模式
22、备忘录模式
23、迭代器模式
24、解释器模式

**技巧型设计模式：**
25、链模式
26、委托模式
27、数据访问对象模式
28、节流模式
29、简单模板模式
30、惰性模式
31、参与者模式
32、等待者模式

**架构型设计模式：**
33、同步模块模式
34、异步模块模式
35、Widget模式
36、MVC模式
37、MVP模式
38、MVVM模式

* 备注：该分类借鉴于《JavaScript设计模式-张容铭》

## 工厂方法模式：
通过对产品类的抽象使其创建业务主要负责用于创建多类产品的实例。
```
// 安全模式创建的工厂类
var Factory = function(type, content) {
    if (this instanceof Factory) {
        // 保证是通过new进行创建的
        var s = new this[type](content);
        return s;
    } else {
        return new Factory(type, content);
    }
};

// 工厂原型中设置创建所有类型数据对象的基类
Factory.prototype = {
    Java: function(content) {

    },
    Php: function(content) {

    },
    JavaScript: function(content) {

    }
};
```

## 原型模式：
用原型实例指向创建对象的类，使用于创建新的对象的类共享原型对象的属性以及方法。
```
// 图片轮播类
var LoopImages = function(imgArr, container) {
    this.imagesArray = imgArr;
    this.container = container;
};

LoopImages.prototype = {
    // 创建轮播图片
    createImage: function() {
        console.log("LoopImages createImage function");
    },
    // 切换下一张图片
    changeImage: function() {
        console.log("LoopImages changeImage function");
    }
};

// 上下滑动切换类
var SliderLoopImg = function(imgArr, container) {
    // 构造函数继承图片轮播类
    LoopImages.call(this, imgArr, container);
};
SliderLoopImg.prototype = new LoopImages();
// 重写继承的“切换下一张图片”方法
SliderLoopImg.prototype.changeImage = function() {
    console.log("SliderLoopImg changeImage function");
};
```

## 单例模式：
又称单体模式，是只允许实例化一次的对象类。
```
// 惰性
var LarySingle = (function() {
    // 单例实例引用
    var _instance = null;
    // 单例
    function Single() {
        // 这里定义私有属性和方法
        return {
            publicMethod: function() {},
            publicProperty: "1.0"
        };
    }
    // 获取单例对象接口
    return function() {
        // 如果未创建单例将创建单例
        if(!_instance){
            _instance = Single();
        }
        // 返回单例
        return _instance;
    };
})();
```

## 外观模式：
为一组复杂的子系统接口提供一个更高级的统一接口，通过这个接口使得对子系统接口的访问更容易。
```
function addEvent(dom, type, fn) {
    // 对于支持DOM2级事件处理程序addEventListener方法的浏览器
    if (dom.addEventListener) {
        dom.addEventListener(type, fn, false);
    } else if (dom.attachEvent) {
        // 对于不支持addEventListener方法但支持attchEvent方法的浏览器
        dom.attachEvent("on" + type, fn);
    } else {
        // 对于不支持addEventListener方法，也不支持attchEvent方法，但支持“on”+事件名的浏览器
        dom["on" + type] = fn;
    }
}
```

## 装饰者模式：
在不改变原对象的基础上，通过对其进行包装拓展(添加属性或方法)使原对象可以满足用户更复杂需求。
```
var decorator = function (input, fn) {
    // 获取事件源
    var input = document.getElementById(input);
    // 若事件源已经绑定事件
    if (typeof input.click === 'function') {
        // 缓存事件源原有回调函数
        var oldClickFn = input.click;
        // 为事件源定义新的事件
        input.click = function () {
            // 事件源原有回调函数
            oldClickFn();
            // 执行事件源新增回调函数
            fn();
        }
    } else {
        // 事件源未绑定事件，直接为事件源添加新增回调函数
        input.onclick = fn;
    }
}
```

## 观察者模式：
又称发布-订阅者模式或消息机制，定义一种依赖关系，解决了主体对象与观察者之间功能的耦合。
```
var Observer = (function () {
    var __messages = {};
    return {
        // 注册消息
        register: function (type, fn) {
            if (typeof __messages[type] === 'undefined') {
                __messages[type] = [fn];
            } else {
                __messages[type].push(fn);
            }
        },
        // 发布消息
        fire: function (type, args) {
            if (!__messages[type])
                return;
            var events = {
                type: type,
                args: args || {}
            };
            var i = 0;
            var len = __messages[type].length;
            for (; i < len; i++) {
                __messages[type][i].call(this, events);
            }
        },
        // 移除消息
        remove: function (type, fn) {
            if (__messages[type] instanceof Array) {
                var i = __messages[type].length - 1;
                for (; i >= 0; i--) {
                    __messages[type][i] == fn && __messages[type].splice(i, 1);
                }
            }
        }
    }
})();
```

## 状态模式：
当一个对象的内部状态发生改变时，会导致其行为的改变，这看起来像是改变了对象。
```
// 状态对象
var ResultState = function () {
    var States = {
        state0: function () {
            console.log("第一种情况");
        },
        state1: function () {
            console.log("第二种情况");
        },
        state2: function () {
            console.log("第三种情况");
        },
        state3: function () {
            console.log("第四种情况");
        }
    };

    function show(result) {
        States['state' + result] && States['state' + result]();
    }

    return {
        show: show
    }
}();
```

## 命令模式：
将请求与实现解耦并封装成独立对象，从而使不同的请求对客户端的实现参数化。
```
// 绘图命令
var CanvasCommand = (function () {
   var canvas = document.getElementById('canvas');
   var ctx = canvas.getContext('2d');
   var Action = {
       fillStyle: function (c) {
           ctx.fillStyle = c;
       },
       fillRect: function (x, y, w, h) {
           ctx.fillRect(x, y, w, h);
       },
       strokeStyle: function (c) {
           ctx.strokeStyle = c;
       },
       strokeRect: function (x, y, w, h) {
           ctx.strokeRect(x, y, w, h);
       },
       fillText: function (text, x, y) {
           ctx.fillText(text, x, y);
       },
       beginPath: function () {
           ctx.beginPath();
       },
       moveTo: function (x, y) {
           ctx.moveTo(x, y);
       },
       lineTo: function (x, y) {
           ctx.lineTo(x, y);
       },
       arc: function (x, y, r, begin, end, dir) {
           ctx.arc(x, y ,r, begin, end, dir);
       },
       fill: function () {
           ctx.fill();
       },
       stroke: function () {
           ctx.stroke();
       }
   };
   return {
       excute: function (msg) {
           if (!msg)
               return;
           if (msg.length) {
               for (var i = 0, len = msg.length; i < len; i++) {
                   arguments.callee(msg[i]);
               }
           } else {
               msg.param = Object.prototype.toString.call(msg.param) === "[object Array]" ? msg.param : [msg.param];
               Action[msg.command].apply(Action, msg.param);
           }
       }
   }
})();
```

## 迭代器模式：
在不暴露对象内部结构的同时，可以顺序的访问聚合对象内部的元素。
```
// 迭代器
var Iterator = function (items, container) {
    var container = container && document.getElementById(container) || document;
    var items = container.getElementsByTagName(items);
    var len = items.length;
    var idx = 0;
    var splice = [].splice();

    return {
        first: function () {},
        second: function () {},
        pre: function () {},
        next: function () {},
        get: function () {},
        dealEach: function () {},
        dealItem: function () {},
        exclusive: function () {}
    }
};
```

## 链模式：
通过在对象方法中将当前对象返回，实现对同一个对象多个方法的链式调用。
```
var A = function (selector) {
    return new A.fn.init(selector);
};
A.fn = A.prototype = {
    constructor: A,
    init: function (selector) {
        console.log(this.constructor);
    }
};
A.fn.init.prototype = A.fn;
```

## 节流模式：
对重复的业务逻辑进行节流控制，执行最后一次操作并取消其他操作，以提高性能。
```
var throttle = function () {
    var isClear = arguments[0];
    var fn;
    if (typeof isClear === 'boolean') {
        fn = arguments[1];
        fn.__throttleID && clearTimeout(fn.__throttleID);
    } else {
        fn = isClear;
        param = arguments[1];
        var p = extend({
            context: null,
            args: [],
            time: 30
        }, param);
        arguments.callee(true, fn);
        fn.__throttleID = setTimeout(function () {
            fn.apply(p.context, p.args);
        }, p.time);
    }
}
```

## 参与者模式：
在特定的作用域中执行给定的函数，并将参数原封不动的传递。
```
// 函数绑定
function bind(fn, context) {
    return function () {
        return fn.apply(context, arguments);
    }
}

// 函数柯里化
function curry(fn) {
    var Slice = [].slice;
    var args = Slice.call(arguments, l);
    return function () {
        var addArgs = Slice.call(arguments);
        var allArgs = args.concat(addArgs);
        return fn.apply(null, allArgs);
    }
}
```


## 参考资料
* [https://book.douban.com/subject/26589719/](https://book.douban.com/subject/26589719/)
* [https://book.douban.com/subject/26382780/](https://book.douban.com/subject/26382780/)
* [https://www.w3cschool.cn/zobyhd/m1w6jozt.html](https://www.w3cschool.cn/zobyhd/m1w6jozt.html)
* [https://www.cnblogs.com/xiyangbaixue/p/3902699.html](https://www.cnblogs.com/xiyangbaixue/p/3902699.html)