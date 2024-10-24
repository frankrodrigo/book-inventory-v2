# backend/routes.py
from flask import jsonify, request, send_file
from app import app, db
from models import Book
import csv
import io


# Get all books (Read) or filter based on query parameters
@app.route('/api/books', methods=['GET'])
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')
    publication_date = request.args.get('publication_date')

    # Start with the query
    query = Book.query

    # Apply filters if parameters are provided
    if title:
        query = query.filter(Book.title.ilike(f'%{title}%'))
    if author:
        query = query.filter(Book.author.ilike(f'%{author}%'))
    if genre:
        query = query.filter(Book.genre.ilike(f'%{genre}%'))
    if publication_date:
        query = query.filter(Book.publication_date == publication_date)

    # Execute query and return results
    books = query.all()
    return jsonify([book.to_dict() for book in books]), 200


# Get a specific book by ID (Read)
@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify(book.to_dict()), 200

# Add a new book (Create)
@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        genre=data.get('genre'),
        isbn=data.get('isbn'),
        publication_date=data.get('publication_date')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully', 'book': new_book.to_dict()}), 201

# Update an existing book (Update)
@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)
    book.isbn = data.get('isbn', book.isbn)
    book.publication_date = data.get('publication_date', book.publication_date)
    
    db.session.commit()
    return jsonify({'message': 'Book updated successfully', 'book': book.to_dict()}), 200

# Delete a book (Delete)
@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 200

# Delete all books
@app.route('/api/books/delete-all', methods=['DELETE'])
def delete_all_books():
    try:
        num_rows_deleted = db.session.query(Book).delete()
        db.session.commit()
        return jsonify({'message': f'All books have been deleted. {num_rows_deleted} rows removed.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Export books in CSV or JSON
@app.route('/api/books/export/<string:format>', methods=['GET'])
def export_books(format):
    books = Book.query.all()
    
    if format == 'json':
        # Export as JSON
        return jsonify([book.to_dict() for book in books]), 200
    elif format == 'csv':
        # Export as CSV
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Title', 'Author', 'Genre', 'ISBN', 'Publication Date'])  # Header row
        for book in books:
            writer.writerow([book.title, book.author, book.genre, book.isbn, book.publication_date])
        output.seek(0)
        return send_file(
            io.BytesIO(output.getvalue().encode()), 
            mimetype='text/csv', 
            as_attachment=True, 
            download_name='books.csv'  # Corrected argument
        )
    else:
        return jsonify({'message': 'Unsupported format'}), 400