export interface ChatResponseDTO {
  completion: string;
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
