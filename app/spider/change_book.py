from app.libs.httper import HttpReuquest
from flask import current_app

from app.spider.persistence import MySQLHelper


class ChangeBook:
    # 模型层 MVC层 M层
    isbn_url = "http://api.xiaomafeixiang.com/api/bookinfo?isbn={}"
    key_word_url = "http://api.xiaomafeixiang.com/api/bookinfo?q={}&count={}&start={}"

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        book_model = MySQLHelper.has_existed(isbn)
        if book_model:
            self.__fill_single(book_model)
        else:
            url = self.isbn_url.format(isbn)
            result = HttpReuquest.get(url)
            if result.get('status'):
                self.__fill_single(result)
                book_model = MySQLHelper.persistence_book(result)
                return book_model, 'from_mysql'

    def __fill_single(self, data):
        if data and isinstance(data, dict):
            self.total = 1
            self.books.append(data)
        else:
            self.total = 1
            self.books.append({'data':data.__dict__})

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, page=1):
        url = self.key_word_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HttpReuquest.get(url)
        self.__fill_collection(result)
        # return result

    def calculate_start(self, page):
        return (page-1)*current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0]['data'] if self.total >= 1 else None
