from sqlalchemy.orm import relationship

from app.models.base import Base, db
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from app.spider.change_book import ChangeBook


class Wish(Base):
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
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)
        ).all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        # 根据传入的一组isbn，到Wish表中计算出某个礼物
        # 的wish心愿数量
        # 一组数量
        # db.session
        # 条件表达式
        # mysql in
        # isbn对应的数量
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched == False,
                                                                             Gift.isbn.in_(isbn_list),
                                                                             Gift.status == 1).group_by(
            Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list
