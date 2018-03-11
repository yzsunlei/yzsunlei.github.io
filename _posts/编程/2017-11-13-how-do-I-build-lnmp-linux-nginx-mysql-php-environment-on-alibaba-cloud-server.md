---
layout: post
title: 我是如何在阿里云服务器上搭建lnmp(Linux、nginx、mysql、php)环境的
category: 编程
tag: 阿里云、lnmp
exception: 现在创业型的公司或者技术极客做项目，基本上都使用云服务器。今天我们来记录一下怎么在阿里云服务器上搭建lnmp(Linux、nginx、mysql、php)环境
readtime: 8
---

# 远程连接服务器
* 我学习中习惯使用阿里云ECS中ubuntu16 64位系统
* 我使用xshell这款远程连接工具

# 安装lnmp环境
* 更新ubuntu系统的软件源索引，这样才能获取到最新的软件包
```ini
apt-get update
```
* 安装mysql
```ini
apt-get install mysql-service mysql-client
```
* 安装nginx，安装成功后，重启一下nginx服务
````ini
apt-get install nginx
// ngnix的配置文件存放在/etc/nginx/sites-availble/default
// 默认的网站根目录在/var/www
service nginx restart
````
* 安装php环境，我现在都安装php7.0版本的
````ini
apt-get install php7.0-fpm
// 然后安装一些项目需要用到的模块
apt-get install php7.0-mysql php7.0-curl php7.0-gd
````
* 好了，不出意外的话，在浏览器上输入以下地址就可以正常访问默认网站信息了
```ini
http://ip地址
```

# 安装常用的软件
* zip压缩解压工具
````ini
apt-get install zip
````
* git工具
```ini
apt-get install git
```
* 最后用git把项目代码拉下来，在/etc/nginx/sites-availble/下添加一个vhost文件，就可以在服务器上跑项目了

# 参考资料
* [ubuntu通过apt-get方式搭建lnmp环境以及php扩展安装](http://blog.csdn.net/zhxp_870516/article/details/8520358)
* [Ubuntu 16.04 下快速搭建 LNMP环境](http://blog.csdn.net/stfphp/article/details/53492723)
