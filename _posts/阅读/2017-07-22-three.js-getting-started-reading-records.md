---
layout: post
title: 《Three.js入门指南》阅读记录
category: 阅读
tag: JavaScript, Three.js
exception: Three.js，3D JavaScript库，提供了基于Canvas、SVG标签的渲染器。如何你对绚丽的数据可视化效果，精彩绝伦的游戏画面，逼真的VR视频虚拟体验有点兴趣，那么推荐你看看此书...
readtime: 10
---

# 概述
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
* requestAnimationFrame 方法
````javascript
// 要注意requestAnimationFrame的兼容性问题
function draw() {
 mesh.rotation.y = (mesh.rotation.y + 0.01) % (Math.PI * 2);
 renderer.render(scene, camera);
 id = requestAnimationFrame(draw);
}
````
* 对比：requestAnimationFrame适用于对于时间较为敏感的环境(但是动画逻辑更加复杂)；setInterval则可在保证程序的运算不至于导致延迟的情况下提供更加简洁的逻辑(无需自行处理时间)
* 使用stat.js记录FPS
```javascript
// 在页面初始化的时候，对其初始化并将其添加至屏幕一角
var stat = null;
function init() {
 stat = new Stats();
 stat.domElement.style.position = 'absolute';
 stat.domElement.style.right = '0px';
 stat.domElement.style.top = '0px';
 document.body.appendChild(stat.domElement);
 // Three.js init ...
}
```

# 外部模型(Model)：允许用户导入由3ds Max等工具制作的三维模型
* 使用前需要下载并导入一系列的外部文件的辅助函数
* 目前支持的模型格式：`*.obj, *.mtl、*.dae、*.ctm、*.ply、*.stl、*.wrl、*.vtk`
* 无材质的模型：
```javascript
<script type="text/javascript" src="OBJLoader.js"></script>
<script>
var loader = new THREE.OBJLoader();
loader.load('../lib/port.obj', function(obj) {
 mesh = obj; //储存到全局变量中
 scene.add(obj);
});
</script>
```
* 有材质的模型：需要在回调函数中设置模型的材质
```javascript
<script type="text/javascript" src="MTLLoader.js"></script>
<script type="text/javascript" src="OBJMTLLoader.js"></script>
<script>
var loader = new THREE.OBJMTLLoader();
loader.addEventListener('load', function(event) {
 var obj = event.content;
 mesh = obj;
 scene.add(obj);
});
loader.load('../lib/port.obj', '../lib/port.mtl');
</script>
```

# 光与影(Lights)：很大程度上丰富了图像渲染的效果
* 四种常见的光源：环境光、平行光、点光源、聚光灯
* 环境光：场景整体的光照效果，若干光源多次反射，没有明确的光源位置
```javascript
var light = new THREE.AmbientLight(0xffffff);
```
* 点光源：补给光源大小，亮度线性递减
* 平行光：
```javascript
THREE.DirectionalLight(hex, intensity)
```
* 聚光灯：能够朝一个方向折射光线
```javascript
THREE.SpotLight(hex, intensity, distance, angle, exponent)
```
* 阴影：明暗是相对的
```javascript
在Three.js中，能形成阴影的光源只有 THREE.DirectionalLight 与 THREE.SpotLight
而相对地，能表现阴影效果的材质只有 THREE.LambertMaterial 与 THREE.PhongMaterial
```
```javascript
对于光源以及所有要产生阴影的物体调用：
xxx.castShadow = true;
对于接收阴影的物体调用：
xxx.receiveShadow = true;
对于聚光灯，需要设置：
shadowCameraNear 、 shadowCameraFar 、 shadowCameraFov 三个值
对于平行光，需要设置：
shadowCameraNear 、 shadowCameraFar 、 shadowCameraLeft 、shadowCameraRight 、 shadowCameraTop 以及 shadowCameraBottom 六个值
```

# 着色器(Shader)：可以对先前渲染的结果作修改
* 屏幕上呈现页面的最后一步，用它可以对先前渲染的结果作修改，包括对颜色、位置等信息的修改，甚至对先前的结果做后处理，实现高级的渲染效果
* 着色器通常分为几何着色器(Geometry Shader)、顶点着色器(Vertex Shader)、片元着色器(Fragment Shader)等

# 参考资料
* [《Three.js 入门指南》](http://www.ituring.com.cn/book/1272)
* [张雯莉个人网站](http://zhangwenli.com/)