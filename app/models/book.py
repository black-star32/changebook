from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, doc='标题')
    author = Column('author', String(30), default='未名', doc='作者')
    binding = Column(String(20), doc='装帧')
    publisher = Column(String(50), doc='出版社')
    price = Column(String(20), doc='价格')
    pages = Column(Integer, doc='页数')
    pubdate = Column(String(20), doc='出版日期')
    isbn = Column(String(15), nullable=False, unique=True, doc='isbn编号')
    summary = Column(String(1000), doc='简介')
    image = Column(String(100), doc='图片')

    # MVC M Model 只有数据 = 数据表  Model不只有数据，还有业务逻辑操作数据
    # ORM 对象关系映射 Code First

    def sample(self):
        pass
