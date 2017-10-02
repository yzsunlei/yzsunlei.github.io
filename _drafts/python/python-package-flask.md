# Flask web开发框架

# 1、快速入门
# *最小的应用
# from flask import Flask
# app = Flask(__name__)
# 
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
# 
# if __name__ == '__main__':
#     app.run()
# 代码的过程：导入Flask类；实例化该类；使用route()装饰器告诉Flask什么样的URL能触发我们的函数；定义函数返回我们想要显示在浏览器中的信息；使用run()函数让应用运行在本地服务器
# app.run(host='0.0.0.0') #让外部可访问你的服务器
# *调试模式
# app.debug = True;app.run() #适用于启动本地的开发服务器
# app.run(debug=True) #同上
# *路由
# @app.route('/')
# def index():
#     return 'Index Page'
# route()装饰器把函数绑定到对应的URL上
# *变量规则
# @app.route('/post/<int:post_id>') #<int:post_id>这个部分将会作为命名参数传递到你的函数
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
# *唯一URL/重定向行为
# @app.route('/projects/') #访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误
# @app.route('/about') #访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范 URL 去
# *构造URL
# 使用url_for()来给指定得到函数构造URL
# 好处：允许你一次性修改 URL， 而不是到处边找边改；URL 构建会转义特殊字符和 Unicode 数据；妥善处理应用不位于URL的根路径
# *HTTP方法
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()
# *静态文件
# url_for('static', filename='style.css') #文件应该存储在文件系统上的 static/style.css
# *模板渲染
# 使用render_template()方法来渲染模板。将模板名和你想作为关键字的参数传入模板的变量
*访问请求数据
