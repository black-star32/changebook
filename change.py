from app import create_app

app = create_app()

if __name__ == '__main__':  # if中的只在入口文件执行，被其他导入不会执行
    # 生产环境 nginx+uwsgi
    app.run(debug=app.config['DEBUG'], threaded=True)
    # processes = 1

    # http://127.0.0.1:5000/book/search/9787544270878/2
    # http://127.0.0.1:5000/static/wish1111@subnav.png
