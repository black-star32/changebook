from flask import Flask, current_app, request, Request

app = Flask(__name__)

ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config['DEBUG']
ctx.pop()
