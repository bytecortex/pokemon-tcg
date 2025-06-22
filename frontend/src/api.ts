import axios from 'axios';
import { useUserStore } from '@/server/userStore';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

api.interceptors.request.use((config) => {
  const userStore = useUserStore();
  if (userStore.token) {
    config.headers = config.headers ?? {};
    config.headers.Authorization = `Bearer ${userStore.token}`;
  }
  return config;
});

export default api;
