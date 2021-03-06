---
layout: post
title: 混开源社区你应该懂得5种开源协议(GPL、LGPL、BSD、MIT、Apache)
category: 编程
tag: 开源
exception: 我们在开源社区查看、学习甚至是使用一些开源项目或框架时，基本上很少有人回去注意一下项目根目录会有LICENSE这样一个文件。这里咱们一起来深入理解开源协议这个东西
readtime: 12
---

# 介绍
* 开源协议也即许可协议，其目的就是向使用你产品的人提供一定的权限
* 开源界的5大许可协议：GPL、LGPL、BSD、MIT、Apache，下面我们一起来一一理解

# GNU GPL
* GNU General Public Licence (GPL) 可能是开源界最常用的许可模式。它保证所有开发者的权利，同时为使用者提供足够的复制、分发、修改的权利
* 具体的权利：可自由复制、可自由分发、可用来盈利、可自由修改
* 需要注意的是，分发的时候需要明确提供源代码和二进制文件

# GNU LGPL
* LGPL，GNU的另外一种协议，它对产品所保留的权利比GPL少
* LGPL适合那些用于非GPL或非开源产品的开源类库或框架
* 跟GPL不一样的一点是，使用GPL代码的产品必须也使用GPL协议，开发者不允许将GPL代码用于商业产品，但LGPL绕过了这一限制

# BSD
* BSD在软件分发方面的限制比别的开源协议要少
* 包含两个主要版本，新BSD协议与简单BSD协议，这两种协议经过修正，都和GPL兼容
* 新BSD协议除需要包含一份版权提示和免责声明外，没有任何限制

# MIT
* 可能是几大开源协议中最宽松的一个
* 核心条款：软件及其相关文档对所有人免费，可以任意处置，包括使用、复制、合并、发表、再授权、或者销售
* 唯一限制：软件中必须包含上述版权和许可提示

# Apache
* 除为用户提供版权许可外，还有专利许可。对于涉及专利内容的开发者而言，该协议最适合
* 特别说明：永久免费、全球范围的权利、授权免费，且无版税、授权无排他性、授权不可撤消

# 附带说一下，Creative Commons
* 并非严格意义上的开源许可，主要用于设计
* 主要包含四种基本形式：署名权(必须为原始作者署名)、保持一致、非商业、不能衍生新作品

# 参考资料
* [致Element UI 团队的公开性](https://zhuanlan.zhihu.com/p/25893972)
* [五种开源协议(GPL,LGPL,BSD,MIT,Apache)](http://blog.csdn.net/mic_hero/article/details/50662234)