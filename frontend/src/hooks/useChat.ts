import { useState, useCallback, useEffect } from 'react';
import { ChatMessage, ChatReceipt, Thread } from '../types';
import { api } from '../api/client';

const USER_ID = 'dev_user';

function makeThread(id: string, title: string = ''): Thread {
  return {
    thread_id: id,
    title,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
    message_count: 0,
    messages: [],
  };
}

export function useChat() {
  const [threads, setThreads] = useState<Thread[]>([]);
  const [activeThreadId, setActiveThreadId] = useState<string | undefined>();
  const [loading, setLoading] = useState(false);
  const [lastLatencyMs, setLastLatencyMs] = useState<number | undefined>();
  const [totalTokens, setTotalTokens] = useState(0);
  const [lastReceipt, setLastReceipt] = useState<ChatReceipt | undefined>();

  // Load threads from server on mount
  useEffect(() => {
    api.threads.list(USER_ID).then((res) => {
      const data = res.data as any;
      if (data?.threads) {
        const loaded: Thread[] = data.threads.map((t: any) => ({
          thread_id: t.thread_id,
          title: t.title || 'Untitled',
          created_at: t.created_at,
          updated_at: t.updated_at,
          message_count: t.message_count,
          messages: [],
        }));
        setThreads(loaded);
      }
    }).catch(() => {});
  }, []);

  const activeThread = threads.find((t) => t.thread_id === activeThreadId);

  const loadThreadMessages = useCallback(async (threadId: string) => {
    const res = await api.threads.messages(threadId);
    const data = res.data as any;
    if (data?.messages) {
      const msgs: ChatMessage[] = data.messages.map((m: any) => ({
        role: m.role,
        content: m.content,
      }));
      setThreads((prev) =>
        prev.map((t) =>
          t.thread_id === threadId ? { ...t, messages: msgs } : t
        )
      );
    }
  }, []);

  const selectThread = useCallback(async (id: string) => {
    setActiveThreadId(id);
    await loadThreadMessages(id);
  }, [loadThreadMessages]);

  const newThread = useCallback(() => {
    const id = `thread_${Date.now()}`;
    const t = makeThread(id);
    setThreads((prev) => [t, ...prev]);
    setActiveThreadId(id);
    setTotalTokens(0);
    setLastLatencyMs(undefined);
    setLastReceipt(undefined);
  }, []);

  const sendMessage = useCallback(
    async (text: string, provider?: string, model?: string) => {
      let threadId = activeThreadId;

      if (!threadId) {
        threadId = `thread_${Date.now()}`;
        const t = makeThread(threadId);
        setThreads((prev) => [t, ...prev]);
        setActiveThreadId(threadId);
      }

      const userMsg: ChatMessage = { role: 'user', content: text };
      setThreads((prev) =>
        prev.map((t) => {
          if (t.thread_id !== threadId) return t;
          return {
            ...t,
            messages: [...t.messages, userMsg],
            message_count: t.message_count + 1,
            updated_at: new Date().toISOString(),
            title: t.title || text.slice(0, 48),
          };
        })
      );

      setLoading(true);

      try {
        const res = await api.chat.turn({
          message: text,
          thread_id: threadId,
          user_id: USER_ID,
          provider,
          model,
        });

        const data = res.data as any;
        const content = data?.assistant_message?.content ?? 'No response.';
        const receipt = data?.receipt ?? {};
        const latency = receipt.latency_ms;
        const threadTokens = receipt.thread_total_tokens ?? 0;

        if (latency) setLastLatencyMs(latency);
        if (threadTokens) setTotalTokens(threadTokens);

        setLastReceipt({
          userTokens: receipt.user_tokens ?? 0,
          assistantTokens: receipt.assistant_tokens ?? 0,
          threadTotalTokens: receipt.thread_total_tokens ?? 0,
          latencyMs: receipt.latency_ms ?? 0,
        });

        // Update thread title from server if it was just generated
        const serverThreadId = data?.thread_id;

        const assistantMsg: ChatMessage = {
          role: 'assistant',
          content,
          latency_ms: latency,
        };
        setThreads((prev) =>
          prev.map((t) => {
            if (t.thread_id !== threadId && t.thread_id !== serverThreadId) return t;
            const id = serverThreadId || threadId!;
            if (t.thread_id !== id) return t;
            return {
              ...t,
              thread_id: id,
              messages: [...t.messages, assistantMsg],
              message_count: t.message_count + 1,
              updated_at: new Date().toISOString(),
            };
          })
        );

        // Refresh thread list to get server-generated titles
        api.threads.list(USER_ID).then((r) => {
          const d = r.data as any;
          if (d?.threads) {
            setThreads((prev) => {
              const serverMap: Record<string, any> = {};
              d.threads.forEach((t: any) => { serverMap[t.thread_id] = t; });
              return prev.map((t) => {
                const s = serverMap[t.thread_id];
                if (s && s.title && !t.title) {
                  return { ...t, title: s.title };
                }
                return t;
              });
            });
          }
        }).catch(() => {});

      } catch {
        const errMsg: ChatMessage = {
          role: 'assistant',
          content: 'Backend unreachable — check server and API keys.',
        };
        setThreads((prev) =>
          prev.map((t) =>
            t.thread_id === threadId
              ? { ...t, messages: [...t.messages, errMsg] }
              : t
          )
        );
      } finally {
        setLoading(false);
      }
    },
    [activeThreadId]
  );

  return {
    threads,
    activeThread,
    activeThreadId,
    loading,
    lastLatencyMs,
    totalTokens,
    lastReceipt,
    newThread,
    selectThread,
    sendMessage,
  };
}
