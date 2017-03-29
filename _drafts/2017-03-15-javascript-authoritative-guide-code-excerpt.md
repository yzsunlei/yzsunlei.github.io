---
layout: post
title: JavaScript权威指南重点代码记录
category: 读书
tag: JavaScript
exception: JavaScript权威指南重点代码记录
readtime: 20
---

# 区分数组和非数组对象
```$xslt
var isArray = Function.isArray || function(o) {
    return typeof o === "object" && Object.prototype.toString.call(o) === "[object Array]";
};
```


# 判定是否为类数组对象
```$xslt
// 字符串和函数有length属性，但是他们可以用typeof检测将其排除
// 在客户端javascript中，DOM文本节点也有length属性，需要用额外判断o.nodeType != 3将其排除
function isArrayLike() {
    if (o &&                                    //o非null、undefined
        typeof o === "object" &&                //o是对象
        isFinite(o.length) &&                   //o.length是有限数值
        o.length >= 0 &&                        //o.length是非负值
        o.length === Math.floor(o.length) &&    //o.length是整数
        o.length < 4294967296)                  //o.length < 2^32
        return true;                            //o是类数组对象
    else
        return false;                           //否则它不是
}
```