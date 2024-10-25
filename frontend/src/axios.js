import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL || 'https://flask-backend-656844231878.us-central1.run.app/api/',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export default apiClient;
