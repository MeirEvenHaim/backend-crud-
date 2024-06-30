from __main__ import app, db
from flask import Blueprint, request, jsonify
from models.books import Book 
# from datetime import datetime
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from werkzeug.exceptions import HTTPException
from format_respons import format_response




# Book CRUD routes
@app.route('/books', methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        new_book = Book(
            book_name=data['book_name'],
            author=data['author'],
            date_of_publish=data['date_of_publish'],
            series=data['series'],
            readers_age=data['readers_age'],
            img=data.get('img')
        )
        db.session.add(new_book)
        db.session.commit()
        return format_response(new_book.to_dict()), 201
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        return format_response([book.to_dict() for book in books])
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    try:
        book = Book.query.get(id)
        if book is None:
            return format_response(error='Book not found'), 404
        return format_response(book.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    try:
        data = request.get_json()
        book = Book.query.get(id)
        if book is None:
            return format_response(error='Book not found'), 404
        
        book.book_name = data.get('book_name', book.book_name)
        book.author = data.get('author', book.author)
        book.date_of_publish = data.get('date_of_publish', book.date_of_publish)
        book.series = data.get('series', book.series)
        book.readers_age = data.get('readers_age', book.readers_age)
        book.img = data.get('img', book.img)
        
        db.session.commit()
        return format_response(book.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    try:
        book = Book.query.get(id)
        if book is None:
            return format_response(error='Book not found'), 404
        db.session.delete(book)
        db.session.commit()
        return format_response(message='Book deleted successfully')
    except Exception as e:
        return format_response(error=str(e)), 400

