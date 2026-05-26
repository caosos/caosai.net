import { ApiEnvelope } from '../types';

const BASE = process.env.REACT_APP_API_URL || '/api';

async function request<T>(
  method: string,
  path: string,
  body?: unknown
): Promise<ApiEnvelope<T>> {
  const res = await fetch(`${BASE}${path}`, {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: body ? JSON.stringify(body) : undefined,
  });
  return res.json();
}

export const api = {
  health: () => request<{ ok: boolean }>('GET', '/health'),

  runtime: () => request<unknown>('GET', '/runtime'),

  models: {
    list: () => request<unknown>('GET', '/models'),
    select: (provider: string, model: string) =>
      request<unknown>('POST', '/models/select', { provider, model }),
  },

  chat: {
    turn: (params: {
      message: string;
      thread_id?: string;
      session_id?: string;
      user_id?: string;
      provider?: string;
      model?: string;
    }) => request<unknown>('POST', '/chat/turn', params),
  },

  memory: {
    list: (user_id: string, category?: string) =>
      request<unknown>('POST', '/memory/atoms/query', {
        user_id,
        category: category || null,
        limit: 200,
      }),
    create: (params: {
      user_id: string;
      content: string;
      category?: string;
      source_type?: string;
    }) => request<unknown>('POST', '/memory/atoms', params),
  },

  threads: {
    list: (user_id: string) =>
      request<unknown>('POST', '/threads/list', { user_id, limit: 50 }),
    messages: (thread_id: string, user_id: string = 'dev_user') =>
      request<unknown>('GET', `/threads/${thread_id}/messages?user_id=${user_id}`),
  },

  auth: {
    devLogin: (user_id: string, is_admin?: boolean) =>
      request<unknown>('POST', '/auth/dev-login', { user_id, is_admin }),
  },

  admin: {
    probe: (user_id: string, is_admin: boolean) =>
      request<unknown>('POST', '/admin/probe', { user_id, is_admin }),
  },
};
