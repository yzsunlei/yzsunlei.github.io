---
layout: post
title: 一站式页面调试、抓包工具spy-debugger推荐
category: 编程
tag: node
exception: 一站式页面调试、抓包工具。远程调试任何手机浏览器页面，任何手机移动端webview（如：微信，HybirdApp等）。支持HTTP/HTTPS，无需USB连接设备。
readtime: 5
---

# 特性
* 1、页面调试＋抓包
* 2、操作简单，无需USB连接设备
* 3、支持HTTPS。
* 4、spy-debugger内部集成了weinre、node-mitmproxy、AnyProxy
* 5、自动忽略原生App发起的https请求，只拦截webview发起的https请求。对使用了SSL pinning技术的原生App不造成任何影响
* 6、可以配合其它代理工具一起使用(默认使用AnyProxy) (设置外部代理)

# 安装使用
* 1、安装
```html
// Windows 下
npm install spy-debugger -g
// Mac 下
sudo npm install spy-debugger -g
```
* 2、命令行输入`spy-debugger`，浏览器自动打开地址或按命令行提示用浏览器打开地址
* 3、打开wifi，连接到电脑同一个网络下的wifi，并将命令行中提示内容设置到HTTP代理上
```html
Android设置代理步骤：设置 - WLAN - 长按选中网络 - 修改网络 - 高级 - 代理设置 - 手动
iOS设置代理步骤：设置 - 无线局域网 - 选中网络 - HTTP代理手动
```
* 4、手机安装证书(手机首次调试需要安装证书，已安装了证书的手机无需重复安装)
* 5、用手机浏览器或微信浏览器访问你要调试的页面

# 高级设置
* 自定义端口(默认9888)
```html
spy-debugger -p 8888
```
* 设置外部代理（默认使用AnyProxy）
```html
spy-debugger -e http://127.0.0.1:8888
注：spy-debugger内置AnyProxy提供抓包功能，但是也可通过设置外部代理和其它抓包代理工具一起使用，如：Charles、Fiddler
```
* 设置页面内容为可编辑模式(默认是false)
```html
spy-debugger -w true
注：内部实现原理：在需要调试的页面内注入代码：document.body.contentEditable=true。暂不支持使用了iscroll框架的页面。
```
* 是否允许weinre监控iframe加载的页面（默认是false）
```html
spy-debugger -i true
```
* 是否只拦截浏览器发起的https请求（默认是true）
```html
spy-debugger -b false
```
* 是否允许HTTP缓存(默认是false)
```html
spy-debugger -c true
```

# 使用示例
* 启动
![启动](https://yzsunlei.b0.upaiyun.com/2018/20170726195806.png)
* 手机上操作
![手机上操作](https://yzsunlei.b0.upaiyun.com/2018/20170726200442.jpg)
* 页面调试
![页面调试](https://yzsunlei.b0.upaiyun.com/2018/20170726200340.png)
* 请求抓包
![请求抓包](https://yzsunlei.b0.upaiyun.com/2018/20170726200335.png)

# 参考资料
* [spy-debugger](https://www.npmjs.com/package/spy-debugger)
