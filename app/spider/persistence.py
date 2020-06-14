from app import db
from app.libs.helper import get_isbn
from app.models.book import Book


class MySQLHelper:
    @classmethod
    def has_existed(cls, isbn):
        book = Book.query.filter(Book.isbn==isbn).first()
        if book:
            return book
        else:
            return None

    @classmethod
    def persistence_book(cls, book):
        book_model = Book()
        book_model.set_attr(book['data'])

        # book_model.isbn = get_isbn(book['data'])
        # book_model.image = book['images']['large']
        db.session.add(book_model)
        db.session.commit()
        return book_model

