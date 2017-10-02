# SQLAlchemy教程

# 1、快速入门
# 以下是一个最小的应用
# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
# 
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)
# 
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
# 
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
# 
#     def __repr__(self):
#         return '<User %r>' % self.username
# 
# >>> from yourapplication import db #导入db对象
# >>> db.create_all() #创建表和数据库
# 
# >>> from yourapplication import User #导入User模型
# >>> admin = User('admin', 'admin@example.com') #生成一条数据
# >>> guest = User('guest', 'guest@example.com') #生成一条数据
# 
# >>> db.session.add(admin) #添加到会话
# >>> db.session.add(guest) #添加到会话
# >>> db.session.commit() #提交会话
# 
# >>> users = User.query.all() #查询所有
# >>> admin = User.query.filter_by(username='admin').first() #查询过滤(username='admin')
#
# 2、模型声明
# *简单的例子
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True) #用Column来定义一个列, 主键用 primary_key=Ture 标记
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
# 
#     def __repr__(self):
#         return '<User %r>' % self.username
# *一对多关系
# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     addresses = db.relationship('Address', backref='person', lazy='dynamic') #关系用relationship()函数来表示
# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(50))
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id')) #外键必须用sqlalchemy.schema.ForeignKey来单独声明
# 以上实例中db.relationship(), 我们让他指向Address类并加载那些中的多个, backref是一个同样在Address类上声明新属性的简单方法, lazy决定了SQLAlchemy什么时候从数据库中加载数据
# *多对多关系
# 需要定义一个用于关系的辅助表, 建议不使用模型, 而是采用一个实际的表
# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
# )
# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags,
#         backref=db.backref('pages', lazy='dynamic'))
# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
# 3、增删改查
# *插入数据(insert)
# me = User('admin', 'admin@example.com') #创建python对象
# db.session.add(me) #把它添加到会话
# db.session.commit() #提交会话
# *删除记录(delete)
# db.session.delete(me) #添加会话
# db.session.commit() #提交会话
# *查询记录(query)
# sqlalchemy.orm.query.Query.all #查询所有
# sqlalchemy.orm.query.Query.first #查询第一条
# sqlalchemy.orm.query.Query.filter #查询过滤
# sqlalchemy.orm.query.Query.get #按id来查询
# peter = User.query.filter_by(username='peter').first() #查询返回对应的数据对象，否则返回None
# User.query.order_by(User.username) #以某种规则进行排序
# User.query.limit(1).all() #限制返回的数目
# 用get_or_404()替代get(), first_or_404()代替first() #对不存在的条目返回一个404错误
#
# 4、用bind操作多个数据库
# 在SQLAlchemy 中，一个bind是可以执行SQL语句且通常是一个连接或引擎的东西
# create_all()和drop_all()方法默认作用于声明的所有bind
#
# 5、信号支持
# models_committed #这个信号在修改的模型提交到数据库时发出
# before_models_committed #除了刚好在提交发送前发生
