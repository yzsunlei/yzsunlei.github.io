// 插值查找
function InsertionSearch(arr, val, start, end) {
  var end = end || data.length - 1;
  var start = start || 0;

  var mid = start + (val - arr[low]) / (arr[end] - arr[start]) * (end - start);
  if (arr[mid] == val) {
    return mid;
  }

  if (arr[mid] > val) {
    return InsertionSearch(arr, val, start, mid - 1);
  }
  else {
    return InsertionSearch(arr, val, mid + 1, end);
  }
}