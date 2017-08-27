// node.js后端，测试中因跨域问题，只能由curl连接测试
var http = require("http");

http.createServer(function(request, response) {
  response.writeHead(200, {
    "Content-Type": "text/event-stream"
  });
  setInterval(function() {
    // data:前缀和\n\n后缀是SSE协议规范所要求的
    var content = "data:" + new Date().toISOString() + "\n\n";
    response.write(content);
  }, 1000);
}).listen(1234);