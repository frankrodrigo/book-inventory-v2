<template>
  <div class="index-wrapper">
    <div class="index-container">
      <h2>Welcome to SB Book Inventory</h2>
      <p>Manage your book collection easily. Use the options below to navigate the system.</p>

      <!-- Navigation buttons only -->
      <div class="button-container">
        <router-link to="/add" class="btn-link">Add New Book</router-link>
        <router-link to="/filter" class="btn-link">Filter Books</router-link>
        <router-link to="/export" class="btn-link">Export Data</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.index-wrapper {
  display: flex;
  justify-content: center;  /* Centers horizontally */
  align-items: center;      /* Centers vertically */
  width: 100vw;
  height: 100vh;            /* Full viewport height */
  background: linear-gradient(180deg, #E0F2E9, white); /* Ensures the background covers the full view */
  margin: 0; /* Removes default margin */
  padding: 0; /* Removes default padding */
}

.index-container {
  background-color: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
  text-align: center;
  box-sizing: border-box;
}

.index-container h2 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 10px;
}

.index-container p {
  font-size: 14px;
  margin-bottom: 20px;
  color: #555;
}

.button-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
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
  transition: background-color 0.3s ease, transform 0.2s ease;
  display: inline-block;
  width: 100%;
}

.btn-link:hover {
  background-color: #45a049;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .index-container {
    padding: 20px;
    width: 90%;
  }
}
</style>
