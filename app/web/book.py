from flask import jsonify, request

from app.forms.book import SearchForm
from app.spider.change_book import ChangeBook
from app.libs.helper import is_isbn_or_key
from . import web


@web.route('/book/search')
def search():
    """
        q：普通关键字 isbn
        page
        ?q=金庸&page=1
    :return:
    """
    # http://127.0.0.1:5000/book/search/9787544270878/1
    # http://127.0.0.1:5000/book/search?q=9787544270878&page=1
    # http://127.0.0.1:5000/book/search?q=郭敬明&page=1
    # Request(包含了几乎全部的http请求信息：查询参数，post参数，remote ip)
    # Response
    # q = request.args['q']
    # # 至少要有一个字符，长度限制
    # page = request.args['page']
    # # 正整数，也有有一个最大值限制

    form = SearchForm(request.args)
    if form.validate():
        # a = request.args.to_dict()
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = ChangeBook.search_by_isbn(q)
        else:
            result = ChangeBook.search_by_keyword(q, page)
        # dict 序列化
        # API
        return jsonify(result)
    return jsonify(form.errors)



