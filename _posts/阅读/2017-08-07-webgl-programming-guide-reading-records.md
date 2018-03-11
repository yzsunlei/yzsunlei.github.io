---
layout: post
title: 《WebGL编程指南》阅读记录
category: 阅读
tag: WebGL
exception: 
readtime: 15
---

# 概述
* WebGL页面包含三种语言：HTML5、JavaScript和GLSL ES（着色器代码）

# 入门
* JavaScript只能在`<canvas>`上绘制二维图形，有了WebGL就可以在上面绘制三维图形
* 两种着色器：顶点着色器（Vertex shader）、片元着色器（Fragment shader）
* WebGL程序包括运行在浏览器中的JavaScript和运行在WebGL系统的着色器程序这两部分
* WebGL坐标系统：右手坐标系，X轴是水平的(正方向为右)，Y轴是垂直的(正方向为下)，Z轴是垂直于屏幕(正方向为外)
* attribute变量和uniform变量：attribute变量传输的是那些与顶点相关的数据，uniform变量传输的是那些对于所有顶点都相同(或与顶点相关的数据)
* 获取attribute变量的存储位置：
```javascript
var a_Position = gl.getAttribLocation(gl.program, 'a_Position')
```
* 向attribute变量赋值：
```javascript
gl.vertexAttrib3f(a_Position, 0.0, 0.0, 0.0)
```
* 获取uniform变量的存储位置
```javascript
var u_FragColor = gl.getUniformLocation(gl.program, 'u_FragColor');
```
* 向uniform变量赋值
```javascript
gl.uniform4f(u_FragColor, 0, 0, 0);
```

# 三角形
* 缓冲区对象：可以一次性地向着色器传入多个顶点的数据
* 使用缓冲区对象向顶点着色器传入多个顶点的数据：
```javascript
1、创建缓冲区对象(gl.createBuffer())
2、绑定缓冲区对象(gl.bindBuffer())
3、将数据写入缓冲区对象(gl.bufferData())
4、将缓冲区对象分配给一个attribute变量(gl.vertexAttribPointer())
5、开启attribute变量(gl.enableVertexAttribArray())
```
* 7种基本图形是WebGL可以直接绘制的图形：
```javascript
1、点(gl.POINTS)
2、线段(gl.LINES)
3、线条(gl.LINE_STRIP)
4、回路(gl.LINE_LOOP)
5、三角形(gl.TRIANGLES)
6、三角带(gl.TRIANGLE_STRIP)
7、三角扇(gl.TRIANGLE_FAN)
```
* 矩阵变换：平移、旋转、缩放，纯数学知识..

# 高级变换和动画
* 矩阵变换库：cuon-matrix.js
* setInterval()和requestAnimation()：
```javascript
不管标签页是否被激活，`setInterval()`函数都会反复调用func；
而requestAnimationFrame()只有当标签页处于激活状态时才会生效
```
* 复杂变换的矩阵可以通过一系列基本变换的矩阵相乘得到；通过反复变换和重绘图形可以生成动画效果；

# 颜色和纹理
* 图元光栅化：发生在顶点着色器和片元着色器之间的图形到片元的转化
* 处理过程：顶点坐标-〉图形装配-〉光栅化-〉执行片元着色器
* 纹理映射：将一张图片贴到一个由两个三角形组成的矩形上，这样矩形表面看上去就是这张图片
* WebGL纹理坐标系统中的t轴的方向和PNG、BMP、JPG等格式图片的坐标系统的Y轴方向是相反的
* 纹理设置过程：
```javascript
1、设置纹理坐标(initVertexBuffers)
2、配置和加载纹理(initTextures)
3、为WebGL配置纹理(loadTexture)
4、激活纹理单元(activeTexture)
5、绑定纹理对象(bindTexture)
6、配置纹理对象的参数(texParameteri)
7、将纹理图像分配给纹理对象(texImage2D)
8、将纹理单元传递给片元着色器(uniform1i)
9、在片元着色器中获取纹理像素颜色(texture2D)
```

# OpenGL ES着色器语言
* GLSL ES：专门用来编写着色器的编程语言
* 只支持两种数据类型：数值类型、布尔值类型
* 强类型语言，支持的基本类型：float、int、bool
* 支持矢量和矩阵类型
```javascript
矢量 vec2、vec3、vec4  具有2、3、4个浮点数元素的矢量
     ivec2、ivec3、ivec4  具有2、3、4个整型数元素的矢量
     bvec2、bvec3、bvec4  具有2、3、4个布尔值元素的矢量
矩阵 mat2、mat3、mat4  2*2、3*3、4*4的浮点数元素的矩阵
```
* 支持用户自定义的类型，即结构体
````javascript
struct light {
  vec4 color;
  vec3 position;
}
````
* continue、break、discard语句：关于discard只能在片元着色器中使用，表示放弃当前片元直接处理下一个片元
* 涉及的attribute变量、varying变量和uniform变量都必须声明为全局变量
* attribute变量只能出现在顶点着色器中，只能被声明为全局变量，被用来表示逐顶点的信息
* uniform变量可以用在顶点着色器和片元着色器中，且必须是全局变量，可以是除了数组或结构体之外的任意类型
* varying变量是从顶点着色器向片元着色器传输数据，必须是全局变量，必须在两种着色器中声明同名、同类型的varying变量
* 支持预处理指令，即用来在真正编译之前对代码进行预处理，都以井号开始
```javascript
# ifdef  GL_ES
precision mediump float;
# endif
```

# 进入三维世界
* 立方体由三角形构成
* 视图矩阵可以表示观察者的状态，含有观察者的视点，观察目标点，上方向等信息
* 隐藏面消除、深度冲突

# 光照
* 光源类型：平行光、点光源光、环境光
* 反射类型：漫反射、环境反射

# 层次模型
* 多个简单模型组成复杂模型
* 层次结构模型
* 单关节模型
* 多节点模型

# 高级技术
* 用鼠标控制物体旋转
* 选中物体
* 选中一个表面
* 平视显示器(HUD)
* 在网页上显示三维物体
* 雾化(大气效果)
* 绘制圆形的点
* 半透明的三维物体
* 切换着色器
* 渲染到纹理
* 绘制阴影
* 提高精度
* 加载三维模型
* 自定义类型对象
* 响应上下文丢失

# 附录
* 无须交换缓冲区：提供切换前台与后台缓冲区的机制
* 投影矩阵：正射投影矩阵、透视投影矩阵
* 左手坐标系还是右手坐标系：WebGL并不强制，大部分采用传统的右手坐标系
* 从文件加载着色器
* 本地坐标系：组成场景中的模型或角色的顶点，其坐标是相对于角色本身的原点的
* 世界坐标系：用来移动和放置角色的坐标系
