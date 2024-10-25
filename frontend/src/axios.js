import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL || 'http://localhost:5000/api', // Use environment variable or fallback to localhost
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export default apiClient;
