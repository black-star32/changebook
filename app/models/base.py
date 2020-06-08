from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import SmallInteger, Column, Integer

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_time = Column('crate_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attr(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != id:
                setattr(self, key, value)
