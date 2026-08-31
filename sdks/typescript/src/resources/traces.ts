import { ChatCompletionRequest, ChatCompletionResponse } from '../types';

export class EnterpriseResourceClient {
  private apiKey: string;
  private baseUrl: string;

  constructor(apiKey: string, baseUrl: string) {
    this.apiKey = apiKey;
    this.baseUrl = baseUrl;
  }

  async execute(path: string, payload: Record<string, any>): Promise<any> {
    const res = await fetch(`${this.baseUrl}${path}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': this.apiKey,
      },
      body: JSON.stringify(payload),
    });
    if (!res.ok) {
      throw new Error(`Atlas Resource Client error: ${res.statusText}`);
    }
    return res.json();
  }

  async list(path: string, params?: Record<string, any>): Promise<any[]> {
    const query = new URLSearchParams(params).toString();
    const url = query ? `${this.baseUrl}${path}?${query}` : `${this.baseUrl}${path}`;
    const res = await fetch(url, {
      headers: { 'X-API-Key': this.apiKey },
    });
    if (!res.ok) throw new Error(`Atlas List error: ${res.statusText}`);
    return res.json();
  }
}
