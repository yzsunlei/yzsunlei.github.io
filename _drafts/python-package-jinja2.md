# Jinja2模板引擎

# JInja2简明教程
# 1、特征
# 沙箱中执行
# 强大的 HTML 自动转义系统保护系统免受 XSS
# 模板继承
# 及时编译最优的 python 代码
# 可选提前编译模板的时间
# 易于调试。异常的行数直接指向模板中的对应行。
# 可配置的语法
#
# 2、基本API使用:
# from jinja2 import Template #引入模块
# template = Template('Hello {{ name }}!') #创建一个新的模板对象
# template.render(name = 'John Doe') #调用变量渲染模板
#
# 3、Jinja2的API
# *使用基础
# from jinja2 import Environment, PackageLoader #使用一个名为Environment的中心对象，用于存储配置、全局对象和加载模板
# env = Environment(loader=PackageLoader('yourapplication', 'templates')) #创建一个默认设定下的模板环境和yourapplication python包中的templates文件夹中寻找模板的加载器
# template = env.get_template('mytemplate.html') #从这个环境中加载模板并返回已加载的Template
# print template.render(the='variables', go='here') #用变量来渲染
# *内部使用Unicode
# 需要向渲染函数传递Unicode对象或只包含ASCII字符的字符串
# 显式使用Unicode字符串，需要给字符串字面量加上u前缀：u'Hänsel und Gretel sagen Hallo'
# 妥善设置模块编码：# -*- coding: utf-8 -*-
# inja2 对只有 ASCII 的字符串返回 str，而对其它返回 unicode
# *自动转义
# 推荐为以.html、.htm、.xml以及.xhtml的模板开启自动转义，并对其他扩展名禁用
#
# 4、扩展:
# *添加扩展
# 支持扩展来添加过滤器、测试、全局变量甚至是处理器
# 扩展在环境被创建时添加，一旦环境创建，就不能添加额外的扩展
# 添加扩展：传递一个扩展类或导入路径的列表
# jinja_env = Environment(extensions=['jinja2.ext.i18n']) #创建一个加载i18n扩展的jinja2环境


# Jinja2模板文档:
# 1、概述
# 模板就是个普通文本文件，可以设计为任何文本格式(HTML、XML、CSV等, 也可以不需要扩展名)
# jinja2的语法主要参考自Django和Python
# 
# 2、变量
# {{foo.bar}} #对象方式
# {{foo['bar']}} #字典方式
# {{...}}用来打印变量，要在其他标签中访问变量，则不能在变量名旁边加花括号
# 
# 3、过滤器(filters)
# {{name|striptags|title}} #类似管道操作
# {{list|join(',')}} #也可用来调用参数
# 
# 4、检查器(tests)
# 用来在jinja2的if块中检查一个变量是否符合某种条件，用法是varname is tests
# {% if name is defined%} #检查一个变量是否存在
# {% if loop.index is divisibleby 3 %} #也可以带参数，只有一个参数时可不写括号
# 
# 5、注释
# {#
#   {% for user in users %} 
#     ... 
#   {% endfor %} 
# #} 
# 以上注释内容就不会出现在模板产生的文本
# 
# 6、模板继承
# 一般工程都是创建一个包含所有公共元素的页面基本骨架，在子模板中可以重用这些公用的元素
# *先写一个base.html基础模板
# <html lang="en"> 
# <head> 
#     {% block head %} 
#     <link rel="stylesheet" href="style.css" /> 
#     <title>{% block title %}{% endblock %} - My Webpage</title> 
#     {% endblock %} 
# </head> 
# <body> 
#     <div id="content">{% block content %}{% endblock %}</div> 
#     <div id="footer"> 
#         {% block footer %} 
#         &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>. 
#         {% endblock %} 
#     </div> 
# </body>
# </html>
# *再写子模板child.html将基础模板中的block替换掉
# {% extends "base.html" %} #继承基础模板
# {% block title %}Index{% endblock %} 
# {% block head %} 
#     {{ super() }} 
#     <style type="text/css"> 
#         .important { color: #336699; } 
#     </style> 
# {% endblock %} 
# {% block content %} 
#     <h1>Index</h1> 
#     <p class="important"> 
#       Welcome on my awsome homepage. 
#     </p> 
# {% endblock %}
# *也可以在子模板中覆写基础模板
# {% block sidebar %} 
#     <h3>Table Of Contents</h3> 
#     ... 
#     {{ super() }} 
# {% endblock %} 
# *最后要注意的几点：
# 同一个模板中不能定义名称相同的block
# 不支持多继承
# 
# 7、HTML转义
# 传递给模板的变量中可能会有一些html标识符，会影响页面正常显示，也可能带来跨站脚本攻击的隐患
# 通过给Environment或Template的构建器传递autoescape参数，可以设置自动转义与否
# 手动转义：{{user.username|e}} #e是使用过滤器转换我们需要的变量
# 自动转义：{{user.username|safe}} #打印变量时自动进行转义
# 
# 8、结构控制标记
# *常用的(for-loop)循环控制
# {% for user in users %}
#   <li>{{ user.username|e }}</li>
# {% endfor %}
# 循环不支持break和continue，可以对需要迭代的sequence使用过滤器达到同样的效果
# {% for user in users if not user.hidden %} #如果user.hidden属性为true的则continue
#     <li>{{ user.username|e }}</li> 
# {% endfor %} 
# for语句还有else，当无循环时显示else中的内容
# {% for user in users %} 
#     <li>{{ user.username|e }}</li> 
# {% else %} 
#     <li><em>no users found</em></li> #for循环无内容时显示
# {% endif %} 
# *完整的if-elif-else-endif条件语句
# {% if kenny.sick %} 
#     Kenny is sick. 
# {% elif kenny.dead %} 
#     You killed Kenny!  You bastard!!! 
# {% else %} 
#     Kenny looks okay --- so far 
# {% endif %} 
# *使用宏(Macro)
# {% macro input(name, value='', type='text', size=20) -%} #定义一个简单的宏
#     <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}"> 
# {%- endmacro %}
# {{ input('username') }} #调用宏
# 宏其实也是个对象
# *使用内部赋值
# {% navigation = [('index.html', 'Index'), ('about.html', 'About')] %} 
# *使用include
# 导入一个模板到当前模板
# {% include 'header.html' %} 
# Body 
# {% include 'footer.html' %} 
# *宏定义 #写一个forms.html的模板
# {% macro input(name, value='', type='text') -%} #定义一个宏input
#     <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}"> 
# {%- endmacro %}
# {%- macro textarea(name, value='', rows=10, cols=40) -%} #定义一个宏textarea
#     <textarea name="{{ name }}" rows="{{ rows }}" cols="{{ cols }}">{{ value|e }}</textarea> 
# {%- endmacro %}
# *宏定义导入
# {% import 'forms.html' as forms %} #先使用import导入
# {{ forms.input('username') }} #引用input
# {{ forms.textarea('comment') }} #引用textarea
# {% from 'forms.html' import input as input_field, textarea %} #导入指定的内容（宏或者变量）
# {{ input_field('username') }} #引用input
# {{ textarea('comment') }} #引用textarea

# 9、表达式
# 表达式在模板中常见，语法类似python
# *字面值类型：字符串、数字、序列、元组、字典、布尔
# *数字计算：+,-,/,//(整除），%求余，*乘，**次方
# *逻辑计算：and, or, not, () 
# *其他操作符：
# in 判断一个对象是否存在于另一个序列或者元组中  #{{ 1 in [1, 2, 3] }}  
# is 执行一个检查器 
# | 执行一个过滤器 
# ~ 连接字符串 {{ "Hello " ~ name ~ "!" }}，如果name的值是world， 显示的内容将是 "Hello world"
# ( ) 调用函数 
# . / [] 访问一个对象的属性 
# *if内联表达式
# {% extends layout_template if layout_template is defined else 'master.html' %} 
# 如果变量layout_template已定义则导入，否则导入master.html
#
# 10、内置过滤器
# abs(number) #返回数字的绝对值
# batch(value, linecount, fill_with=None) #将一个序列以给定值分成若干片。如果给定fill_with，则会将fill_with补充到未分配的部分
# capitalize(s) #首字符大写
# center(value, width=80) #生成一个长度为width的空字符串，并将value放在中间
# default(value, default_value=u”, boolean=False) #value未定义时，显示default_value。如果value是一个bool型，需要将boolean置为true
# dictsort(value, case_sensitive=False, by='key') #字典排序，case_sensitive决定是否大小写敏感，by决定是按照key排序还是按value排序
# escape(s) #html字符转义，别名是e
# filesizeformat(value) #将一个大数字转换成KMG形式，如1.3k，34g
# first(seq) #返回序列的第一个值 
# float(value, default=0.0) #将一个值转换成浮点数，如果转换失败则返回default 
# forceescape(value) #不管value是否被转义过，一律进行html转义
# format(value, *args, **kwargs) #等同于python的"%s,%s" % (str1, str2)
# groupby(value, attribute) #类似SQL的group by,可以将一个序列里的对象/字典，按照attribute分组
# indent(s, width=4, indentfirst=False) #将文本s中每行的首字符缩进width个字符
# int(value, default=0) #将value转换成整数，如果转换失败则返回default 
# join(seq, d=u”) #将序列seq中的各个值用d字符连接起来形成一个字符串
# last(seq) #序列的最后一个值
# length(object) #序列或字典的长度
# list(value) #将value转成为序列，如果value为字符串，则将字符串转换成为字符数组
# lower(s) #将字符串转换成小写
# pprint(value, verbose=False) #debug时使用，可以打印变量的详细信息
# random(seq) #随机从序列中取得一个值
# replace(s, old, new, count=None) #将字符s中的old字符串替换为new字符串，如果给定了count，则最多替换count次
# reverse(value) #将一个序列反转
# round(value, precision=0, method='common') #浮点数求精。precision=0, method有(common四舍五入，ceil向上取整，floor向下取整)
# safe(value) #如果当前模板设置html自动转义，用此过滤器可以使value不转义
# slice(value, slices, fill_with=None) #将序列分片，用fill_with字符填充最后一组子序列长度不足的部分
# sort(value, reverse=False) #将序列按从小到大排序，reverse为true则按从大到小排序
# string(object) #将一个对象转换为unicode字符串 
# striptags(value) #去掉字符串value中的html，xml标签 
# sum(sequence, start=0) #统计数值序列的和。start表示从第几项开始计算 
# title(s) #将字符串s中每个单词首字符大写 
# trim(value) #去掉字符串value中首尾的空格 
# truncate(s, length=255, killwords=False, end='...') #截断一个字符串为length长度，末尾补end字符，killwords选择如何处理最后一个单词
# upper(s) #将字符串转换成大写
# urlize(value, trim_url_limit=None, nofollow=False) #将链接文本转换成可点击的真实链接
# wordcount(s) #统计字符串中单词的个数 
# wordwrap(s, pos=79, hard=False) #将字符串s按照pos长度换行。如果hard为True，则强制截断单词
# xmlattr(d, autospace=True) #创建一个sgml/xml的属性字符串
# autospace #自动在首部添加空格
# 
# 11、内建检查器
# callable(object) #对象是否可调用
# defined(value) #对象是否已定义
# divisibleby(value, num) #value是否可以被num整除
# escaped(value) #是否已转义
# even(value) #是否为奇数
# iterable(value) #是否可以循环
# lower(value) #是否为小写
# none(value) #是否为None
# number(value) #是否为数字
# odd(value) #是否为偶数
# sameas(value, other) #value是否与other为同一个对象实例
# sequence(value) #是否为序列
# string(value) #是否是字符串
# undefined(value) #是否未定义
# upper(value) #是否为大写