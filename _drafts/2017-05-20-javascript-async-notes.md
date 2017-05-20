1、浏览器操作DOM对象时，脚本角度看是即时生效的，视效角度看，在返回事件队列之前不会渲染DOM对象更改
2、下面代码在webkit中打印有值，在node中没有值，是严格同步的
var obj = {};
console.log(obj);
obj.aaa = 1;
3、setInterval触发频率大约为200次/秒，在node环境，大约能达到1000次/秒
   while触发频率为400万次/秒，在node环境，会达到500万次/秒
   HTML规范推行的延时/间隔的最小值是4毫秒
   setTimeout和setInterval就是不精确的计时工具 
   要想产生短时延时，Node中process.nextTick,浏览器中，尝试垫片技术(shim)：支持requestAnimationFrame就用它，不支持就用setTimeout