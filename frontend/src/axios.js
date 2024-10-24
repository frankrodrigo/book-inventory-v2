import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://192.168.6.139:5000/api', // Flask API base URL
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export default apiClient;
