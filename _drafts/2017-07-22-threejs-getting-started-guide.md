---
layout: post
title: Three.js入门指南
category: 阅读
tag: JavaScript, Three.js
exception: Three.js，3D JavaScript库，提供了基于Canvas、SVG标签的渲染器。如何你对绚丽的数据可视化效果，精彩绝伦的游戏画面，逼真的VR视频虚拟体验有点兴趣，那么推荐你看看此书...
readtime: 10
---

# 概述()
* WebGL是基于OpenGL ES2.0的Web标准，可以通过HTML5 Canvas元素作为DOM访问接口
* Three.js：3D JavaScript库，封装了底层的图形接口，基于Canvas和SVG标签的渲染器，很简单的实现三维场景的渲染
* 应用场景：酷炫的网页效果、精彩绝伦的游戏效果、绚丽的数据可视化效果
* 一个典型的Three.js程序至少要包括渲染器(Renderer)、场景(Scene)、照相机(Camera)，以及你在场景中创建的物体

# 照相机(Camera)：定义了三维空间到二维屏幕的投影方式
* 分类：正交投影照相机、透视投影照相机
* 透视投影获得结果是类似人眼在真实世界中看到的有“近大远小”的效果，正交投影获得的结果是如同数学几何课上画的立体图形一样
* 正交投影照相机构造函数
```javascript
THREE.OrthographicCamera(left, right, top, bottom, near, far)
```
* 透视投影照相机的构造函数
```javascript
THREE.PerspectiveCamera(fov, aspect, near, far)
```

# 几何形状(Geometric)：快速创建三维立体
* 立方体（CubeGeometry）
```javascript
THREE.CubeGeometry(width, height, depth, widthSegments, heightSegments, depthSegments)
```
* 平面（PlaneGeometry）
```javascript
THREE.PlaneGeometry(width, height, widthSegments, heightSegments)
```
* 球体（SphereGeometry）
```javascript
THREE.SphereGeometry(radius, segmentsWidth, segmentsHeight, phiStart, phiLength, thetaStart, thetaLength)
```
* 圆形（CircleGeometry）
```javascript
THREE.CircleGeometry(radius, segments, thetaStart, thetaLength)
```
* 圆柱体（CylinderGeometry）
```javascript
THREE.CylinderGeometry(radiusTop, radiusBottom, height, radiusSegments, heightSegments, openEnded)
```
* 正四面体（TetrahedronGeometry）、正八面体（OctahedronGeometry）、正二十面体（IcosahedronGeometry）
```javascript
THREE.TetrahedronGeometry(radius, detail)
THREE.OctahedronGeometry(radius, detail)
THREE.IcosahedronGeometry(radius, detail)
//  radius 是半径； detail 是细节层次（Level of Detail）的层数
```
* 圆环面（TorusGeometry）
```javascript
THREE.TorusGeometry(radius, tube, radialSegments, tubularSegments, arc)
```
* 圆环结（TorusKnotGeometry）
```javascript
THREE.TorusKnotGeometry(radius, tube, radialSegments, tubularSegments, p, q, heightScale)
```
* 文字形状（TextGeometry）：需要下载和应用额外的字体库
```javascript
<script type="text/javascript" src="helvetiker_regular.typeface.js"></script>
THREE.TextGeometry(text, parameters) // parameters是参数对象
```
* 自定义形状（使用 Geometry 类）
```javascript
THREE.Geometry()
```

# 材质(Materials)：控制物体的颜色、纹理、光照模式等
* 基本材质（BasicMaterial）：渲染后始终为该材质的颜色，不会由于光照产生明暗、阴影效果
```javascript
THREE.MeshLambertMaterial(opt)
```
* Lambert 材质（MeshLambertMaterial）：只考虑漫反射而不考虑镜面反射的效果，对金属、镜面等表现不合适
```javascript
new THREE.MeshLambertMaterial({
 color: 0xffff00
})
```
* `Phong 材质（MeshPhongMaterial）：考虑了镜面反射的效果，对于金属、镜面的表现尤为适合
```javascript
new THREE.MeshPhongMaterial({
 color: 0xffff00
});
```
* 法向材质：可以将材质的颜色设置为其法向量的方向
```javascript
new THREE.MeshNormalMaterial()
```
* 纹理贴图：倒入图像作为材质
```javascript
var texture = THREE.ImageUtils.loadTexture('../img/0.png');
var material = new THREE.MeshLambertMaterial({
 map: texture
});
```
* 棋盘格：黑白相间的图像
```javascript
var texture = THREE.ImageUtils.loadTexture('../img/chess.png', {}, function() {
 renderer.render(scene, camera);
});
texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
texture.repeat.set(4, 4);
```

# 网格(Mesh)：网格是由顶点、边、面等组成的物体
* 最常见的物体就是网格（Mesh），其他物体包括线段（Line）、骨骼（Bone）、粒子系统（ParticleSystem）
```javascript
var mesh = new THREE.Mesh(new THREE.CubeGeometry(1, 2, 3),
 new THREE.MeshLambertMaterial({
 color: 0xffff00
 })
);
scene.add(mesh);
```
* 三种常用属性修改：scale、rotation、position
```javascript
mesh.position = new THREE.Vector3(1.5, -0.5, 0);
```

# 动画(Animation)：利用了人眼的视觉暂留特性，快速地变换画面
* NTSC标准的电视FPS是30，PAL标准的电视FPS是25，电影的FPS标准为24
* setInterval 方法
````javascript
setInterval(func, msec)
````

# 外部模型()


# 光与影(Lights)



# 着色器()



# 参考资料
* [《Three.js 入门指南》](http://www.ituring.com.cn/book/1272)
* [张雯莉个人网站](http://zhangwenli.com/)