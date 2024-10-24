<template>
  <div class="export-wrapper">
    <div class="export-container">
      <h2>Export Book Data</h2>
      <p>Select the format in which you want to export your book inventory.</p>

      <div class="button-container">
        <!-- CSV Export Button -->
        <button class="btn-link" @click="exportBooks('csv')">Export CSV</button>

        <!-- JSON Export Button -->
        <button class="btn-link" @click="exportBooks('json')">Export JSON</button>
      </div>

      <router-link to="/" class="btn-link back-btn">Back</router-link>
    </div>
  </div>
</template>

<script>
import BookService from '@/services/BookService';

export default {
  methods: {
    exportBooks(format) {
      BookService.exportBooks(format)
        .then(response => {
          let blob;
          if (format === 'json') {
            // Correctly convert JSON data to a string
            blob = new Blob([JSON.stringify(response.data, null, 2)], { type: 'application/json' });
          } else {
            // Assume CSV data is correctly formatted
            blob = new Blob([response.data], { type: 'text/csv' });
          }
          const url = window.URL.createObjectURL(blob);
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `books.${format}`);
          document.body.appendChild(link);
          link.click();
          link.remove();
        })
        .catch(error => {
          console.error("Error exporting books:", error);
        });
    },
  }
}

</script>

<style scoped>
.export-wrapper {
  display: flex;
  justify-content: center;  
  align-items: center;      
  width: 100vw;
  height: 100vh;            
  background: linear-gradient(180deg, #E0F2E9, white);
  margin: 0;
  padding: 0;
}

.export-container {
  background-color: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
  text-align: center;
  box-sizing: border-box;
}

.export-container h2 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 10px;
}

.export-container p {
  font-size: 14px;
  margin-bottom: 20px;
  color: #555;
}

.button-container {
  display: flex;
  flex-direction: column;
  gap: 20px; /* Increased gap for better spacing */
}

.btn-link {
  padding: 15px 0;
  background-color: #4CAF50;
  color: white;
  border-radius: 6px;
  text-align: center;
  text-decoration: none;
  font-size: 18px;
  font-weight: 600;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  display: inline-block;
  width: 100%;
}

.btn-link:hover {
  background-color: #45a049;
  transform: translateY(-2px);
}

.back-btn {
  background-color: #333;
  color: white;
  padding: 15px 0;
  margin-top: 20px;
}

.back-btn:hover {
  background-color: #444;
}
</style>
