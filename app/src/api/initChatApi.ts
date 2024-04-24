import axiosInstance from '@utils/axiosInstance';
import { initChatResponseDTO } from './dto/ChatDTO';

const initChatApi = {
  postChatMessage: async (message: string): Promise<any> => {
    try {
      const response = await axiosInstance.post('/chat', {prompt: message});
      const chatResponse : initChatResponseDTO = {
        id: response.data.id,
        response: response.data.response,
        suggestedResponses: response.data.suggested_responses,
      };
      return chatResponse;
    } catch (error) {
      throw error;
    }
  },
};

export default initChatApi;
