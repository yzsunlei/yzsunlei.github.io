<?php
// php后端
header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');

$time = date('r');
// data:前缀和\n\n后缀是SSE协议规范所要求的
echo "data: The server time is: {$time}\n\n";
flush();
?>