// 最大公共子串
function findSubStr(str1, str2) {
  if (str1.length > str2.length) {
    var temp = str1;
    str1 = str2;
    str2 = temp;
  }
  var len1 = str1.length,
    len2 = str2.length;
  for (var j = len1; j > 0; j--) {
    for (var i = 0; i < len1 - j; i++) {
      var current = str1.substr(i, j);
      if (str2.indexOf(current) >= 0) {
        return current;
      }
    }
  }
  return "";
}