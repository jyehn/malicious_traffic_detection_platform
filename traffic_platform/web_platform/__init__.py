# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class MyFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
    ))
app=MyFlask(__name__)

# import sys
# sys.path.append('..')
from .controller import message


# # 注意： 只能在flask对象声明后引入
# from web_platform.model import User,Category

# # 查看环境变量是否配置成功
# import  os
# # print (os.environ.keys())
# print (os.environ.get('FLASKR_SETTINGS'))


#加载配置文件内容（数据库方案）
app.config.from_object('traffic_platform.web_platform.setting')  #模块下的setting文件名，不用加py后缀 
# app.config.from_envvar('FLASKR_SETTINGS')   #环境变量，指向配置文件setting的路径

# #创建数据库对象 
# db = SQLAlchemy(app)