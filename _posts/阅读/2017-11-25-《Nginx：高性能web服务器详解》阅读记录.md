---
layout: post
title: 《Nginx：高性能web服务器详解》阅读记录
category: 阅读
tag: nginx
exception: Nginx服务器是一个广受好评的产品，我现在构建一些小项目基本上都跑在nginx上。这本书应该是属于运维人员必读的书列，我作为开发工程师只是因为兴趣，泛泛而看，下面我把我这几天重点看的内容记录下来，分享予你。
readtime: 15
---

# 架构初探
* Nginx模块化结构：习惯上将Nginx设计到的模块分为核心模块、标准HTTP模块、可选HTTP模块、邮件服务模块以及第三方模块等5大类
* Nginx核心模块主要包含对两类功能的支持，一类是主体功能，包括进程管理、权限控制、错误日志记录、配置解析等，另一类是用于响应请求事件必须的功能，包括时间驱动机制、正则表达式解析等
* Web请求处理机制：多进程方式、多线程方式、异步方式
* Nginx如何处理请求的：结合多进程机制和异步机制对外提供服务，异步机制使用的异步非阻塞方式
* 事件驱动模型：一般由事件收集器(专门负责收集所有的事件)、事件发送器(负责将收集器收集到的事件分发到目标对象中的)和事件处理器(主要负责具体事件的响应工作)三部分组成
* Nginx中事件驱动模型：最常见的包括select模型、poll模型、epoll模型，还支持rtsig模型、dev/poll模型和eventport模型等
* Nginx服务器架构示意图
![Nginx服务器架构示意图](http://yzsunlei.b0.upaiyun.com/201711/20171125194531.png)

# Rewrite功能
* Rewrite功能是大多数web服务器支持的一项功能，也是比较实用的一项功能。nginx服务器使用ngx_http_rewrite_module模块解析和处理Rewrite功能的相关配置
* Rewrite常用的几种使用场景：域名跳转、域名镜像、独立域名、目录合并、防盗链等。
* 下面是一个目录合并的实例，这也是一种使用搜索引擎的规则来提高网站在有关搜索引擎内排名的方式
```ini
server
{
  listen 80;
  server_name www.myweb.name;
  location ^~ /server
  {
    rewrite ^/server-([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)\.htm$ /server/$1/$2/$3/$4/$5.html last;
    break;
  }
 
}
# 上面配置我们只需要在客户端输入http://www.myweb.com/server-12-34-56-78-9.html就可以访问到服务器上[root]/server/12/34/56/78/9.htm文件了
```

# 代理服务
* 代理服务，通常也称正向代理服务，当然对应的也有反向代理服务。
* 局域网内的机器借助代理服务访问局域网外的网站，主要为了增强局域网内部网络的安全性，使得网外的威胁因素不容易影响到网内
* 负载均衡：这是Nginx服务器反向代理服务的一个重要用途。
* Nginx服务器实现了静态的基于优先级的加权轮询算法，主要配置是proxy_pass指令和upsteam指令
```ini
upstream backend                                # 配置后端服务器组
{
  server 192.168.1.2:80  weight=5;
  server 192.168.1.3:80  weight=2;
  server 192.168.1.4:80;                        # 默认weight=1
}
server
{
  server_name www.myweb.com;
  index index.html index.htm;
  location / {
    proxy_pass http://backend;
    proxy_ser_header  Host $host;
  }
}
# 以上配置中backend服务器组中的服务器被赋予了不同的优先级，weight变量的值就是轮询策略中的“权值”
```

# 缓存机制
* web缓存机制的优势：减轻后端服务负载，减少web服务器和后端服务器之间的网络流量，减轻网络拥塞，减少数据传输延迟等
* 常用的5种配置方案：404错误驱动web缓存，资源不存在驱动web缓存，基于memcached的缓存，Proxy Cache的缓存机制，Nginx和Squid组合的缓存方案
```ini
http {
  proxy_cache_path  /myweb/server/proxycache levels=1:2 max_size=2m inactive=5m loader_sleep=1m; keys_zone=MYPROXYCACHE:10m
  # 配置了缓存数据存放路径和Proxy Cache使用的内存Cache空间
  proxy_temp_path /myweb/server/tmp; # 配置响应数据的临时存放目录
  server {
    # 其他配置
    location / {
      # 其他配置
      proxy_pass http://www.myweb.name/;
      proxy_cache MYPROXYCACHE; # 配置使用MYPROXYCACHE这个keys_zone
      proxy_cache_valid 200 302 1h; #配置200状态和302状态额响应缓存1小时
      proxy_cache_valid 301 1d; # 配置301状态额响应缓存1天
      proxy_cache_valid any 1m; # 配置其他状态的响应数据缓存1分钟
    }
  }
}
# 以上是Proxy Cache的缓存机制方案的配置实例
```

# 邮件服务
* 邮件服务是Nginx服务器的基础功能之一，也是最初开发的主要需求
* 一套完整的邮件服务主要有三类主要部件：用户代理、邮件服务器和用于实现传输的简单邮件传送协议(SMTP)
```ini
mail 
{
  server_name mail.myweb.name;
  auth_http mail.postfix.cn:80/auth.php;   # 配置了HTTP认证的地址
   imap_capabilities "IMAP4rev1" "UIDPLUS" "IDLE" "LITERAL +" "QUOTA";
    pop3_auth plain apop cram-md5;
    pop3_capabilities "LAST" "TOP" "USER" "PIPELINING" "UIDL";
    smtp_auth login plain cram-md5;
    smtp_capabilities "SIZE 10485760" ENHANCEDSTATUSCODES 8BITMIME DSN;
    xclient off;

    server {
        listen 25;
        protocol smtp;
        # The RFC 2821 timeout should be 300 seconds
        timeout 300s;
    }
    server {
        listen 110;
        protocol pop3;
        proxy on;
        proxy_pass_error_message on;
    }
    server {
        listen 143;
        protocol imap;
        proxy on;
    }
    server {
        listen 587;
        protocol smtp;
        timeout 300s;
    }
}
# 以上是一个比较完整的邮件服务配置实例
```

# 参考资料
* [《Nginx：高性能web服务器详解》豆瓣地址](https://book.douban.com/subject/25773187/)
* [高性能Web服务器 NGINX 简明教程 ](http://www.imooc.com/article/18416?block_id=tuijian_wz)
* [高性能web服务器nginx---实战篇](http://blog.51cto.com/masters/1597131)
* [Nginx高性能web服务器系列](http://blog.51cto.com/liangey/1631402)