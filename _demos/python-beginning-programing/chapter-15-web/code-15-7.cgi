#!/usr/bin/env python
# coding=utf-8
# 带有HTML表单的问候脚本

import cgi
form = cgi.FieldStorage()

name = form.getvalue('name', 'world')

print """Content-type: text/html
<html>
<head>
    <title></title>
</head>
<body>
    <h1>Hello, %s!</h1>
</body>
</html>
""" % name



