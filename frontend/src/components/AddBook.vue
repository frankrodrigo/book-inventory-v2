<template>
  <div class="add-book-container">
    <form @submit.prevent="submitBook">
      <h2>Add New Book</h2>
      <p>Fill in the details below to add a book to the inventory.</p>

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
        <router-link to="/" class="back-btn">Back</router-link>
        <button type="submit" class="next-btn">Add Book</button>
      </div>
    </form>
  </div>
</template>

<script>
import BookService from "../services/BookService";

export default {
  data() {
    return {
      book: {
        title: "",
        author: "",
        genre: "",
        isbn: "",
        publication_date: "",
      },
    };
  },
  methods: {
    submitBook() {
      BookService.addBook(this.book)
        .then(() => {
          alert("Book added successfully");
          this.$router.push("/");
        })
        .catch((error) => {
          console.error("Error adding book:", error);
        });
    },
  },
};
</script>

<style scoped>
/* Keep the green gradient background for all pages */
body {
  background: linear-gradient(180deg, #E0F2E9, white);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
}

/* Ensure the container is vertically centered */
.add-book-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  padding: 20px;
}

.container {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  width: 100%;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

input[type="text"],
input[type="date"] {
  width: calc(100% - 20px); /* Adds padding to ensure it's not touching the right edge */
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  margin-right: auto; /* Keeps input fields from touching the right edge */
}

/* Button styles */
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

/* Responsive adjustments */
@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
  }

  .form-group {
    width: 100%;
  }

  .container {
    width: 90%;
    padding: 20px;
    margin-top: 10px; /* Reduce the top margin to bring the content closer to the top */
  }

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
