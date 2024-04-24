import axios, { AxiosInstance } from 'axios';

const backendUrl = process.env.URL;
const backendPort = process.env.PORT;

if (!backendUrl || !backendPort) {
  throw new Error('Backend URL or port not defined');
}

const baseURL = `${backendUrl}:${backendPort}`;

const axiosInstance: AxiosInstance = axios.create({
  baseURL,
  timeout: 10000, // 10 seconds
  headers: {
    'Content-Type': 'application/json', 
  },
});

export default axiosInstance;