// 判断一个数是不是素数
function isPrinme(n) {
  if (n == 0 || n == 1) {
    return false;
  }
  if (n == 2) {
    return true;
  }
  for (var i = 2; i < Math.sqrt(n); i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

// 输出n内的所有素数
function prinmeN(n) {
  var flag = 0;
  var result = [];
  if (n == 0 || n == 1) {
    result = [];
  } else if (n == 2) {
    result = [2];
  } else if (n == 3 || n == 4) {
    result = [2, 3]
  } else {
    result.push(2, 3);
    for (var i = 5; i <= n; i++) {
      for (var j = 2; j <= Math.sqrt(i); j++) {
        if (i % j == 0) {
          flag = 1;
          break;
        } else {
          flag = 0;
        }
      }
      if (flag == 0) {
        result.push(i);
      }
    }

  }
  return result;
}