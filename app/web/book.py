from flask import jsonify, request

from app.forms.book import SearchForm
from app.spider.change_book import ChangeBook
from app.libs.helper import is_isbn_or_key
from app.view_models.book import BookViewModel, BookCollection
from . import web
import json

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

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        # a = request.args.to_dict()
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        change_book = ChangeBook()

        if isbn_or_key == 'isbn':
            change_book.search_by_isbn(q)
        else:
            ChangeBook.search_by_keyword(q, page)

        # __dict__
        books.fill(change_book, q)
        return json.dumps(books, default=lambda o:o.__dict__, ensure_ascii=False)
        # return jsonify(books.__dict__)
    return jsonify(form.errors)



