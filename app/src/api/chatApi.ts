import axiosInstance from '@utils/axiosInstance';
import {
  ChatRequestDTO,
  ChatResponseDTO,
  VectorAddRequestDTO,
  VectorAddResponseDTO,
} from '@api/dto/ChatDTO';

// Endpoints
// POST /chat/{id}
// POST /chat/
// POST /vectorstore/add

const chatApi = {
  postChatMessage: async (
    request: ChatRequestDTO,
  ): Promise<ChatResponseDTO> => {
    const r = {
      prompt: request.prompt,
    };

    try {
      const response = await axiosInstance.post(`/chat/${request.id}`, r);
      const chatResponse: ChatResponseDTO = {
        response: response.data.response,
        sources: response.data.sources,
        suggestedResponses: response.data.suggested_responses,
      };
      return chatResponse;
    } catch (error) {
      throw error;
    }
  },
  // postVectorAdd: async (request: VectorAddRequestDTO): Promise<void> => {
  //   try {
  //     const response = await axiosInstance.post(
  //       '/vectorstore/add',
  //       request.vectors,
  //     );
  //     const vectorAddResponse: VectorAddResponseDTO = {
  //       message: response.data.message,
  //     };
  //   } catch (error) {
  //     throw error;
  //   }
  //   // verify that the request was successful
  // },
};

export default chatApi;
