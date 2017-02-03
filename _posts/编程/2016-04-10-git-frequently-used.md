---
layout: post
title: git解读和常用命令介绍
category: 编程
tag: git
exception: git现在是互联网公司管理项目代码不可或缺的工具，可以这样说，不会使用git，你就别说自己是做互联网的...
readtime: 15
---

## git简介
* git不仅仅是一个版本控制工具，也是一个内容管理系统，工作管理系统
* 现在公司项目开发中，基本上都是用的git来管理团队写的代码。当然也有用svn、cvs的(不如git多)

## git与svn的区别
1. **git是分布式的，而svn不是的**
git和svn一样都有自己的集中式版本库或服务器。但是git更倾向于被使用于分布式模式，每个开发人员从中心的版本库check out代码后会在自己的机器上克隆一份本地的版本库。
2. **git把内容按元数据方式存储，而svn是按文件存储**
git把版本库的元信息隐藏在.git文件夹中，svn隐藏在.svn文件夹中。他们差距很大，.git目录拥有中心版本库上的所有东西，如标签，分支，版本记录等。
3. **git没有一个全局版本号，而SVN有**
这是目前文职svn相比git缺少的一个最大的特性。svn的版本号实际上是一个相应时间的源代码快照，git里面是什么特征与之对应暂不清楚。
4. **git的内容完整性要优于svn**
git的内容存储使用的SHA-1哈希算法。确保代码内容的完整性。
5. **git分支和svn分支不同**
分支在svn中一点都不特别，就是版本库中的另外一个目录。
处理git的分支相当简单和有趣，可以快速的在几个分支间切换。

## git常用工具
GitBash、EGit、SourceTree。
gitbash应该是使用最多的，知道有这几个工具就行了，好好玩下gitbash就好。

##git常用命令汇总
 1. **帮助**
`git --help`
查看帮助(忘了命令就敲它吧)
 2. **创建**
`git clone http://user@domain.com/repo.git`
克隆(复制)一个已存在的库
`git init`
在本地创建一个库
 3. **本地修改**
`git status`
显示工作路径下已修改的文件
`git diff`
显示与上次提交版本文件的不同
 4. **提交与发布**
`git add`
把当前所有修改添加到下次提交中
`git commit -m 'description'`
提交并附带说明
 5. **分支管理**
`git branch`
列出所有的分支
`git checkout <branch>`
切换到某个分支
 6. **合并与重置**
`git merge <branch>`
将分支合并到当前HEAD中
`git rebase <branch>`
将当前HEAD版本重置到分支中
`git rebase --abort`
退出重置
 7. **查看历史**
`git log`
显示所有的提交记录
`git log --author="username"`
显示某个用户的所有提交

## 资料参考
* [话说Svn与Git的区别(以后别再问我了)](http://www.jianshu.com/p/bfec042349ca)
* [Git和SVN之间的五个基本区别](http://www.jianshu.com/p/bfec042349ca)
* [廖雪峰的git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/)(牛逼人物写的wiki，顺便赞一个!)