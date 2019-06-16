---
layout: post
title: JavaScript常用6大继承方式解析
category: 编程
tag: JavaScript
exception: 
readtime: 15
---

## 原型链继承
```javascript
//父类
function Person(name, age) {
   this.name = name;
   this.age = age;
   this.play = [1, 2, 3];
   this.setName = function () { }
}
Person.prototype.setAge = function () { }
//子类
function Student(price) {
   this.price = price;
   this.setScore = function () { }
}
Student.prototype = new Person() // 核心，子类型的原型为父类型的一个实例对象
var s1 = new Student(15000)
var s2 = new Student(14000)
console.log(s1,s2)
```

* 说明：
    实现的本质是通过将子类的原型指向了父类的实例。所以子类的实例就可以通过__proto__访问到 Student.prototype 也就是Person的实例，
    这样就可以访问到父类的私有方法，然后再通过__proto__指向父类的prototype就可以获得到父类原型上的方法。
    子类继承父类的属性和方法是将父类的私有属性和公有方法都作为自己的公有属性和方法。

* 特点：
    父类新增原型方法/原型属性，子类都能访问到
    简单，易于实现
    
* 缺点：
    无法实现多继承
    来自原型对象的所有属性被所有实例共享
    创建子类实例时，无法向父类构造函数传参
    要想为子类新增属性和方法，必须要在Student.prototype = new Person() 之后执行，不能放到构造器中

## 构造函数继承
```javascript
function Person(name, age) {
    this.name = name,
    this.age = age,
    this.setName = function () {}
}
Person.prototype.setAge = function () {}
function Student(name, age, price) {
    Person.call(this, name, age)  // 核心，相当于: this.Person(name, age)
    /*this.name = name
    this.age = age*/
    this.price = price
}
var s1 = new Student('Tom', 20, 15000)
```

* 说明：
    就是将子类中德变量在父类中执行一遍。只能继承父类的属性和方法，如果父类的原型还有方法和属性，子类是拿不到的。
    
* 特点：
    解决了原型链继承中子类实例共享父类引用属性的问题
    创建子类实例时，可以向父类传递参数
    可以实现多继承(call多个父类对象)
    
* 缺点：
    实例并不是父类的实例，只是子类的实例
    只能继承父类的实例属性和方法，不能继承原型属性和方法
    无法实现函数复用，每个子类都有父类实例函数的副本，影响性能

## 组合继承
```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
    this.setAge = function () { }
}
Person.prototype.setAge = function () {
    console.log("111");
}
function Student(name, age, price) {
    Person.call(this,name,age);//核心
    this.price = price;
    this.setScore = function () { }
}
Student.prototype = new Person();//核心
Student.prototype.constructor = Student//核心，组合继承是需要修复构造函数指向的
Student.prototype.sayHello = function () { }
var s1 = new Student('Tom', 20, 15000);
var s2 = new Student('Jack', 22, 14000);
console.log(s1);
console.log(s1.constructor); //Student
console.log(s2.constructor); //Person
```

* 说明：
    融合原型链继承和构造函数的优点，并过滤掉其缺点，是 JavaScript 中最常用的继承模式。
    先在使用构造函数继承时执行一遍父类的构造函数，又在实现子类原型的原型链继承时又调用一遍父类构造函数。

* 优点：
    可以继承实例属性/方法，也可以继承原型属性/方法
    不存在引用属性共享问题
    可传参
    函数可复用

* 缺点：
    调用了两次父类构造函数，生成了两份实例

## 原型式继承
```javascript
function createObj(o) {
    function F(){}
    F.prototype = o;
    return new F();
}
```

* 说明：
    实际上是对原型链继承的一个封装，也是ES5 Object.create 的模拟实现，将传入的对象作为创建的对象的原型。
    
* 特点：
    父类新增原型方法/原型属性，子类都能访问到
    简单，易于实现
    
* 缺点：
    包含引用类型的属性值始终都会共享相应的值，这点跟原型链继承一样。

## 寄生式继承
```javascript
function createObj (o) {
    var clone = Object.create(o);
    clone.sayName = function () {
        console.log('hi');
    }
    return clone;
}
```

* 说明：
    其实是对原型式继承的第二次封装，过程中对继承的对象进行了拓展。
    
* 特点：
    跟借用构造函数模式一样，每次创建对象都会创建一遍方法。
    
* 缺点：

## 寄生组合式继承
```javascript
function object(o) {
    function F() {}
    F.prototype = o;
    return new F();
}

function prototype(child, parent) {
    var prototype = object(parent.prototype);
    prototype.constructor = child;
    child.prototype = prototype;
}

// 使用时
prototype(Child, Parent);
```

* 说明：
    解决了组合继承存在的问题
    
* 特点：
    只调用了一次 Parent 构造函数，并且因此避免了在 Parent.prototype 上面创建不必要的、多余的属性
    原型链还能保持不变
    还能够正常使用 instanceof 和 isPrototypeOf
    
* 缺点：


## 参考资料
* [https://www.cnblogs.com/humin/p/4556820.html](https://www.cnblogs.com/humin/p/4556820.html)
* [https://github.com/mqyqingfeng/Blog/issues/16](https://github.com/mqyqingfeng/Blog/issues/16)
* [https://segmentfault.com/a/1190000016708006](https://segmentfault.com/a/1190000016708006)
* [http://es6.ruanyifeng.com/#docs/class-extends](http://es6.ruanyifeng.com/#docs/class-extends)