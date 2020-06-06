from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    rigister_blueprint(app)
    return app

def rigister_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
