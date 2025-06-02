from flask import Blueprint, request, jsonify
from models import db, Book

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': b.id, 'title': b.title, 'author': b.author} for b in books])

@book_routes.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added'}), 201

@book_routes.route('/test')
def test():
    return {"message": "Hello from Flask"}
