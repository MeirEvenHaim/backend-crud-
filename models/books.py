from __main__ import app, db

# from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
from datetime import datetime




class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(25), unique=True, nullable=True)
    author = db.Column(db.String(120), unique=False, nullable=False)
    date_of_publish = db.Column(db.Integer, unique=False, nullable=False)
    series = db.Column(db.String(120), unique=False, nullable=False)
    readers_age = db.Column(db.Integer, unique=False, nullable=False)
    img = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return f"<Book(id={self.id}, author='{self.author}', series='{self.series}', img='{self.img}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'author': self.author,
            'date_of_publish': self.date_of_publish,
            'series': self.series,
            'readers_age': self.readers_age,
            'img': self.img
        }
