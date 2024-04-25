import axios, {AxiosInstance} from 'axios';

const backendUrl = '127.0.0.1';
const backendPort = '8000';

const baseURL = `http://${backendUrl}:${backendPort}`;

const axiosInstance: AxiosInstance = axios.create({
  baseURL,
  timeout: 20000, // 10 seconds
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;
