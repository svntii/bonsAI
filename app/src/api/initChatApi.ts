import axiosInstance from '../utils/axiosInstance';

const initChatApi = {
  postChatMessage: async (message: string): Promise<any> => {
    try {
      const response = await axiosInstance.post('/chat', { prompt: message });
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default initChatApi;
