export type RiskLevel = 'low' | 'medium' | 'high';
export type ActionStatus = 'pending_approval' | 'approved' | 'rejected' | 'executed' | 'failed';

export interface ProposedAction {
  action_id: str;
  agent_name: str;
  tool_name: str;
  risk_level: RiskLevel;
  description: str;
  parameters: Record<string, any>;
  created_at: str;
  status: ActionStatus;
  approval_comment?: str;
}

export interface UserQueryRequest {
  query: string;
  user_id?: string;
  provider?: 'anthropic' | 'openai' | 'gemini';
}

export interface UserQueryResponse {
  status: string;
  data: {
    query: string;
    routed_to: string;
    execution: Record<string, any>;
  };
}

export interface UserProfile {
  name: string;
  email: string;
  role: string;
  avatar: string;
  theme: 'light' | 'dark';
}

export interface AgentCardInfo {
  id: string;
  name: string;
  role: string;
  badge: string;
  description: string;
  capabilities: string[];
  mcpTools: string[];
}
