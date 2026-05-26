// Core CAOS types matching backend schemas exactly

export type MemoryCategory =
  | 'identity'
  | 'projects'
  | 'governance'
  | 'preferences'
  | 'relationship'
  | 'domains'
  | 'tech_state'
  | 'behavioral'
  | 'traits'
  | 'learning'
  | 'real_world'
  | 'risk'
  | 'counter'
  | 'unclassified';

export type MemoryStatus = 'active' | 'pending_confirmation' | 'forgotten' | 'superseded';

export type MemorySourceType =
  | 'explicit_user_statement'
  | 'conversation_inference'
  | 'system_event'
  | 'imported_legacy'
  | 'admin_entry';

export interface MemoryEvidence {
  source_type: MemorySourceType;
  source_ref?: string;
  quote?: string;
  captured_at: string;
}

export interface MemoryAtom {
  memory_id: string;
  user_id: string;
  category: MemoryCategory;
  content: string;
  status: MemoryStatus;
  confidence: number;
  priority: number;
  evidence: MemoryEvidence[];
  metadata: Record<string, unknown>;
  created_at: string;
  updated_at: string;
}

export interface ChatMessage {
  role: 'user' | 'assistant' | 'system' | 'tool';
  content: string;
  latency_ms?: number;
}

export interface ChatReceipt {
  userTokens: number;
  assistantTokens: number;
  threadTotalTokens: number;
  latencyMs: number;
}

export interface Thread {
  thread_id: string;
  title: string;
  created_at: string;
  updated_at: string;
  message_count: number;
  messages: ChatMessage[];
}

export interface ModelContextSpec {
  provider: string;
  model: string;
  display_name: string;
  context_window_tokens: number;
  usable_context_tokens: number;
  reserved_output_tokens: number;
  reserved_system_tokens: number;
  wcw_policy: string;
  enabled: boolean;
}

export interface ModelSelection {
  active_model: ModelContextSpec;
  available_models: ModelContextSpec[];
}

export interface DiagnosticReceipt {
  status: string;
  phase: string;
  detail: string;
}

export interface ApiEnvelope<T = unknown> {
  ok: boolean;
  data?: T;
  error_code?: string;
  message?: string;
  diagnostic_receipt?: DiagnosticReceipt;
}

export interface RuntimeState {
  runtime: Record<string, unknown>;
  database: Record<string, unknown>;
}

export type SidebarView = 'threads' | 'memory' | 'settings' | 'admin' | 'artifacts';
