export interface ChatResponseDTO {
  id: number;
  responseText: string;
  userResponseSuggestions: string[];
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
