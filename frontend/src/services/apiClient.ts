import { UserQueryRequest, UserQueryResponse, ProposedAction } from '../types';

const API_BASE = '/api/v1';

export const apiClient = {
  async healthCheck() {
    const res = await fetch(`${API_BASE}/health`);
    if (!res.ok) throw new Error('Health check failed');
    return res.json();
  },

  async queryAgent(payload: UserQueryRequest): Promise<UserQueryResponse> {
    const res = await fetch(`${API_BASE}/query`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ message: 'Query processing failed' }));
      throw new Error(err.message || 'API Error');
    }
    return res.json();
  },

  async getPendingHITLActions(): Promise<{ pending_actions: Record<string, ProposedAction> }> {
    const res = await fetch(`${API_BASE}/hitl/pending`);
    if (!res.ok) throw new Error('Failed to fetch pending HITL actions');
    return res.json();
  },

  async approveHITLAction(action_id: string, approver_id: string = 'Rishan Admin', comment?: string) {
    const res = await fetch(`${API_BASE}/hitl/approve`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action_id, approver_id, comment }),
    });
    if (!res.ok) throw new Error('Failed to approve action');
    return res.json();
  },

  async rejectHITLAction(action_id: string, approver_id: string = 'Rishan Admin', reason: string = 'User cancelled') {
    const res = await fetch(`${API_BASE}/hitl/reject`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action_id, approver_id, reason }),
    });
    if (!res.ok) throw new Error('Failed to reject action');
    return res.json();
  }
};
