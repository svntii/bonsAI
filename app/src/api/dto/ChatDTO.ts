export interface initChatResponseDTO {
  id: string;
  response: string;
  suggestedResponses: string[];
}

export interface ChatResponseDTO {
  response: string;
  sources: string[];
  suggestedResponses: string[];
}

export interface ChatRequestDTO {
  id: string;
  prompt: string;
}

export interface VectorAddRequestDTO {
  vectors: string[];
}

export interface VectorAddResponseDTO {
  message: string;
}
