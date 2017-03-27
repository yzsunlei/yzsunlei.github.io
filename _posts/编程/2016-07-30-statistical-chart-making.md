---
layout: post
title: 统计图表绘制库对比
category: 编程
tag: JavaScript
exception: 目前各种各样的图表图形绘制插件或库都是基于这三种技术：VML、SVG、Canvas。大多数框架都支持简单的条形图、折线图、饼状图等基本图形，少数复杂点的框架还支持维恩图、热图、进化图、二维散点图、二维散点气泡图、三维散点图等，下面就三个不同层次的图表绘制库进行简要的解析
readtime: 15
---

## [chart.js](http://www.bootcss.com/p/chart.js/docs/)
* 比较简单的一个图表绘制库。是一个简单、面向对象、为设计者和开发者准备的图表绘制工具库。
* 6种图表类型：曲线图(Line charts) 、柱状图(Bar charts)、雷达图或蛛网图(Radar charts)、饼图(Pie charts)、极地区域图(Polar area charts)、环形图(Doughnut charts)
* 基于HTML5：Chart.js基于HTML5 canvas技术，支持所有现代浏览器，并且针对IE7/8提供了降级替代方案。
* 简单、灵活：Chart.js不依赖任何外部工具库，轻量级(压缩后仅4.5k)，并且提供了加载外部参数的方法。
* 使用步骤：
```$xslt
 1. 引入Chart.js
<script src="Chart.js" type="text/javascript"></script>
 2. 创建图表容器
<canvas id="Chart" width="400" height="400"></canvas>
 3. 实例化Chart对象
var ctx = document.getElementById('Chart').getContext("2d");
var newChart = new Chart(ctx);
 4. 配置数据、生成图表
newChart.Bar(data, options);
```

* [【中文文档】(http://www.bootcss.com/p/chart.js/docs/index.html)](http://www.bootcss.com/p/chart.js/docs/index.html)
* [【英文文档】(http://www.chartjs.org/docs)](http://www.chartjs.org/docs)

## [echarts](http://echarts.baidu.com/index.html)
* 功能比较强大的图表绘制库
纯JavaScript的图表库，可以流畅的运行在PC和移动设备上，兼容当前绝大部分的浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖轻量级的Canvas类库ZRender，提供直观、生动，可交互，可高度定制的数据可视化图表。
ECharts提供了常规的折线图，柱状图，散点图，饼图，K线图，用于统计的盒形图，用于地理数据可视化的地图，热力图，线图，用于关系数据可视化的关系图，treemap，多维数据可视化的平行坐标，还有用于BI的漏斗图，仪表盘，并且支持图与图之间的混搭。
* 使用步骤：
```$xslt
 1. 准备一定大小的Dom
 <div id="ECharts" style="height: 400px;"></div>
 2. 引入模块化单文件echart.js
 <script src="http://echarts.baidu.com/build/dist/echarts.js" type="text/javascript"></script>
 3. 为模块加载器配置echarts和所需图表的路径
    require.config({
        paths: {
            echarts: 'http://echarts.baidu.com/build/dist'
        }
    });
 4. <script>标签内动态加载echarts和所需图表，回调函数中可以初始化图表并驱动图表的生成
    require(
      [
        'echarts',
        'echarts/chart/bar'
      ], 
      function (ec) {
        var myChart = ec.init(document.getElementById('Echarts'));
        var option = {
          tooltip: {
            show: true
          },
          legend: {
            data: ['销量']
          },
          xAxis: [
            {
              type: 'category',
              data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
            }
          ],
          yAxis: [
            {
              type: 'value'
            }
          ],
          series: [
            {
              "name": "销量"，
              "type": "bar",
              "data": [5, 20, 40, 10, 10, 20]
            }
          ]
        };
        myCharts.setOption(option);
    });
```

* 【官方文档】[http://echarts.baidu.com/tutorial.html](http://echarts.baidu.com/tutorial.html)
* 【示例演示】[http://echarts.baidu.com/examples.html](http://echarts.baidu.com/examples.html)

##[highcharts](http://www.highcharts.com/)
* 高大上的感觉但是不免费的图表绘制库。
* 功能支持：Highcharts目前支持直线图、曲线图、面积图、饼图、散点图等多达18种不同类型的图表。
* 兼容性好：Highcharts支持目前所有的现代的浏览器，包括IE6+、iPhone/iPad、Android。在标准(W3C标准)浏览器中使用SVG技术渲染图形，在遗留的IE浏览器中使用VML技术来绘图。
* 使用步骤：
```$xslt
1. 引入资源
 基本文件
<script src="js/jquery.min.js" type="text/javascript"></script>
<script SRC="js/highchart.js" type="text/javscript"></script>
 图表导出功能
<script src="modules/exporting.js" type="text/javascript"></script>
 图表主题
<script scr="themes/gray.js" type="text/javascript"></script>
 2. 创建容器
 <div id="container" style="min-height: 800px;height: 400px;">
 3. 渲染表格数据
$(function() {
    $('#container').highcharts({
        chart: {
          type: 'column'
        },
        title: {
          text: 'My first Highcharts chart'
        },
        xAxis: {
          categories: ['my', 'first', 'chart']
        },
        yAxis: {
          title: {
            text: 'something'
          }
        },
        series: [{
          name: 'Jane',
          data: [1, 0, 4]
        }, {
          name: 'John',
          data: [5, 7, 3]
        }]
    });
 });
```

* 【文档教程】[(http://www.hcharts.cn/docs/index.php?doc=start)](http://www.hcharts.cn/docs/index.php?doc=start)
* 【示例演示】[(http://www.hcharts.cn/demo/index.php)](http://www.hcharts.cn/demo/index.php)
