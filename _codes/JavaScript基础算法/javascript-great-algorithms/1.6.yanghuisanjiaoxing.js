// 杨辉三角形

// 假设当前行为第m行, 当前元素为第n个元素
function combine (m, n) {
  if (n == 0) {           // 每行第0个元素为1
    return 1;
  } else if (m == n) {    // 每行最后一个元素为1
    return 1;
  } else {                // 其他情况用公式实现
    return combine(m - 1, n) + combine(m - 1, n - 1);
  }
}

function put (len) {
  for (let i = 0; i < len; i++) {      // 遍历每一行
    for (let j = 0; j <= i; j++) {    // 遍历每行上面每个元素
      document.write(combine(i, j) + ' ');
    }
    document.write('<br/>');
  }
}