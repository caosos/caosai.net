import React, { useEffect, useState } from 'react';
import { api } from '../../api/client';
import { AgentJobPacket } from '../../types';

interface ReceiptSummary { receipt_id?: string; event_type?: string; status?: string; }

export default function AgentPlayground() {
  const [jobs, setJobs] = useState<AgentJobPacket[]>([]);
  const [loading, setLoading] = useState(false);
  const [receipt, setReceipt] = useState<ReceiptSummary | null>(null);

  const loadJobs = async () => {
    setLoading(true);
    const res = await api.agentJobs.list();
    setJobs(res.data?.jobs || []);
    setReceipt((res.data?.receipt as ReceiptSummary) || null);
    setLoading(false);
  };
  useEffect(() => { loadJobs(); }, []);

  const createSampleJob = async () => {
    setLoading(true);
    const res = await api.agentJobs.create({
      project_id: 'caos-playground-v0', agent_role: 'planner',
      task_summary: 'Inspect repository docs and propose bounded implementation plan only.',
      read_scope: ['docs/*', 'backend/app/*', 'frontend/src/*'], write_scope: [], network_scope: [], connector_scope: [],
      memory_bins_available: ['projects', 'governance'], secret_access_allowed: false,
      tools: { allowed_tools: ['read_file', 'list_files'], forbidden_tools: ['shell_execute', 'deploy', 'write_repo', 'spawn_agent'] },
      limits: { max_runtime_seconds: 300, max_tool_calls: 10, max_tokens: 4000, max_spawned_agents: 0 },
      approval_required_for: ['any_write_action', 'connector_write', 'deployment'], stop_conditions: ['scope_complete', 'attempted_forbidden_action'], status: 'pending',
    });
    setReceipt((res.data?.receipt as ReceiptSummary) || null);
    await loadJobs();
  };

  return <div style={{ padding: '68px 24px 120px', overflowY: 'auto', height: '100%' }}>
    <div className="glass" style={{ padding: 16, marginBottom: 14 }}>
      <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--caos-accent-bright)' }}>Read-only playground — no autonomous execution</div>
    </div>
    <div className="glass" style={{ padding: 16, marginBottom: 14 }}>
      <button onClick={createSampleJob} disabled={loading}>Create Sample Read-only Job Packet</button>
      {receipt && <div style={{ marginTop: 10, fontSize: 12, color: 'var(--caos-text-dim)' }}>Receipt: {receipt.event_type} · {receipt.status} · {receipt.receipt_id}</div>}
    </div>
    <div className="glass" style={{ padding: 16 }}>
      <div style={{ fontSize: 13, fontWeight: 600, marginBottom: 10 }}>Agent Jobs</div>
      {loading && <div style={{ fontSize: 12 }}>Loading…</div>}
      {!loading && jobs.length === 0 && <div style={{ fontSize: 12 }}>No jobs created yet.</div>}
      {jobs.map((job) => <div key={job.job_id} style={{ borderTop: '1px solid var(--caos-border)', paddingTop: 10, marginTop: 10 }}>
        <div style={{ fontSize: 12 }}><b>project_id:</b> {job.project_id}</div>
        <div style={{ fontSize: 12 }}><b>job_id:</b> {job.job_id}</div>
        <div style={{ fontSize: 12 }}><b>agent_role:</b> {job.agent_role}</div>
        <div style={{ fontSize: 12 }}><b>task_summary:</b> {job.task_summary}</div>
        <div style={{ fontSize: 12 }}><b>allowed_tools:</b> {job.tools.allowed_tools.join(', ') || '(none)'}</div>
        <div style={{ fontSize: 12 }}><b>forbidden_tools:</b> {job.tools.forbidden_tools.join(', ') || '(none)'}</div>
        <div style={{ fontSize: 12 }}><b>max_tool_calls:</b> {job.limits.max_tool_calls}</div>
        <div style={{ fontSize: 12 }}><b>max_tokens:</b> {job.limits.max_tokens}</div>
        <div style={{ fontSize: 12 }}><b>max_spawned_agents:</b> {job.limits.max_spawned_agents}</div>
        <div style={{ fontSize: 12 }}><b>stop_conditions:</b> {job.stop_conditions.join(', ') || '(none)'}</div>
        <div style={{ fontSize: 12 }}><b>status:</b> {job.status}</div>
      </div>)}
    </div>
  </div>;
}
