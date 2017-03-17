# 廖雪峰的Python教程

# IO编程
# 读文件 文件不存在, 抛出IOError错误
# f = open('test.txt', 'r')
# f.read()
# f.close()
# 
# 建议写法 文件读写随时都可能产生IOError
# try:
# 	f = open('test.txt', 'r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()
# 
# 最佳简洁写法 引入with
# with open('test.txt', 'r') as f:
# 	print(f.read())
# 	
# 调用read()会一次性读取文件全部内容, 为避免内存爆掉, 可以反复的调用read(size)
# 每次读取size个字节, 另外配置文件使用readline()每次读取一行内容
# with open('test.txt', 'r') as f:
# 	for line in f.readlines():
# 		print(line.strip()) # strip()把末尾的'\n'删掉
# 
# 读取二进制文件, 使用'rb'模式打开文件
# f = open('test.jpg', 'rb')
# 读取非UTF-8编码的文本文件, 给open()函数传入encoding参数
# f = open('test.txt', 'r', encoding='gbk')
# 遇到编码不规范的, 可能会遇到UnicodeDecodeError, 可以接受一个errors参数表明怎么去处理
# 最简单的就是忽略
# f = open('test.txt', 'r', encoding='gbk', errors='ignore')
# 
# 写文件：唯一区别就是调用open()函数
# f = open('test.txt', 'w')
# f.write('Hello, world\n')
# f.write('test') #可以反复调用write()来写入文件
# f.close() #务必要调用f.close()来关闭
# 
# 保险的写法还是使用with
# with open('test.txt', 'w') as f:
# 	f.write('hello\n')
# 	f.write('world\n')
# 	f.write('test')
# 
# StringIO在内存中读写str
# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue()) #用于获得写入后的str
# 
# 读取StringIO
# from io import StringIO
# f = StringIO('Hello!\nHi\nGoodbye')
# while True:
# 	s = f.readline()
# 	if s == '':
# 		break
# 	print(s.strip())
# 
# StringIO操作的只能是str, 要操作二进制数据, 就需要使用BytesIO
# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8')) #写入的不是str, 而是经过UTF-8编码的bytes
# print(f.getvalue())
# 
# 注意三点：StringIO不需要close; f.tell() 当前数据流的位置 f.seek(0) 当前数据流位置指向开头
# 
# python内置的os模块可直接调用操作系统提供的接口函数
# import os
# os.name #操作系统的类型
# os.uname() #详细的系统信息, windows上不提供
# os.environ #操作系统定义的环境变量
# os.environ.get('PATH') #获取某个环境变量的值
# 
# 操作文件和目录
# import os
# os.path.abspath('.') #查看当前目录的绝对路径
# os.path.join('/User/michael', 'testdir') #要在某个目录创建新目录, 首先把新目录的完整的路径表示出来
# os.mkdir('/User/michael/testdir') #创建一个新目录
# os.rmdir('/User/michael/testdir') #删掉一个目录
# 
# 不能直接拼字符串,要使用os.path.join(), 这样可以正确处理不同操作系统的路径分割符
# os.path.join()
# 也不要直接去拆字符串
# os.path.split()
# os.path.splitext() #可以直接得到文件扩展名
# 
# 文件操作
# os.rename('test.txt', 'test.py') #对文件重新命名
# os.remove('test.py') #删掉文件
# 复制文件的函数在os模块中不存在, 幸运的是shutil模块提供copyfile的函数
# 
# 利用python的特性来过滤文件
# import os
# [x for x in os.listdir('.') if os.path.isdir(x)] #列出当前目录下的所有目录
# [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'] #列出所有的/py文件
# 
# 使用pickle模块来实现序列化
# import pickle
# d = dict(name='Bob', age=20, score=88)
# pickle.dumps(d) #把任意对象序列化成一个bytes
# 
# f = open('dump.txt', 'wb')
# pickle.dump(d, f) #将对象序列化后写入文件
# f.close()
# 
# f = open('dump.txt', 'rb')
# d = pickle.load(f) #读取到文件内容, 反序列化出对象
# f.close()
# d
# 
# json模块提供完善的python对象到json格式的转换
# import json
# d = dict(name='Bob', age=20, score=88)
# json.dumps(d) #返回一个str, 内容就是标准的JSON
# 
# json_str = '{"age":20, "score": 88, "name": Bob}'
# json.loads(json_str) #从file-like Object中读取字符串并反序列化
# {'age':20, 'score': 88, 'name': 'Bob'}
# 
# 定义Student类, 然后序列化
# import json
# class Student(object):
# 	def __init__(self, name, age, score):
# 		self.name = name
# 		self.age = age
# 		self.score = score
# s = Student('Bob', 20, 88)
# print(json.dumps(s)) #会抛出一个TypeError, 错误原因是Student对象不是一个可序列化为JSON的对象
# 专门写一个转换函数
# def student2dict(std): #Student实例首先被student2dict函数转换成dict, 然后再序列化为JSON
# 	return {
# 		'name': std.name,
# 		'age': std.age,
# 		'score': std.score
# 	}
# 	print(json.dumps(s, default=student2dict)) #这样就可以了
#
# def dict2student(d): #同理, 反序列化时首先转换成一个dict对象
# 	return Student(d['name'], d['age'], d['score'])
# print(json.loads(json_str, object_hook=dict2student))
# 
# 
# 
# 
# 
# 常用内建模块
# 获取当前日期和时间
# from datetime import datetime
# now = datetime.now() #获取当前datetime
# print(now)
# print(type(now))
# 
# 获取指定日期和时间
# from datetime import datetime
# dt = datetime(2014, 4, 19 ,12 ,20) #用指定的日期时间创建datetime
# print(dt)
# 
# 把datetime类型转换成timestamp
# from datetime import datetime
# dt = datetime(2015, 4, 19, 12, 30) 
# dt.timestamp() #把datetime转换成timestamp
#
# 把timestamp转换成datetime
# from datetime import datetime
# t = 1429417200.0
# print(datetime.fromtimestamp(t))
# 
# str转换成datetime: datetime.strtime()
# datetime转换成str: datetime.strftime()
# datetime加减: 需要导入timedelta类
# 
# hashlib 常见的摘要算法: MD5、SHA1
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest()) #d26a53750bc40b38b65a520292f69306
# 分块多次调用update, 计算结果一样
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest()) #d26a53750bc40b38b65a520292f69306
# sha1算法
# import hashlib
# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hahslib?'.encode('utf-8'))
# print(sha1.hexdigest())
#
# 注册和登录
# import hashlib
# db = {'linqinglong': '123456'}
# def register(username, password):
#     if username in db:
#         print('please input anothor username, username has been instored.')
#     else:
#         md5 = hashlib.md5()
#         md5.update((username + password + 'ext').encode('utf-8'))
#         password1 = md5.hexdigest()
#         db[username] = password1
#         print('register syccessful!')

# def login(username, password):
#     if username in db:
#         md5 = hashlib.md5()
#         md5.update((username+password+'ext').encode('utf-8'))
#         password2 = md5.hexdigest()
#         if password2 == db[username]:
#             print('True')
#         else:
#             print('The user is not register.')

# # register('linqinglong','123456')
# # login('linqinglong','12')
# # login('leilei','123456')
# login('linqinglong','123456')
# 
# itertools 提供用于操作迭代对象的函数
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n) #打印自然数序列, 根本停不下来
# 
# itertools.cycle('ABC') #字符串也是序列的一种, 会把传入的序列无限重复下去
# itertools.repeat('A', 3) #把一个元素无限重复下去, 第二个参数可以限定重复次数
# itertools.takewhile(lambda x: x <=10, natuals) #根据条件判断来截断出一个有限的