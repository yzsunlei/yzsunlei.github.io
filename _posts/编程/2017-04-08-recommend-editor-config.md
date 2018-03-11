---
layout: post
title: 推荐一下EditorConfig
category: 编程
tag: 工具
exception: 推荐一下EditorConfig，当你在自己的笔记本上配置你在公司电脑上已经配置过的项目时，当公司来的新人提交的代码风格和项目原有代码风格不一致时，也许你会想起editorconfig...
readtime: 5
---

## 什么是EditorConfig?
* EditorConfig是一套用于统一代码工具的解决方案，很多项目都有用到
* EditorConfig可以帮助开发者在不同的编辑器和IDE之间定义和维护一致的代码风格。EditorConfig包含一个用于定义代码格式的文件和一批编辑器插件，这些插件可以让编辑器读取配置文件并依此格式化代码
* EditorConfig的配置文件十分易读，并且可以很好的在VCS(版本控制系统)下工作

## EditorConfig的配置文件是什么样的？
* 下面是一个用于设置Python和JavaScript行尾和缩进风格的配置文件
```
# EditorConfig is awesome: http://EditorConfig.org
# top-most EditorConfig file
root = true
# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true
# Matches multiple files with brace expansion notation
# Set default charset
[*.{js,py}]
charset = utf-8
# 4 space indentation
[*.py]
indent_style = space
indent_size = 4
# Tab indentation (no size specified)
[*.js]
indent_style = tab
# Indentation override for all JS under lib directory
[lib/**.js]
indent_style = space
indent_size = 2
# Matches the exact files either package.json or .travis.yml
[{package.json,.travis.yml}]
indent_style = space
indent_size = 2
```

## 怎样使用EditorConfig呢？
* 一般将EditorConfig配置文件放在项目的根目录
* Windows用户要创建该文件时，可以先创建.editorconfig.文件，系统会自动重名为.editorconfig
* 支持的属性
```
indent_style：tab为hard-tabs，space为soft-tabs。
indent_size：设置整数表示规定每级缩进的列数和soft-tabs的宽度（译注：空格数）。如果设定为tab，则会使用tab_width的值（如果已指定）。
tab_width：设置整数用于指定替代tab的列数。默认值就是indent_size的值，一般无需指定。
end_of_line：定义换行符，支持lf、cr和crlf。
charset：编码格式，支持latin1、utf-8、utf-8-bom、utf-16be和utf-16le，不建议使用uft-8-bom。
trim_trailing_whitespace：设为true表示会除去换行行首的任意空白字符，false反之。
insert_final_newline：设为true表明使文件以一个空白行结尾，false反之。
root：表明是最顶层的配置文件，发现设为true时，才会停止查找.editorconfig文件。
```

## 参考资料
* [EditorConfig介绍](http://blog.csdn.net/cengjingcanghai123/article/details/43953307)
* [EditorConfig官网](http://editorconfig.org/)