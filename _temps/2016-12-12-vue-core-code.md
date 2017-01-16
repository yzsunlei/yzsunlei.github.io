# Vue核心代码分析
* Author: RaySun
* Date: 2016/12/12

# DOM编译过程解析(http://www.ituring.com.cn/article/273672)
* 转置(transclude函数)：主要用来把模板转换成DOM对象并返回
* 编译(compile函数)：根据DOM对象的属性匹配Vue的内置指令，匹配到就创建一个对象push到dirs数组，最后返回linkFn树形结构
* 链接

