//求阶乘
function fun(n) {
  if ( n <= 1 ) {
    return 1;
  } else {
    return n * fun(n - 1);
  }
}