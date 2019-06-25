// 最小公倍数
var max =Math.max(a, b);
for ( var i = max; i <= a * b; i++) {
  if (i % a == 0 && i % b == 0) {
    return i;
  }
}