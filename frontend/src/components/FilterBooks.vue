<template>
  <div class="filter-books-container">
    <form @submit.prevent="filterBooks">
      <h2>Filter Books</h2>
      <p>Enter the criteria below to filter the book inventory.</p>

      <div class="form-row">
        <div class="form-group">
          <label for="title">Title</label>
          <input type="text" v-model="filters.title" />
        </div>
        <div class="form-group">
          <label for="author">Author</label>
          <input type="text" v-model="filters.author" />
        </div>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="genre">Genre</label>
          <input type="text" v-model="filters.genre" />
        </div>
        <div class="form-group">
          <label for="publication_date">Publication Date</label>
          <input type="date" v-model="filters.publication_date" />
        </div>
      </div>

      <div class="form-actions">
        <router-link to="/" class="back-btn">Back</router-link>
        <button class="next-btn">Filter Books</button>
      </div>
    </form>
  </div>
</template>

<script>
import BookService from "../services/BookService";

export default {
  data() {
    return {
      filters: {
        title: "",
        author: "",
        genre: "",
        publication_date: "",
      },
      filteredBooks: [], // To store the filtered books
    };
  },
  methods: {
    async filterBooks() {
  try {
    const response = await BookService.getBooks(this.filters);
    console.log("Filtered books response:", response.data);
    this.filteredBooks = response.data;
    console.log("Books before navigating:", this.filteredBooks);

    // Pass the filtered books via the router's query
    this.$router.push({
      name: 'EditBooks',
      query: { books: JSON.stringify(this.filteredBooks) } // Convert array to string
    });
  } catch (error) {
    console.error("Error filtering books:", error);
  }
}
,
  },
};
</script>



<style scoped>
.filter-books-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  padding: 20px;
  background: linear-gradient(180deg, #E0F2E9, white);
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
  .form-row {
    flex-direction: column;
  }

  .form-group {
    width: 100%;
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