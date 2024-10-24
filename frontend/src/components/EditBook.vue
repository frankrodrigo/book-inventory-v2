<template>
  <div class="edit-book-container">
    <form @submit.prevent="updateBook">
      <h2>Edit Book</h2>
      <p>Update the details below to modify the book in the inventory.</p>

      <div class="form-row">
        <div class="form-group">
          <label for="title">Title</label>
          <input type="text" v-model="book.title" required />
        </div>
        <div class="form-group">
          <label for="author">Author</label>
          <input type="text" v-model="book.author" required />
        </div>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="genre">Genre</label>
          <input type="text" v-model="book.genre" />
        </div>
        <div class="form-group">
          <label for="isbn">ISBN</label>
          <input type="text" v-model="book.isbn" />
        </div>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="publication_date">Publication Date</label>
          <input type="date" v-model="book.publication_date" />
        </div>
      </div>

      <div class="form-actions">
        <router-link to="/filter" class="back-btn">Back</router-link>
        <button type="submit" class="next-btn">Update Book</button>
      </div>
    </form>
  </div>
</template>

<script>
import BookService from "../services/BookService";

export default {
  data() {
    return {
      book: {}, // Initial book object
    };
  },
  created() {
    this.fetchBookDetails();
  },
  methods: {
    fetchBookDetails() {
      const id = this.$route.params.id;
      BookService.getBook(id).then(response => {
        this.book = response.data;
      });
    },
    updateBook() {
      const id = this.$route.params.id;
      BookService.updateBook(id, this.book)
        .then(() => {
          alert("Book updated successfully");
          this.$router.push("/filter"); // Correct redirection after update
        })
        .catch(error => {
          console.error("Error updating book:", error);
        });
    },
  },
};
</script>

<style scoped>
.edit-book-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-width: 600px; /* Match AddBook style */
  min-height: 100vh;
  box-sizing: border-box;
  padding: 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
  margin: auto;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

input[type="text"],
input[type="date"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.form-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.back-btn,
.next-btn {
  padding: 15px 0;
  font-size: 18px;
  border-radius: 6px;
  text-align: center;
  text-decoration: none;
  font-weight: 600;
  width: 48%;
  color: white;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.next-btn {
  background-color: #4CAF50;
}

.next-btn:hover {
  background-color: #45a049;
}

.back-btn {
  background-color: #333;
}

.back-btn:hover {
  background-color: #444;
}

@media (max-width: 768px) {
  .form-actions {
    flex-direction: column;
    gap: 10px;
  }

  .back-btn,
  .next-btn {
    width: 100%;
  }
}
</style>
