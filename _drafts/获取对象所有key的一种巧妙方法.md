// 获取对象的所有key的方法
Object.keys || function() {
	var arr = [];
	// 很巧妙的方法
	for (arr[arr.length] in Object);
}