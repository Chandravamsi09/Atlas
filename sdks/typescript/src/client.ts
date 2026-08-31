import { ChatCompletionRequest, ChatCompletionResponse } from './types';

export class AtlasClient {
  private apiKey: string;
  private baseUrl: string;

  constructor(config: { apiKey: string; baseUrl?: string }) {
    this.apiKey = config.apiKey;
    this.baseUrl = config.baseUrl || 'http://localhost:8000/api/v1';
  }

  async chatComplete(request: ChatCompletionRequest): Promise<ChatCompletionResponse> {
    const response = await fetch(`${this.baseUrl}/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': this.apiKey,
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      throw new Error(`Atlas API error (${response.status}): ${await response.text()}`);
    }

    return response.json();
  }
}
