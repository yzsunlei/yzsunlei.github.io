---
layout: post
title: 整理几点php7的新特性
category: 编程
tag: php
exception: 当初在学校自学php编程的时候还是php5.4，也好久没用php写项目了，现在用起来已经是php7.2的新版本了。今天花点时间理理php7很好用的几点新特性
readtime: 8
---

## Null 合并操作符
```php
// 如果 $_GET['user'] 不存在返回 'nobody'，否则返回 $_GET['user'] 的值
$username = $_GET['user'] ?? 'nobody';
// 类似的三元运算符
$username = isset($_GET['user']) ? $_GET['user'] : 'nobody';
```

## 组合比较符
```php
echo 1 <=> 1; // 0
echo 1 <=> 2; // -1
echo 2 <=> 1; // 1
```

## 匿名类
```php
// interface Logger;
// class Application;
$app = new Application;
$app->setLogger(new class implements Logger {
    public function log(string $msg) {
        echo $msg;
    }
});
```

## 通过 define() 定义常量数组
```php
define('ANIMALS', [
    'dog',
    'cat',
    'bird'
]);

echo ANIMALS[1]; 
// 输出 "cat"
```

## 参数类型声明和返回值类型声明
```php
// Coercive mode
function sumOfInts(int ...$ints)
{
    return array_sum($ints);
}

var_dump(sumOfInts(2, '3', 4.1));
// 示例输出int(9)
```

## Closure::call()闭包调用
```php
class A {private $x = 1;}

// Pre PHP 7 代码
$getXCB = function() {return $this->x;};
$getX = $getXCB->bindTo(new A, 'A'); // intermediate closure
echo $getX();

// PHP 7+ 代码
$getX = function() {return $this->x;};
echo $getX->call(new A);
```

## Generator 生成器可以返回表达式
```php
$gen = (function() {
    yield 1;
    yield 2;

    return 3;
})();

foreach ($gen as $val) {
    echo $val, PHP_EOL;
}

echo $gen->getReturn(), PHP_EOL;
```

## 整除函数 intdiv()
```php
var_dump(intdiv(10, 3));
// 输出int(3)
```

## 参考资料
* [php7新特性](http://php.net/manual/zh/migration70.new-features.php)
* [PHP 7 新特性](http://www.runoob.com/w3cnote/php7-new-features.html)
* [PHP 7 值得期待的新特性（下）](http://www.thinkphp.cn/topic/34799.html)