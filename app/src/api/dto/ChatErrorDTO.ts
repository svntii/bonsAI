interface ErrorDetail {
  type: string;
  loc: string[];
  msg: string;
  input: string | null;
  url: string;
}

export interface ChatErrorDTO {
  detail: ErrorDetail;
}
