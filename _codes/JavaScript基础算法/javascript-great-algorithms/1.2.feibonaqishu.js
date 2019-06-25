// 递归写法，参数n变大时，会出现浏览器假死现象
function fb1(n){
  if(n <= 2){
    return 1;
  }else{
    return fb1(n-1) + fb1(n-2);
  }
}

// 尾调用优化
function fb2(n, res1 = 1, res2 = 1) {
  if (n <= 2) {
    return res2;
  } else {
    return fb2(n - 1, res2, res1 + res2);
  }
}

// 迭代写法
function fb3(n) {
  var res1 = 1;
  var res2 = 1;
  var sum = res2;
  for (var i = 2; i < n; i++) {
    sum = res1 + res2;
    res1 = res2;
    res2 = sum;
  }
  return sum;
}

// 闭包写法，实现记忆功能，避免了重复计算，提高性能
const fb4 = function() {
  var mem = [0, 1];
  var f = function (n) {
    var res = mem[n];
    if (typeof res !== 'number') {
      mem[n] = f(n - 1) + f(n - 2);
      res = mem[n];
    }
    return res;
  }
  return f;
}();