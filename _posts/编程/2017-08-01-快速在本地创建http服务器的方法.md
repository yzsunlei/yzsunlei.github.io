---
layout: post
title: 快速在本地创建http服务器的方法
category: 编程
tag: http
exception: 可以通过浏览器直接打开HTML文件来查看可视化的效果，但有时需要在HTTP服务器上打开才能正常显示（文件相互链接的原因），下面几种方法可以快速的实现。
readtime: 5
---

# 用Python--适合大多数UNIX/Mac系统
```javascript
python -m SimpleHTTPServer
```
![使用python打开](https://yzsunlei.b0.upaiyun.com/2018/20170806202557.png)

# 用NPM--如果你安装了Node.js
```javascript
npm install -g http-server
http-server
```
![安装http-server后打开](https://yzsunlei.b0.upaiyun.com/2018/20170806202825.png)

# 用Mongoose--在Mac/Windows上可以移植
```javascript
Windows平台，将下载好的文件复制到一个目录，双击启动就可以在浏览器上显示该目录中的内容
其他平台，将下载好的文件复制到一个目录，通过命令行来启动就可以在浏览器上显示该目录中的内容
```
![用Mongoose双击打开](https://yzsunlei.b0.upaiyun.com/2018/20170806203813.png)
下载地址：[http://www.softpedia.com/dyn-postdownload.php/9a78fb1f806e2db40eac714569862ebf/59870ff8/24218/4/1](http://www.softpedia.com/dyn-postdownload.php/9a78fb1f806e2db40eac714569862ebf/59870ff8/24218/4/1)

# 用webStorm、pycharm等编辑器--如果安装了的话
![pycharm编辑器打开](https://yzsunlei.b0.upaiyun.com/2018/20170806203258.png)
