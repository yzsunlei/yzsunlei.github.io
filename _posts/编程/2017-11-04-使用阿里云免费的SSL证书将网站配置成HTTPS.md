---
layout: post
title: 使用阿里云免费的SSL证书将网站配置成HTTPS
category: 编程
tag: 阿里云
exception: 现在很多网站都使用HTTPS协议，什么好处就不用说了，今天来整理一份使用阿里云免费的SSL证书将网站配置成HTTPS的教程
readtime: 12
---

# 购买免费证书
* 进入阿里云管理控制台
* 进入安全(云盾)-CA证书服务-购买证书-免费型DV SSL-完成购买
* 补全信息-域名信息-个人信息-相关信息-等待审核
![打开阿里云CA证书控制台](http://yzsunlei.b0.upaiyun.com/201711/20171105202937.png)
![购买免费DV SSL证书](http://yzsunlei.b0.upaiyun.com/201711/20171105203052.png)
![补全证书信息](http://yzsunlei.b0.upaiyun.com/201711/20171105203151.png)
![补全证书信息](http://yzsunlei.b0.upaiyun.com/201711/20171105203539.png)

# 下载并上传到服务器
* 下载证书文件：.pem文件和.key文件
* 上传至服务器Nginx目录下：我的服务器Nginx目录在/etc/nginx，所以我在nginx目录下创建cert/www.jishu88.net/目录，并将下载下来的.pem文件和.key文件上传至该目录
![下载证书文件](http://yzsunlei.b0.upaiyun.com/201711/20171105203724.png)
![下载证书文件](http://yzsunlei.b0.upaiyun.com/201711/20171105203825.png)

# Nginx网站配置
![配置nginx](http://yzsunlei.b0.upaiyun.com/201711/20171105203915.png)
* 配置Nginx：我的网站vhost配置文件在/etc/nginx/sites-enabled目录下的www.jishu88.net文件，打开修改配置如下
```$xslt
server {
        listen 443 ssl default_server;
        listen [::]:443 ssl default_server;

        root /var/www/www.jishu88.net;

        index index.html index.php index.htm;
        server_name www.jishu88.net;
        ssl on;

        ssl_certificate   /etc/nginx/cert/www.jishu88.net/214323867420740.pem;
        ssl_certificate_key  /etc/nginx/cert/www.jishu88.net/214323867420740.key;
        ssl_session_timeout 5m;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;

        location / {
                try_files $uri $uri/ =404;
        }
}
```

# 参考资料
* [用阿里云的免费 SSL 证书让网站从 HTTP 换成 HTTPS](https://ninghao.net/blog/4449)
* [使用阿里云免费SSL证书实现全站HTTPS化](https://segmentfault.com/a/1190000009220479)