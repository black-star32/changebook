from app.libs.httper import HttpReuquest
from flask import current_app


class ChangeBook:
    # 模型层 MVC层 M层
    isbn_url = "http://api.xiaomafeixiang.com/api/bookinfo?isbn={}"
    key_word_url = "http://api.xiaomafeixiang.com/api/bookinfo?q={}&count={}&start={}"

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HttpReuquest.get(url)
        self.__fill_single(result)
        # dic
        # return result

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

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
