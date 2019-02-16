---
layout: post
title: jsonp全方位解析
category: 编程
tag: JavaScript
exception: 在网站开发的过程中，我们有时会用到第三方的数据，但会因为同源安全策略的限制导致Ajax无法发送请求，下面总结下jsonp使用方式和工作原理吧
readtime: 12
---
## 同源策略
* 浏览器的一种安全策略，所谓同源，指的是域名、协议、端口号完全相同
* 限制：cookie、localStorage和IndexDB无法读取；无法操作跨域的iframe里的dom元素；Ajax请求不能发送

## jsonp原理
* 本质是利用了标签(link,img,script,这里使用script)具有可跨域的特性，由服务端返回预先定义好的javascript函数的调用，并且将服务端数据以该函数参数的形式传递过来
* 前端javascript代码
```html
<script>
    function fuc(data){
        console.log(data.name);
    }
</script>
<script src="http://www.baidu.com/api.php?callback=fuc"></script>
```
* 后端php代码
```php
<?php
    $cb = $_GET['callback'];
    $data = array(
                'name'=> 'zs',
                'age'=>18,
                'gender'=>true
            );
    echo $cb.'('.json_encode($data).')';
?>
```

## jsonp优点
* 完美解决在测试或者开发中获取不同域下的数据,用户传递一个callback参数给服务端，然后服务端返回数据时会将这个callback参数作为函数名来包裹住JSON数据，这样客户端就可以随意定制自己的函数来自动处理返回数据了

## jsonp缺点
* jsonp只支持get请求而不支持post请求
* 用session来判断当前用户的登录状态，跨域时会出现问题
* jsonp存在安全性问题

## 特别注意
1. 防止callback参数意外截断js代码,特殊字符单引号双引号,换行符存在风险
2. 防止callback参数恶意添加script标签,造成xss漏洞
3. 防止跨域请求滥用,阻止非法站点恶意调用

## 参考资料
* [jsonp的原理,应用场景,优缺点](https://blog.csdn.net/jian_xi/article/details/66472870)
* [深入理解jsonp跨域请求原理](https://www.cnblogs.com/lijinblogs/p/5782502.html)
* [jsonp 实现原理及代码解析](https://segmentfault.com/a/1190000008127050)