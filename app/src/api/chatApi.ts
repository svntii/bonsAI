import axiosInstance from '../utils/axiosInstance';

const chatApi = {
  postChatMessage: async (id: string, message: string): Promise<any> => {
    try {
      const response = await axiosInstance.post(`/chat/${id}`, { prompt: message });
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default chatApi;
