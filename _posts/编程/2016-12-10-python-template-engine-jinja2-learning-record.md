---
layout: post
title: Python模板引擎jinja2学习笔记
category: 编程
tag: Python, Jinja2
exception: jinja2模版引擎学习记录，方便以后回来查阅
readtime: 16
---

## 特性：
* 沙箱中执行
* 强大的`HTML`自动转义系统保护系统免受`XSS`
* 模板继承
* 及时编译最优的`python`代码
* 可选提前编译模板的时间
* 易于调试，异常的行数直接指向模板中的对应行
* 可配置的语法

## API：
* `Jinja2`使用一个名为`Environment`的中心对象，用这个类的实例存储配置、全局对象和从文件系统或其他位置加载模板
* 配置`Jinja2`为你的应用加载文档
  `from jinja2 import Environment, PackageLoader`
  `env = Environment(loader=PackageLoader('yourapplication', 'templates'))`
* 从环境中加载模板
  `template = env.get_template('mytemplate.html')`
* 用若干变量来渲染它
  `print template.render(the='variables', go='here')`
* Jinjia2内部使用`Unicode`，需要向渲染函数传递`Unicode`对象或只包含`ASCII`字符的字符串，用`Jinja2`来处理非`Unicode`数据是不可能的
* `class jinja2.Environment`：jinjia2的核心组件，包含重要的变量如配置、过滤器、测试、全局变量等等
  `class jinja2.Template`：核心模板对象，此类表示已编译的模板
  `class jinja2.environment.TemplateStream`：像普通的python生成器一样的模板流，但它可以缓冲多个item以减少多个迭代
  `class jinji2.runtime.Context`：模板上下文拥有模板变量，它存储了传递给模板的值和模板导出的名称
  `class jinja2.BaseLoader`：加载器负责从文件系统的资源加载模板，环境会吧编译的模块像python的模块一样保持在内存中(缓存默认有大小限制，且模板会自动重载)
* 自定义过滤器：只是常规的python函数，过滤器左边作为第一个参数，其余的参数作为额外的参数或关键字参数传递到过滤器，模板中使用`{{ 42|myfilter(23) }}`
  添加`filters`时需要更新环境上的`filter`字典来把它注册到模板环境上，示例`environment.filters['datetimeformate'] = datetimeformate`
* 自定义测试：测试不能访问环境或上下文，并且不能链式使用。测试的用途是让模板设计者运行类型和一致性检查，模板中使用```{% if 42 is prime %}```
  添加`tests`时需要更新环境上的`tests`字典来把它注册到模板环境上，示例`environment.tests['prime'] = is_prime`
* 底层API：低层API暴露的功能对理解一些实现细节、调试目的或高级扩展技巧是有用的（一般不推荐使用这些api）
* 元API：返回一些关于抽象语法树的信息，这些信息能帮助应用实现更多的高级模板概念。所有的元api函数操作一个`Environment.parse()`方法返回抽象语法树
    
## 沙箱
* jinjia2沙箱用于为不信任的代码求值，访问不安全的属性和方法是被禁止的
* `class jinja2.sandbox.SandboxedEnvironment`：沙箱环境，它工作就像有规则的环境会告诉编译器生成沙箱化的代码，另外这个环境的子类会覆盖一些方法来告诉运行环境什么函数是可以安全执行的

## 模板文档
* 分隔符：`{%...%}` 和`{{...}}`
* 变量传递：`{{foo.bar}}`和`{{foo['bar']}}`
* 过滤器：`{{name|striptags|title}}`(链式调用，前一个过滤器的输出作为后一个过滤器的输入)
* 测试：`{% if loop.index is divisibleby 3 %}`(要测试一个变量或表达式，要在变量后加上一个is以及测试的名称)
* 注释：`{#...#}`
* 空白控制：模板引擎默认不会对空白做进一步修改，空白(空格、制表符、换行符)都会原封不动返回；在块的开始或结束放置一个减号(`-`)，可以移除块前或块后的空白
* 转义：使用变量表达式输出(`{{ '{{' }}`)；标记一个块为raw是有意义的(`{% raw %}`)
* 行语句：如果应用启用了行语句，就可以把一个行标记为一个语句
* 模板继承：允许构建一个包含你站点共同元素的基本模板"骨架"，并定义子模板覆盖
* 基本模板：一般都会定义一个`base.html`作为项目页面的骨架
* 子模板：使用`{% extend %}`标签继承基本模板，使用`{% block head %}`标签替换基本莫班上的块
* Super块：在子模板块中可以使用`{{super()}}`来渲染父级块的内容
* 嵌套块和作用域：嵌套块可以实现更复杂的布局，但默认的块不允许访问块外作用域的变量；
  从jinja2.2开始可以显式的指定在块中可用的变量(块声明中添加`scoped`修饰)
* 模板对象：`{% extends layout_template %}`（假设调用代码传递`layout_template`布局模板到环境）
* HTML转义：变量包含影响已生成HTML的字符，默认的配置未开启自动转义
* 控制结构：条件(`if/elif/else`)、for循环、宏、块，在默认语法中以`{%...%}`块的形式出现
* For循环：默认语法`{%for yser in users%}`，可以递归使用循环，只需要在循环定义中加上`recursive`修饰
* If判断：`Jinja`中的`if`语句可比python中的`if`语句，用`elif`和`else`来构建多个分支
* 宏：宏类似常规编程语言中的函数，用于把常用行为作为可重用的函数，使用`{% macro input(params) -%}...{%- endmacro %}`进行定义，使用`{{ input('user') }}`进行调用
* 调用：需要把一个宏传递到另一个宏，可以使用特殊的call块（还可以传递参数）
* 过滤器：允许在一块模板数据上应用常规的Jinja2过滤器，使用`{% filter upper %}...{% endfilter %}`
* 赋值：在代码块中可以使用set标签为变量赋值，示例`{% set navigation = [('index.html, 'Index')] %}`
* 块：用于继承，同时作为站位符合用于替换的内容
* 包含：用于包含一个模板，使用`{% incalue 'header.html' %}`，使用`ingore missing`标记模板不存在时忽略这条语句，使用`with`或`without context`联合使用时，必须放在上下文可见性语句之前
* 导入：支持在宏中放置经常使用的代码，使用`{% import 'forms.html' as forms %}`、`<div>{{ forms.input('username') }}</div>`
* 导入上下文行为：默认下，每个包含的模板会被传递到当前上下文，而导入的模块不会。但也可以通过直接添加`with context`或`without context`显式的进行更改
* 表达式：像常规的Python一样工作，到处都允许使用基本表达式
* 字面量：字符串、数值、列表、元组、字典、true/false（为了一致性，所有的`jinja2`标识符是小写的，特殊常量true、false、none实际上都是小写的）
* 算术：`+`（加法，也可作为字符串衔接，但连接字符串首选用`~`）、`-`、`/`、`//`（整数除）、`%`、`*`、`**`（取幂）
* 比较：`==`、`!=`、`>`、`>=`、`<`、`<=`
* 逻辑：`and`、`or`、`not`、`(expr)`
* 其他运算符：`in`、`is`、`|`、`~`、`()`、`.`、`[]`，`is`和`in`运算符同样支持使用中缀记法`foo is not bar`和`foo not in bar`
* if表达式：可以使用内联的if表达式`{% extend layout_template if layout_template is defined else 'master.html' %}`

## 扩展
* i18n：`<P>{% trans %}Hello {{ user }}{% endtrans %}</p>`，标记一个段为可译的
* 表达式语句：`{% do navigation.append('a string') %}`，工作几乎如同常规的变量表达式，不打印任何东西，可以用于修改列表
* 循环控制：在循环中添加`break`、`continue`支持
* with语句：可以创建一个新的作用域，该作用域中的变量在外部是不可以见的
* 自动转义扩展：可以在模板中开启或者关闭自动转义，`{% autoescape true %}...自动转义开启...{% autoescape %}`

## 集成
* Jinja2提供一些代码来继承到其他工具，如框架、Babel库或偏好id编辑器的奇特的代码高亮

## 提示和技巧
* Null-Master退回：支持动态继承并且只要`extends`标签没有被访问过，就不分辨父模板和子模板。首个extends标签前的包括空白字符的所有东西会被打印出来而不是被忽略
* 交替的行：对一个表格或列表的每行使用不同的样式，可以使用loop对象的cycle方法，`<li class="{ loop.cycle('odd', 'even') }">{{ row }}</li>`
* 高亮活动菜单项：在block外的声明在子模板中是全局的，并且在布局模板求值前执行，在子模板中定义活动的菜单项，`{% set active_page = "index" %}`
* 访问父级循环：特殊的loop变量总是指向最里层的循环，在里层访问外层的循环，可以给它设置别名，`{% set rowloop = loop %}`

## 参考资料
* [http://docs.jinkan.org/docs/jinja2/index.html](http://docs.jinkan.org/docs/jinja2/index.html)