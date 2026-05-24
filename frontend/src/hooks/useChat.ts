import { useState, useCallback } from 'react';
import { ChatMessage, Thread } from '../types';
import { api } from '../api/client';

const SESSION_ID = `session_${Date.now()}`;
const USER_ID = 'dev_user';

function makeThread(id: string): Thread {
  return {
    thread_id: id,
    title: '',
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

  const activeThread = threads.find((t) => t.thread_id === activeThreadId);

  const newThread = useCallback(() => {
    const id = `thread_${Date.now()}`;
    const t = makeThread(id);
    setThreads((prev) => [t, ...prev]);
    setActiveThreadId(id);
  }, []);

  const selectThread = useCallback((id: string) => {
    setActiveThreadId(id);
  }, []);

  const sendMessage = useCallback(
    async (text: string, provider?: string, model?: string) => {
      let threadId = activeThreadId;

      if (!threadId) {
        threadId = `thread_${Date.now()}`;
        const t = makeThread(threadId);
        t.title = text.slice(0, 48);
        setThreads((prev) => [t, ...prev]);
        setActiveThreadId(threadId);
      }

      const userMsg: ChatMessage = { role: 'user', content: text };

      setThreads((prev) =>
        prev.map((t) => {
          if (t.thread_id !== threadId) return t;
          const updated = {
            ...t,
            messages: [...t.messages, userMsg],
            message_count: t.message_count + 1,
            updated_at: new Date().toISOString(),
          };
          if (!updated.title) updated.title = text.slice(0, 48);
          return updated;
        })
      );

      setLoading(true);

      try {
        const res = await api.chat.turn({
          message: text,
          thread_id: threadId,
          session_id: SESSION_ID,
          user_id: USER_ID,
          provider,
          model,
        });

        const data = res.data as any;
        const assistantContent =
          data?.assistant_message?.content ??
          (res.ok
            ? 'Response received.'
            : res.message ?? 'Error from backend.');

        const assistantMsg: ChatMessage = {
          role: 'assistant',
          content: assistantContent,
        };

        setThreads((prev) =>
          prev.map((t) => {
            if (t.thread_id !== threadId) return t;
            return {
              ...t,
              messages: [...t.messages, assistantMsg],
              message_count: t.message_count + 1,
              updated_at: new Date().toISOString(),
            };
          })
        );
      } catch (err) {
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
    newThread,
    selectThread,
    sendMessage,
  };
}
