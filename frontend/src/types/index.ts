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

export type SidebarView = 'threads' | 'memory' | 'settings' | 'admin' | 'artifacts' | 'agent_playground';

export type AgentJobStatus = 'pending' | 'planned' | 'blocked' | 'completed' | 'failed';

export interface AgentToolScope {
  allowed_tools: string[];
  forbidden_tools: string[];
}

export interface AgentLimits {
  max_runtime_seconds: number;
  max_tool_calls: number;
  max_tokens: number;
  max_spawned_agents: number;
}

export interface AgentJobPacket {
  job_id: string;
  project_id: string;
  agent_role: string;
  task_summary: string;
  read_scope: string[];
  write_scope: string[];
  network_scope: string[];
  connector_scope: string[];
  memory_bins_available: string[];
  secret_access_allowed: boolean;
  tools: AgentToolScope;
  limits: AgentLimits;
  approval_required_for: string[];
  stop_conditions: string[];
  status: AgentJobStatus;
  created_at: string;
  updated_at: string;
}

export interface AgentJobResponse {
  job?: AgentJobPacket | null;
  jobs?: AgentJobPacket[];
  receipt: Record<string, unknown>;
}
