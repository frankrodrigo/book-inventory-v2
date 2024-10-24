<template>
  <div class="edit-books-container">
    <h2>Filtered Books</h2>

    <!-- Back button to FilterBooks page -->
    <router-link to="/filter" class="back-btn">Back</router-link>

    <!-- Responsive table container -->
    <div class="table-responsive">
      <table class="results-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Genre</th>
            <th>ISBN</th>
            <th>Publication Date</th>
            <th>Edit</th>
            <th>Delete</th>
          </tr>
        </thead>

        <tbody>
          <tr v-if="!localBooks.length">
            <td colspan="7">No books found.</td>
          </tr>
          <tr v-for="book in localBooks" :key="book.id">
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.genre }}</td>
            <td>{{ book.isbn }}</td>
            <td>{{ book.publication_date }}</td>
            <td><button @click="editBook(book)">Edit</button></td>
            <td><button @click="deleteBook(book.id)">Delete</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import BookService from "../services/BookService"; // Ensure BookService exists for backend communication

export default {
  data() {
    return {
      localBooks: [], // Create a local copy of books for editing/deleting
    };
  },
  created() {
    // Parse the books array from the query string
    if (this.$route.query.books) {
      this.localBooks = JSON.parse(this.$route.query.books);
    }
    console.log("Books passed to EditBooks:", this.localBooks); // Check if books are passed correctly
  },
  methods: {
        editBook(book) {
          console.log("Editing book with ID:", book.id); // This should log the id
          if (book && book.id) {
            this.$router.push({ name: 'EditBook', params: { id: book.id } });
          } else {
            console.error('Book ID is missing');
          }
        },
        deleteBook(bookId) {
          if (confirm('Are you sure you want to delete this book?')) {
            this.performDelete(bookId);
          }
        },
        async performDelete(bookId) {
          try {
            await BookService.deleteBook(bookId);
            this.localBooks = this.localBooks.filter(book => book.id !== bookId);
            console.log("Book with ID " + bookId + " deleted from DB");
            alert('Book deleted successfully');
          } catch (error) {
            console.error("Error deleting book:", error);
            alert('Failed to delete book');
          }
        }
      },
};

</script>

<style scoped>
/* General page and container adjustments */
body, .edit-books-container {
  background: linear-gradient(180deg, #E0F2E9, white); 
  font-family: 'Poppins', sans-serif;
  margin: 0;
  padding: 0;
}

.edit-books-container {
  padding: 20px;  /* Reduced padding */
  margin: auto;   /* Center alignment */
  width: 100%;    /* Full width to use the available space */
  box-sizing: border-box; /* Include padding and border in the element's total width and height */
}

/* Back button styling */
.back-btn {
  display: block; /* Ensures the button is on a new line */
  width: fit-content; /* Adjust width to the content */
  margin-bottom: 15px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  font-weight: bold;
  border-radius: 6px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.back-btn:hover {
  background-color: #45a049;
}

/* Table styling for responsiveness */
.table-responsive {
  overflow-x: auto; /* Enable horizontal scrolling */
}

.results-table {
  width: 100%; /* Full width to stretch across the container */
  min-width: 600px; /* Minimum width for better table structure */
  border-collapse: collapse; /* Eliminate space between borders */
}

.results-table th,
.results-table td {
  padding: 10px 15px; /* Sufficient padding for content */
  border: 1px solid #ddd; /* Light borders for differentiation */
  text-align: left; /* Align text to the left */
}

.results-table th {
  background-color: #f4f4f4; /* Light gray background for headers */
  font-weight: bold;
}

.results-table tr:nth-child(even) {
  background-color: #f9f9f9; /* Zebra striping for rows */
}

button {
  padding: 6px 12px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer; /* Pointer on hover for better user indication */
}

button:hover {
  background-color: #45a049;
}

/* Adjustments for smaller screens */
@media screen and (max-width: 768px) {
  .results-table th, .results-table td {
    padding: 8px; /* Smaller padding on mobile */
  }

  .results-table {
    font-size: 14px; /* Smaller font size for better readability */
  }

  .edit-books-container {
    padding: 10px; /* Reduced padding on smaller screens */
  }
}
</style>
