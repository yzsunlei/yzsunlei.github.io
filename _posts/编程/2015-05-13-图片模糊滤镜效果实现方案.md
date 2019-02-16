---
layout: post
title: 图片模糊滤镜效果实现方案
category: 编程
tag: CSS3
exception: 
readtime: 6
---

# 简介
最近很流行图片高斯模糊处理，让网站的图片看起来有高大上的效果。应用点：如网站Banner、大气背景图等。模糊背景（blurred backgrounds）是一个很常见的设计效果，也被称为背景虚化，在网页和App的设计中屡见不鲜。虚化的界面设计直观的给人一种干净自然的视觉感 受，因此，模糊背景的基调会使整个界面看起来更柔美。合理运用虚化背景可以将界面效果提高一个档次。

# 案例素材
- 背景虚化案例
* 优秀案例参考：[http://www.uisdc.com/blurred-background-website-design](http://www.uisdc.com/blurred-background-website-design)
* 国外优秀案例：[http://www.onextrapixel.com/2013/12/06/effective-use-of-blurred-images-in-web-design/](http://www.onextrapixel.com/2013/12/06/effective-use-of-blurred-images-in-web-design/)
* 透明效果网站：[http://www.uisdc.com/transparency-website-design](http://www.uisdc.com/transparency-website-design)

- 背景图片资源
* 模糊图片下载：[http://vdisk.weibo.com/s/dt23BkiXHbFmp](http://vdisk.weibo.com/s/dt23BkiXHbFmp)
* 150+背景素材：[http://vdisk.weibo.com/s/aj4Q1htdUrYaV](http://vdisk.weibo.com/s/aj4Q1htdUrYaV)
* 模糊景观背景：[http://vdisk.weibo.com/s/aj4Q1hteoqwVO](http://vdisk.weibo.com/s/aj4Q1hteoqwVO)
* 模糊材质纹理：[http://pepsized.com/100-free-blurry-textures/](http://pepsized.com/100-free-blurry-textures/)

# 实现方案
- 方案一：图片高斯模糊
* 直接利用PS处理图片，使图片高斯模糊，调节参数可达到不同效果。
* 同时可以结合透明度达到更加优质的效果，如参考网易云音乐播放器。
![直接利用PS处理](https://yzsunlei.b0.upaiyun.com/2018/asfdsaf1.jpg)
* 案例：[http://www.xuanfengge.com/demo/201410/blur/demo.html](http://www.xuanfengge.com/demo/201410/blur/demo.html)
![网易云音乐播放器](https://yzsunlei.b0.upaiyun.com/2018/sadsadas.jpg)
![网易云音乐播放器](https://yzsunlei.b0.upaiyun.com/2018/asfdsf.jpg)
![网易云音乐播放器](https://yzsunlei.b0.upaiyun.com/2018/sdfgvfsdg.jpg)

- 方案二：使用CSS3 filter
* CSS3 高斯模糊效果 “-webkit-filter:blur(2px)”。这个效果很赞，结合动画效果更佳。
* 案例：[http://xuanfengge.com/demo/201410/blur/index.html](http://xuanfengge.com/demo/201410/blur/index.html)
![高斯模糊效果](https://yzsunlei.b0.upaiyun.com/2018/dsfdsgf.gif)
```css
.bac_img{
    -webkit-filter:blur(0px);
    -moz-filter:blur(0px);
    -o-filter:blur(0px);
    filter:blur(0px);
    -webkit-transition: all 0.3s linear;
    -moz-transition: all 0.3s linear;
    -o-transition: all 0.3s linear;
    transition: all 0.3s linear;
}
.bac_img:hover{
    -webkit-filter:blur(18px);
    -moz-filter:blur(18px);
    -o-filter:blur(18px);
    filter:blur(18px);
}
```