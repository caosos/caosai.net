import { useState, useEffect, useCallback } from 'react';
import { ModelContextSpec } from '../types';
import { api } from '../api/client';

export function useModels() {
  const [availableModels, setAvailableModels] = useState<ModelContextSpec[]>([]);
  const [activeModel, setActiveModel] = useState<ModelContextSpec | undefined>();
  const [error, setError] = useState<string | undefined>();

  useEffect(() => {
    api.models.list().then((res) => {
      const data = res.data as any;
      if (data?.available_models) {
        setAvailableModels(data.available_models);
        setActiveModel(data.active_model);
      }
    }).catch(() => {
      setError('Could not load models from backend.');
    });
  }, []);

  const selectModel = useCallback(async (provider: string, model: string) => {
    const res = await api.models.select(provider, model);
    const data = res.data as any;
    if (data?.active_model) {
      setActiveModel(data.active_model);
    }
  }, []);

  return { availableModels, activeModel, selectModel, error };
}
