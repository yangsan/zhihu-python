# -*- coding: utf8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Dbuser(Base):
    """
    Table for zhihu users.
    """
    __tablename__ = "users"

    number = Column(Integer, primary_key=True)
    id = Column(String(50), unique=True)
    name = Column(String(50))

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)


class Dbanswer(Base):
    """
    Table for users' answers.
    """
    __tablename__ = "answers"

    id = Column(String(50), primary_key=True)
    upvote = Column(Integer)
    content = Column(String)
    user_id = Column(String(50), ForeignKey("users.id"))

    user = relationship("Dbuser", backref=backref("answers", order_by=id))

    def __repr__(self):
        return "<Answer(id=%s)>" % str(self.id)
