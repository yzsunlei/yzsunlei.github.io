// 最大公约数
var min = Math.min(a, b);
for ( var  i = min; i > 0; i-- ) {
  if (a % i == 0 && b % i == 0) {
    return i;
  }
}
