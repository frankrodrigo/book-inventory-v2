import apiClient from '../axios';

export default {
  // Get all books or filter based on criteria
  getBooks(filters = {}) {
    const params = {};
    // If any filters are provided, add them as query parameters
    if (filters.title) params.title = filters.title;
    if (filters.author) params.author = filters.author;
    if (filters.genre) params.genre = filters.genre;
    if (filters.publication_date) params.publication_date = filters.publication_date;

    return apiClient.get('/books', { params }); // Pass query parameters to the API
  },

  // Add a new book
  addBook(book) {
    return apiClient.post('/books', book);
  },

  // Get a single book by ID
  getBook(id) {
    return apiClient.get(`/books/${id}`);
  },

  // Update a book
  updateBook(id, book) {
    return apiClient.put(`/books/${id}`, book);
  },

  // Delete a book
  deleteBook(id) {
    return apiClient.delete(`/books/${id}`);
  },

  // Export books (CSV, JSON, etc.)
  exportBooks(format) {
    return apiClient.get(`/books/export/${format}`);
  },
};
