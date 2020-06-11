from flask import jsonify, request, flash, render_template
from flask_login import current_user

from app.forms.book import SearchForm
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.change_book import ChangeBook
from app.libs.helper import is_isbn_or_key
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
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
        # return json.dumps(books, default=lambda o:o.__dict__, ensure_ascii=False)
        # return jsonify(books.__dict__)
    else:
        flash('搜索的关键词不符合要求，请重新输入')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    change_book = ChangeBook()
    change_book.search_by_isbn(isbn)
    book = BookViewModel(change_book.first)

    return render_template('book_detail.html', book=book, wishes=trade_wishes_model,
                           gifts=trade_gifts_model, has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)


