---
layout: post
title: XlsxWriter简明使用教程
category: 编程
tag: python excel
exception: XlsxWriter是一个用来写Excel2007和xlsx文件格式的python模块。它可以用来写文本、数字、公式并支持单元格格式化、图片、图表、文档配置、自动过滤等特性
readtime: 15
---

## 简介
* XlsxWriter是一个用来写Excel2007和xlsx文件格式的python模块。它可以用来写文本、数字、公式并支持单元格格式化、图片、图表、文档配置、自动过滤等特性
* 优点：功能更多、文档高保真、扩展格式类型、更快并可配置
  缺点：不能用来读取和修改excel文件

## 基本使用
* 安装
```$xslt
pip install XlsxWriter
```
* 引用
```$xslt
import xlsxwriter
```
* 创建Excel表
```$xslt
workbook = xlsxwriter.Workbook('example.xlsx')
worksheet = workbook.add_worksheet('info')
```
* 预设格式
```$xslt
bold = workbook.add_format({'bold': True})
```
* 设定列宽(两种方式)
```$xslt
worksheet.set_column(1, 1, 15)
worksheet.set_column('B:B', 15)
```
* 获取数据
```$xslt
data = (['Rent', 1000], ['Gas', 100], ['Food', 300])
```
* 写入数据(并使用格式)
```$xslt
row = 0
col = 0

for item, cost in (data):
  worksheet.write(row, col, item, bold)
  worksheet.write(row, col + 1, cost)
  row += 1
```
* 写入公式
```$xslt
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')
```
* 关闭
```$xslt
worksheet.close()
```  

## 核心类
* Workbook class：打开/关闭excel，新建Worksheet等
* Worksheet class：数据写入，格式设置等
* Worksheet class(Page Setup)：打印设置等
* Format class：单元格格式化
* Chart class：图表处理
* Chartsheet Class：单页面图表处理

## 参考阅读
* [官方文档：http://xlsxwriter.readthedocs.io](http://xlsxwriter.readthedocs.io)
