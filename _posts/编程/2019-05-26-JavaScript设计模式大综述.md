---
layout: post
title: JavaScript设计模式大综述
category: 编程
tag: JavaScript
exception: 
readtime: 15
---

* 贴士：示例代码仓库：[https://github.com/yzsunlei/javascript-design-mode](https://github.com/yzsunlei/javascript-design-mode)

## 什么是设计模式？
一个模式就是一个可重用的方案，可应用于在软件设计中的常见问题。另一种解释就是一个我们如何解决问题的模板 - 那些可以在许多不同的情况里使用的模板。 

## 设计模式的分类：
### 创建型设计模式：
* 01、简单工厂模式 

介绍：又叫静态工厂方法，由一个工厂对象决定创建某一种产品对象类的实例。主要用来创建同一类对象。 

示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/01、简单工厂模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/01、简单工厂模式.md)

* 02、工厂方法模式 

介绍：工厂父类负责定义创建产品对象的公共接口，而工厂子类就是负责生成具体的产品对象，这个方法实现的是通过工厂子类可以确定究竟应该实例化哪一个具体产品类。 

示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/02、工厂方法模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/02、工厂方法模式.md)

* 03、抽象工厂模式
介绍：抽象工厂模式实际上是泛化的工厂模式。在抽象工厂模式中的具体产品类可以生产多个具体产品。提供一个创建一系列相关或相互依赖对象的接口，并不需要定义它们具体的类，这就是抽象工厂模式。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/03、抽象工厂模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/03、抽象工厂模式.md)

* 04、建造者模式
介绍：由于组合部件的过程较为复杂，因此，将这些部件的组合过程往往被外部化到一个称作建造者的对象里，建造者返还给客户端是一个完整的对象，而无需关心该对象包含的属性。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/04、建造者模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/04、建造者模式.md)

* 05、原型模式
介绍：用原型实例指定创建对象的种类，并且通过复制这些原型创建新的对象。原型模式允许一个对象再创建另外一个可定制的对象，无须知道任何创建的细节。原型模式的基本工作原理是通过将一个原型对象传给那个要发动创建的对象，这个要发动创建的对象通过请求原型对象复制原型来实现创建过程。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/05、原型模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/05、原型模式.md)

* 06、单例模式
介绍：单例模式确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，它提供全局访问的方法。单例模式的要点有三个：一是某个类只能有一个实例；二是它必须自行创建这个实例；三是它必须自行向整个系统提供这个实例。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/06、单例模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/06、单例模式.md)

### 结构型设计模式：
* 07、外观模式
介绍：外部与一个子系统通信必须通过一个统一的外观对象进行，为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子接口更加容易使用。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/07、外观模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/07、外观模式.md)

* 08、适配器模式
介绍：使原本不兼容的事物一起工作，适配器的存在，就是为了将已存在的东西转换成适合我们的需要、能被我们所利用的东西，使用适配器模式时，客户端一定要针对抽象目标类进行编程。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/08、适配器模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/08、适配器模式.md)

* 09、代理模式
介绍：如果一个客户并不想直接引用一个对象，就可以通过一个称之为“代理”的第三者来实现间接引用。代理对象其实可以看做在客户端和目标对象之间起到中介的作用。给某一个对象提供一个代理，并由代理对象控制对原对象的引用。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/09、代理模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/09、代理模式.md)

* 10、装饰者模式
介绍：在被装饰的类中调用在装饰器类中定义的方法，实现更多更复杂的功能，也就是说装饰模式可以在不需要创造更多子类的情况下，将对象的功能加以扩展。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/10、装饰者模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/10、装饰者模式.md)

* 11、桥接模式
介绍：桥接模式将抽象部分与实现部分分离，使它们都可以独立地变化，将继承关系转换为了关联关系，从而降低了类与类之间的耦合。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/11、桥接模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/11、桥接模式.md)

* 12、组合模式
介绍：动态地给一个对象增加一些额外的职责，就增加对象功能来说，装饰模式比生成子类实现更为灵活。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/12、组合模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/12、组合模式.md)

* 13、享元模式
介绍：主要用于减少创建对象的数量，以减少内存占用和提高性能。运用共享技术有效支持大量细粒度对象的复用。当一个系统有大量相同或相似的对象时可以使用享元模式。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/13、享元模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/13、享元模式.md)

### 行为型设计模式：
* 14、模板方法模式
介绍：定义一个操作中算法的骨架，作为父类模板，在子类中不改变一个算法的结构只是进行重定义该算法的某些特定步骤完成具体算法。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/14、模板方法模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/14、模板方法模式.md)

* 15、观察者模式
介绍：将发生改变的对象成为观察目标，而被通知的对象称为观察者。观察者模式定义了一种对象间的一种一对多依赖关系，使得每当一个对象状态发生改变时，其相关的依赖对象可以得到通知并被自动更新。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/15、观察者模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/15、观察者模式.md)

* 16、状态模式
介绍：一个对象在其内部的状态发生改变时要改变它的行为，即状态和行为不可以分离。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/16、状态模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/16、状态模式.md)

* 17、策略模式
介绍：定义一系列算法，并且进行封装，这样就可以让它们进行相互替换。保证这些策略的一致性，使用一个抽象类做算法的定义。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/17、策略模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/17、策略模式.md)

* 18、职责链模式
介绍：职责链可以使一条直线，一个环或者一个树形结构，沿着这条单向的链来传递请求，而链上的每一个对象都是请求处理者，职责链模式将请求的处理者组织成一条链，并使请求沿着链传递，由链上的处理者对请求进行相应的处理。职责链模式避免了请求发送者与接受者发生碰撞，使多个对象都有可能接受请求，进行相应的处理。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/18、职责链模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/18、职责链模式.md)

* 19、命令模式
介绍：将一个请求封装为一个对象，从而使我们可用不同的请求对客户进行参数化；对请求排队或者记录请求日志，以及支持可撤销的操作。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/19、命令模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/19、命令模式.md)

* 20、访问者模式
介绍：封装一些施加于某种数据结构元素之上的操作，一旦操作被修改，可以保持结构不变，使我们可以在不改变各元素的类的前提下定义作用于这些元素的新操作。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/20、访问者模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/20、访问者模式.md)

* 21、中介者模式
介绍：提供了一种简化复杂交互的解决方案，引入一个中介者，将原本对象之间的两两交互转化为每个对象与中介者之间的交互，降低了原有系统的耦合度，系统更加灵活。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/21、中介者模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/21、中介者模式.md)

* 22、备忘录模式
介绍：提供了一种对象状态的撤销机制，相当于“后悔药”，使系统恢复到原有历史状态。如果系统需要提供回滚操作时，使用备忘录模式非常合适。例如文本编辑器的撤销操作的实现，数据库中事务操作。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/22、备忘录模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/22、备忘录模式.md)

* 23、迭代器模式
介绍：举个例子，如果将电视机看成一个视频频道的集合，那么迭代器就相当于是电视机遥控器。我们可以通过遥控器对电视频道进行操作。迭代器模式提供了一种方法来访问聚合对象，但是不用暴露对象的内部表示。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/23、迭代器模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/23、迭代器模式.md)

* 24、解释器模式
介绍：定义语言的文法，并且建立一个解释器来解释该语言中的句子，这个“语言”的含义就是使用规定格式和语法的代码。
示例：[https://github.com/yzsunlei/javascript-design-mode/blob/master/24、解释器模式.md](https://github.com/yzsunlei/javascript-design-mode/blob/master/24、解释器模式.md)

### 技巧型设计模式：
* 25、链模式
* 26、委托模式
* 27、数据访问对象模式
* 28、节流模式
* 29、简单模板模式
* 30、惰性模式
* 31、参与者模式
* 32、等待者模式

### 架构型设计模式：
* 33、同步模块模式
* 34、异步模块模式
* 35、Widget模式
* 36、MVC模式
* 37、MVP模式
* 38、MVVM模式

* 备注：该分类借鉴于《JavaScript设计模式-张容铭》

## 参考
* [https://book.douban.com/subject/26589719/](https://book.douban.com/subject/26589719/)
* [https://book.douban.com/subject/26382780/](https://book.douban.com/subject/26382780/)
* [https://www.w3cschool.cn/zobyhd/m1w6jozt.html](https://www.w3cschool.cn/zobyhd/m1w6jozt.html)
* [https://www.cnblogs.com/xiyangbaixue/p/3902699.html](https://www.cnblogs.com/xiyangbaixue/p/3902699.html)

