from flask import Flask, current_app, request, Request

app = Flask(__name__)

# 离线应用，单元测试
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()


with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__
# 上下文表达式必须要返回一个上下文管理器
# with 语句
