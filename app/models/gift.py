from flask import current_app
from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc

from app.spider.change_book import ChangeBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        change_book = ChangeBook()
        change_book.search_by_isbn(self.isbn)
        return change_book.first

    @classmethod
    def recent(cls):
        # 链式调用
        # 主体 Query
        # 子函数
        # first all
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_PER_PAGE']).distinct().all()

        return recent_gift
