from flask import Flask
from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<User %r>' % (self.name)


class Entries(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    title = Column('title', String(80), unique=True, nullable=False)
    text = Column('text', String(255), nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Entry %r>' % self.title