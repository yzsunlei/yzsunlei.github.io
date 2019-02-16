---
layout: post
title: 图片压缩方案整理
category: 编程
tag: Canvas, JavaScript
exception: 现在手机的像素都老高了，前端做图片上传时最好先压缩一下图片大小再进行上传，这样就避免浪费用户的流量，体验也更好。
readtime: 15
---

# 方案整理：
* 方案一：用Canvas的toDataUrl可以将内容导出为base64编码格式的图片，默认采用base64编码将比源文件大1/3,但可以指定导出图片质量，实现上传图片的压缩
* 方案二：将文件读取为dataURL，重新new Image()时按所需比例设置图片的宽度width和高度height可以自动压缩图片大小

# 核心方法：
* canvas转换为dataURL
```javascript
canvas.toDataURL('image/jpeg', 0.8)
```
* File对象转换为dataURL、Blob对象转换为dataURL
```javascript
function readBlobAsDataURL(blob, callback) {
    var a = new FileReader();
    a.onload = function(e) {callback(e.target.result);};
    a.readAsDataURL(blob);
}
```
* dataURL转换为Blob对象
```javascript
function dataURLtoBlob(dataurl) {
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new Blob([u8arr], {type:mime});
}
```
* dataURL图片数据绘制到canvas
```javascript
var img = new Image();
img.onload = function(){
    canvas.drawImage(img);
};
img.src = dataurl;
```
* File,Blob的图片文件数据绘制到canvas
```javascript
readBlobAsDataURL(file, function (dataurl){
    var img = new Image();
    img.onload = function(){
        canvas.drawImage(img);
    };
    img.src = dataurl;
});
```
* Canvas转换为Blob对象并使用Ajax发送
```javascript
var dataurl = canvas.toDataURL('image/png');
var blob = dataURLtoBlob(dataurl);
//使用ajax发送
var fd = new FormData();
fd.append("image", blob, "image.png");
var xhr = new XMLHttpRequest();
xhr.open('POST', '/server', true);
xhr.send(fd)
```

# 参考资料
* [HTMLCanvasElement.toDataURL()](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLCanvasElement/toDataURL)
* [HTML5 canvas drawImage() 方法](http://www.w3school.com.cn/tags/canvas_drawimage.asp)