# python常用包

1、simplejson
几个常用函数: dump, dumps, load, loads.(带s跟不带s的区别是带s是对字符串的处理, 不带s是对文件对象的处理)

2、pymysql

3、tornado: python web框架和异步网络库

4、attrs

5、urllib

6、argparse

7、traceback

8、datetime: 基本的时间和日期类(参考：#http://python.usyiyi.cn/documents/python_278/library/datetime.html)

9、functools

10、sys: 系统相关的参数和函数(参考: #http://python.usyiyi.cn/python_278/library/sys.html)
以下是部分函数:
sys.argv #传递非python脚本的命令行列表
sys.copuright #包含python解释器版权的字符串
sys.path #指定用于模块搜索路径的字符串列表
sys.prefix #给出与平台无关的python文件安装位置的目录前缀
sys.exit #从python退出
sys.flags #显示命令行标志的状态
 
11、csv: 实现类来读取和写入CSV格式的表格数据(参考：#http://python.usyiyi.cn/python_278/library/csv.html)
以下是部分功能函数:
csv.reader(csvfile, dialect='excel', **fmtparams) #返回一个reader对象, 它将遍历csvfile中的每一行
csv.writer(csvfile, dialect='excel', **fmtparams) #返回一个writer对象, 负责将用户的数据装换为分隔字符串并写入给定的类文件对象中

12、time：时间获取和转换(参考: #http://python.usyiyi.cn/documents/python_278/library/time.html)

13、python内建函数(参考：#http://python.usyiyi.cn/translate/python_278/library/index.html)