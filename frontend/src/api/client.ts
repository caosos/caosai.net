import { AgentJobPacket, ApiEnvelope } from '../types';

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

  auth: {
    devLogin: (user_id: string, is_admin?: boolean) =>
      request<unknown>('POST', '/auth/dev-login', { user_id, is_admin }),
  },

  admin: {
    probe: (user_id: string, is_admin: boolean) =>
      request<unknown>('POST', '/admin/probe', { user_id, is_admin }),
  },


  agentJobs: {
    create: (params: {
      project_id: string;
      agent_role: string;
      task_summary: string;
      read_scope?: string[];
      write_scope?: string[];
      network_scope?: string[];
      connector_scope?: string[];
      memory_bins_available?: string[];
      secret_access_allowed?: boolean;
      tools?: { allowed_tools: string[]; forbidden_tools: string[] };
      limits?: {
        max_runtime_seconds: number;
        max_tool_calls: number;
        max_tokens: number;
        max_spawned_agents: number;
      };
      approval_required_for?: string[];
      stop_conditions?: string[];
      status?: 'pending' | 'planned' | 'blocked' | 'completed' | 'failed';
    }) => request<{ job: AgentJobPacket; receipt: Record<string, unknown> }>('POST', '/agent-jobs', params),
    list: () => request<{ jobs: AgentJobPacket[]; receipt: Record<string, unknown> }>('GET', '/agent-jobs'),
    get: (jobId: string) => request<{ job: AgentJobPacket | null; receipt: Record<string, unknown> }>('GET', `/agent-jobs/${jobId}`),
  },
};
