---
layout: post
title: 《python核心编程（第二版）》阅读记录
category: 阅读
tag: python
exception: 从基础到深入，逐步让你理解python语言的优美编程，python开发从业者不可缺少的一本桌边书...
readtime: 15
---

# 1、python起步
* Python的主提示符(`>>>`): 解释器告诉你她在等待你输入下一个语句
* Python的次提示符(`...`): 解释器正在等待你输入当前语句的其他部分
* 下划线(`_`)在解释器中表示最后一个表达式的值
* 符号(`>>`)用来重定向输出
* 从用户那里得到数据输入的最容易的方式是使用`raw_input()`内建函数
* 从交互式解释器中获得帮助使用`help()`,然后将函数名作为参数
* Python不支持C语言中的自增1和自减1
* Python的长整数所能表达的范围与大小超过C语言的长整数, 类似于Java的BigInteger
* Python支持使用成对的单引号或双引号以及三引号(三个连续的单引号或者双引号)
* 使用索引运算符`[]`和切片运算符`[:]`可以得到子字符串
* 加号`(+)`用于字符串连接运算, 星号`*`用于字符串重复，两个星号表示幂运算
* print语句默认会给每一行添加一个换行符, 只要在print语句的最后添加一个逗号(`,`), 输出的元素之间会自动添加一个空格
* 列表解析, 你可以在一行中使用一个for循环将所有值放到一个列表中
* `sqdEvens = [x ** 2 for x in range(8) if not x % 2]`
* `self`是类实例自身的引用
* 标准输出`write()`不会自动在字符串后面添加换行符号

# 3、python基础
* 井号`#`表示之后的字符为 Python 注释
* 换行`\n` 是标准的行分隔符（通常一个语句一行）
* 反斜线`\` 继续上一行
* 分号`;`将两个语句连接在一行中
* 冒号`:`将代码块的头和体分开
* 语句（代码块）用缩进块的方式体现
* 不同的缩进深度分隔不同的代码块
* Python 文件以模块的形式组织
* 支持多元赋值: `x, y, z = 1, 2, 'a string'`
* Python 的多元赋值方式可以实现无需中间变量交换两个变量的值: `x, y = y, x`
* `_xxx` 不用`from module import *`导入
* `__xxx__`系统定义名字
* `__xxx` 类中的私有变量名
* 如果模块是被导入，`__name__`的值为模块名字
* 如果模块是被直接执行，`__name__`的值为`__main__`
* 使用`del`语句删除一个变量，但没法删除一个常量值(会自动垃圾回收)
* Python的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器
* 调试模块pdb允许你设置（条件）断点，代码逐行执行，检查堆栈。它还支持事后调试

# 4、python对象
* 所有的Python对象都拥有三个特性：身份，类型和值
* 其他内建类型：类型、Null 对象 (`None`)、文件、集合/固定集合、函数/方法、模块、类
* `type(type(42)) #<type 'type'>`  所有类型对象的类型都是`type`，它也是所有Python 类型的根和所有Python标准类的默认元类（`metaclass`）
* 特殊类型: `Null`对象或`NoneType`，只有一个值， 那就是`None`
* 和`None` 类型最接近的C 类型就是`void`，`None` 类型的值和C 的`NULL` 值非常相似
* 空列表: `[]`、空元组`()`、空字典`{}`
* `foostr = 'abcde'; foostr[::-1] #'edcba'` 相当于反转
* 省略对象有一个唯一的名字 `Ellipsis`, 它的布尔值始终为 `True`.
* `3 < 4 < 7` #多个比较操作可以在同一行上进行，求值顺序为从左到右
* Python 提供了`is` 和`is not`运算符来测试两个变量是否指向同一个对象
* 整数对象和字符串对象是不可变对象，所以Python 会很高效的缓存它们 `#a = 1; id(a) #8402824;b = 1; id(b) #8402824`
* `repr(obj)` 或 `obj` 返回一个对象的字符串表示
* `str()` 和 `repr()` 或反引号运算符`(``)` 可以方便的以字符串的方式获取对象的内容、类型、数值属性等信息
* 通常情况下 `obj == eval(repr(obj))` 这个等式是成立的
* Python 2.2 统一了类型和类， 所有的内建类型现在也都是类
* 原来的所谓内建转换函数象`int(), type(), list()` 等等， 现在都成了工厂函数
* 存储模型：标量/原子类型 数值（所有的数值类型），字符串（全部是文字）; 容器类型 列表、元组、字典
* 更新模型: 可变类型 列表， 字典; 不可变类型 数字、字符串、元组
* 访问模型: 直接访问: 数字; 顺序访问: 字符串、列表、元组; 映射访问: 字典
* 其实在Python 中， 一切都是指针
* 事实上Python 的整数实现等同于C 语言的长整数
* Python 的浮点类型实际上是C 语言的双精度浮点类型

# 5、数字类型

# 7、序列：字符串、列表和元组
* 成员关系操作符 (in, not in)使用来判断一个元素是否属于一个序列
* seq * expr 序列重复expr 次
* 正负索引的区别在于正索引以序列的开始为起点(从0开始)，负索引以序列的结束为起点(从-1开始)
* 可以先创建一个只包含None 的列表,然后用extend()函数把range()的输出添加到这个列表 
* [None].extend(range(-1, -len(s), -1))
* [None].extend(...)函数返回None , None 既不是序列类型也不是可迭代对象
* 在Python里面没有字符这个类型.这可能是双引号和单引号在Python 里面被视作一样的的另一个原因
* 成员操作符用于判断一个字符或者一个子串(中的字符)是否出现在另一个字符串中
* 注意，成员操作符不是用来判断一个字符串是否包含另一个字符串的，这样的功能由find()或者index()
* s = ' '.join(('Spanish', 'Inquisition', 'Made Easy'))

# 8、条件和循环
* 根本上说, 迭代器就是有一个 next() 方法的对象, 而不是通过索引来计数
* 对一个对象调用 iter() 就可以得到它的迭代器
* map(lambda x: x ** 2, range(6)) ======= [x ** 2 for x in range(6)]

# 11、函数式编程
* 函数：有返回值; 过程: 简单、特殊、没有返回值的函数

# 12、模块
* sys.path.append('/home/wesc/py/lib') #添加模块搜索路径
* __builtins__ 模块和 __builtin__ 模块不能混淆：
* __builtins__ 模块包含内建名称空间中内建名字的集合；在标准 Python 执行环境下, __builtins__ 包含 __builtin__ 的所有名字
* 限制使用 "from module import *"
* __import__(module_name[, globals[, locals[, fromlist]]]) #提供这个函数是为了让有特殊需要的用户覆盖它, 实现自定义的导入算法
* reload() 内建函数可以重新导入一个已经导入的模块
* 从 2.5 版 开始, 相对导入被加入到了 Python 中 #from ..common_util import setup
* 如果你不想让某个模块属性被 "from module import *" 导入 , 那么你可以给你不想导入的属性名称加上一个下划线( _ )
* 很多方法可以执行一个 Python 模块: 通过命令行或 shell , execfile() , 模块导入, 解释器的 -m 选项

# 13、面向对象编程
* 实例名字mathObj 将mathObj.x和mathObj.y 关联起来。这就是我们所说的使用类作为名字空间容器
* 如果子类重写基类的构造器，基类的构造器就不会被自动调用了－－这样，基类的构造器就必须显式写出才会被执行
* 请注意Python 并不支持纯虚函数（像C++）或者抽象方法（如在JAVA 中），这些都强制程序员在子类中定义方法


# 14、执行环境


# 15、正则表达式
* 有两种主要方法完成模式匹配：搜索(searching)和匹配(matching)
* 管道符号( | ), 表示一个或操作，它的意思是选择被管道符号分隔的多个不同的正则表达式中的一个 #at|home匹配的字符串at,home
* 点字符或句号(.)符号匹配除换行符(NEWLINE)外的任意一个单个字符(Python 的正则表达式有一个编译标识[S or DOTALL], 该标识能去掉这一限制
* \b 匹配的模式是一个单词边界, 对应的模式一定在一个单词的开头 #\bthe 任何以"the"开头的字符串
* \B 只匹配出现在一个单词中间的模式(即, 不在单词边界上的字符) #\Bthe 任何包含"the"单不以"the"开头的单词
* 当前Python 的默认正则表达式模块 re 模块, regex 和regsub 这两个模块已在Python 2.5 版本时被移除了
* 常用的正则表达式函数与方法: compile、match、search、findall、finditer、split、sub、group、groups



# 16、网络编程
* 使用套接字进行网络编程？
* 套接字是一种具有之前所说的“通讯端点”概念的计算机网络数据结构;
* socket(socket_family, socket_type, protocol=0);
* 在运行网络应用程序时，最好在不同的电脑上执行服务器和客户端的程序;
* accept()函数是阻塞式的，即程序在连接到来之前会处于挂起状态;
* Twisted 框架(官网链接(https://twistedmatrix.com/trac/)): 完全事件驱动的网络框架;
* select 模块通常在底层套接字程序中与socket 模块联合使用;

# 17、网络客户端编程
* 虽然现在我们不再使用底级别的套接字来创建因特网客户端，但模型是完全相同的;
* 最流行的有文件传输协议(FTP)，Unix-to-Unix 复制协议(UUCP)，以及网页的超文本传输协议(HTTP)，（Unix 下的）远程文件复制指令rcp（以及更安全，更灵活的scp 和rsync）。
* RFC（中文目录：http://man.chinaunix.net/develop/rfc/default.htm）？是一系列以编号排定的文件，基本的因特网通讯协定都有在RFC文件内详细说明；
* 使用Python的FTP支持，需要导入ftplib模块，并实例化ftplib.FTP类对象
* 在一般的FTP 通讯中，要使用到的指令有login(), cwd(), dir(), pwd(), stor*(), retr*()和quit()
* Usenet？新闻组，全球性的文件交换网络，可以用来发言评论，可以用来传递文件
* 有一个库nntplib 和一个类nntplib.NNTP，要实例化这个类用于NNTP
* 一些方法：group返回元组(rsp, ct, fst, last, group)，服务器的返回信息，文章数量，第一个和左后一个文章的号码和组名
* 仔细看看你收到的e-mail 的邮件头，会看到一个“passport”标记，其中记录了邮件寄给你这一路上都到过了哪些地方；
* MTA？MTA 之间通讯所使用的协议叫消息传输系统（MTS）；
* SMTP 由已故的Jonathan Postel（加利福尼亚大学信息学院）创建，记录在RFC 821中；
* Pyhthon中使用smtp也存在一个smtplib 模块和一个smtplib.SMTP 类要实例化；
* sendmail()的所有参数都要遵循RFC 2822；
* 用于下载邮件的第一个协议叫邮局协议，记录在RFC 918 中；

# 18、多线程编程
* 守护线程?
* Python 提供了几个用于多线程编程的模块，包括thread, threading 和Queue
* 核心提示：避免使用thread 模块,序应该尽可能地使用threading 等高级别的线程模块
* 锁原语?
* 另一个避免使用thread 模块的原因是，它不支持守护线程


# 19、图形用户界面编程
* Python 的默认GUI 工具集是Tk;
* Tkinter 是Python 的默认GUI 库，它基于Tk 工具集，后者最初是为工具命令语言（Tcl）设计
 的;
* 基础: 顶层窗口对象;
* Tkinter.Tk()返回的对象通常被称作根窗口;
* Tkinter.mainloop() #这通常是您程序执行的最后一段代
* 4 种比较流行且可用的工具集来编写同一个GUI 程序示例：Tix（Tk Interface eXtensions)、Pmw（Python MegaWidgets
 的Tkinter 扩展）、wxPython（wxWidgets 的Python 绑定）、和PyGTK（GTK+的Python 绑定）


# 20、web编程



# 21、数据库编程



# 22、扩展Python
* 编写扩展代码并将它们的功能整合到Python编程环境中来；
* Python 的一大特点就是，扩展和解释器之间的交互方式与普通的Python模块完全一样；
* 扩展Python的几点理由：添加额外的非pyhton功能；性能瓶颈的效率提升；保持专有源代码私密；
* 代码保密的一种方法是只发布预编译后的.pyc文件；
* 在从Python到C的转换就用PyArg_Parse*系列函数；



# 23、更多
* 客户端的COM编程?
* win32com 中的excel、word、powerpoint、email、outlook使用

QS: Python中*args 和**kwargs的用法
