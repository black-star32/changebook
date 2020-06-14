from change import app
import time

from app.libs.httper import HttpReuquest
from app.spider.persistence import MySQLHelper


class BookSpider:
    # 模型层 MVC层 M层
    isbn_url = "http://api.xiaomafeixiang.com/api/bookinfo?isbn={}"

    def search_and_save_books(self, isbn):
        book_model = MySQLHelper.has_existed(isbn)
        if not book_model:
            url = self.isbn_url.format(isbn)
            result = HttpReuquest.get(url)
            print(isbn, result.get('status'))
            if result.get('status'):
                book_model = MySQLHelper.persistence_book(result)
                return book_model, 'from_mysql'


if __name__ == '__main__':
    with app.app_context():
        for i in range(9787000002994, 9787999999999):
            BookSpider().search_and_save_books(i)
            time.sleep(0.1)
