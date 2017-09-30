---
layout: post
title: 开始使用Laravel的一些姿势
category: 编程
tag: php，laravel
exception: 没想到现在我又捡起大学时的最爱之一(写php)，这次我们还使用了php的一个巨匠级的框架laravel，今天来几点笔记，做一个好的开始。
readtime: 8
---

# 使用Wamp开发环境
* 官网(http://www.wampserver.com/)，先去下载安装了
* wamp是一个集apache、mysql、php的windows集成开发环境，当然Linux下对应的就叫lamp了。
* 不过现在nginx用的要比apache多了，不过现在习惯了本地开发用wamp(win+apache+mysql+php)，服务器上部署用lnmp(ubantu+nginx+mysql+php)
* 现在语言种类繁多，lamp也可以认为是Windows下的Apache+Mysql/MariaDB+Perl/PHP/Python，感觉好多知识了

# 使用laravel框架创建项目骨架
* Laravel 利用 Composer(http://www.phpcomposer.com/) 来管理依赖，我把Composer认为跟node.js的npm一样了
* 方法一：通过 Laravel 安装器
```haml
// 先使用 Composer 下载 Laravel 安装程序
composer global require "laravel/installer"
// 然后将 $HOME/.composer/vendor/bin 目录放到环境变量里面去
// 最后使用 laravel 命令创建项目了，不过速度好慢
laravel new project
```
* 方法二：使用 composer 直接安装
```haml
// 先找个目录，运行这个命令就好，不过首次也很慢
composer create-project --prefer-dist laravel/laravel project
```

# 建立虚拟目录
* 一般电脑上不会只跑一个项目的，所以我想给项目建一个虚拟目录然后通过一个域名直接访问项目
* 先在apache的httpd-vhosts.conf文件中添加一个虚拟目录
```haml
<VirtualHost *:80>
	ServerName local.project.com
	DocumentRoot e:/project/project-php/public
	<Directory  "e:/project/project-php/public">
		Options +Indexes +Includes +FollowSymLinks +MultiViews
		AllowOverride All
		Require local
	</Directory>
</VirtualHost>
```
* 然后在本地.hosts文件添加域名映射
```haml
// .hosts这个文件在c盘搜就出来了
127.0.0.1  local.project.com
```
* 最后apache正常启动了，浏览器输入local.project.com就可以看到laveral的hello world页面了

# 相关资料
* [Laravel China 社区 - 一个很好的社区，github开源有这个社区的完整代码](https://laravel-china.org/)
* [Laravel 5.5 中文文档](https://d.laravel-china.org/docs/5.5/)
* [Laravel 5.1 LTS 速查表](https://cs.laravel-china.org/)