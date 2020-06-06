from app.libs.http_request import HttpReuquest
from flask import current_app


class ChangeBook:
    # 模型层 MVC层 M层
    isbn_url = "http://api.xiaomafeixiang.com/api/bookinfo?isbn={}"
    key_word_url = "http://api.xiaomafeixiang.com/api/bookinfo?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HttpReuquest.get(url)
        # dic
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.key_word_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HttpReuquest.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1)*current_app.config['PER_PAGE']
