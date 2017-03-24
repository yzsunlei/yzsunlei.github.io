---
layout: post
title: 常用mysql整理
category: 编程
tag: mysql
exception: 花了点时间整理下常用mysql语句，后面不记得命令时就可以过来翻一翻...
readtime: 20
---

# mysql操作
```$xslt
// 连接mysql
mysql -h <主机地址> -u <用户名> -p <密码>
// 退出mysql
exit;
```

# 用户操作
```$xslt
// 添加新用户 
grant select,update,delete,insert on <数据库>.<表名> to <用户名>@<登录主机> identified by "<密码>";
// 修改用户密码
mysqladmin -u <用户名> -p <旧密码> password <新密码>;
// 查看所有用户
select distinct user, host from mysql.user;
// 查看某个用户的权限
show grants for '<用户名>'@'localhost';
// 删除用户及权限
drop user <用户名>@'localhost'
```

# 数据库操作
```$xslt
// 创建数据库
create database <数据库名>;
// 显示所有数据库
show databases;
// 删除数据库
drop database <数据库名>;
// 连接数据库
use <数据库名>;
// 导入.sql文件
source /tmp/mysql.sql;
// 显示当前使用的数据库名
select database();
// 显示当前的用户
select user();
```

# 数据表操作
```$xslt
// 创建数据表
create table <表名> (
    <字段名> <类型> <属性>,
    id int(4) not null primary key auto_increment,
);
// 查看数据表结构
desc <表名>;
// 删除数据表
drop table <表名>;
// 修改数据表名
rename table <表名> to <新表名>;
```

# 表字段操作
```$xslt
// 加索引
alter table <表名> add index <索引名> (字段名1, 字段名2);
// 加主关键字的索引
alter table 表名 add primary key <字段名>;
// 加唯一限制条件的索引
alter table 表名 add unique <索引名> (字段名);
// 删除某个索引
alter 表名 drop index <索引名>;
// 添加表字段
alter table <表名> add <字段> 类型 其他;
alter table test_table add deleted int(4) default '0'
// 修改表字段
alter table <表名> change <旧字段名> <新字段名> 类型 其他;
// 删除字段
alter table <表名> drop <字段名>;
```

# 简单数据操作
```$xslt
// 插入数据
insert into <表名> (字段名1, 字段名2, 字段名3, ...) values(值1, 值2, 值3, ...);
// 查询数据
select <字段名1>, <字段名2>, ... from <表名> where <条件表达式>;
// 删除数据
delete from <表名> where <表达式>;
// 修改数据
update <表名> set <字段名> = <值> where <条件表达式>;
```

# 高级查找操作
```$xslt
// 批量查询数据
select * from <表名> where <字段名> in (值1, 值2, 值3);
// concat连接查询结果
select concat(<字段名1>, "-", <字段名2>) as <字段别名> from <表名> where <条件表达式>;
// 使用group by
select * from <表名> group by <字段名>;
// 使用having
// 先按city归组，然后找出city的数量大于10的城市
select city, count(*), min(birth_day) from customer  group by city having count(*) > 10;
// 使用distinct
// 从customer表中查询所有的不重复的city
select distinct city from customer order by id desc;
```

# 备份数据操作
```$xslt
// 导出整个数据库
mysqldump -u <用户名> -p <数据库名> > <导出的文件名>;
// 导出一个表
mysqldump -u <用户名> -p <数据库名> <表名> > <导出的文件名>;
// 导出数据库结构
mysqldump -u <用户名> -p -d -add-drop-table <数据库名> > <导出的文件名>;
// 恢复数据库
mysql -u root -p <数据库名> > <.sql文件名>;
```