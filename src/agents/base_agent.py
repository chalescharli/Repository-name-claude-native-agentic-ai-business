from typing import List, Dict, Any, Optional
import json
import anthropic
from config.settings import settings
from config.logging_config import logger

class BaseAgent:
    """Base class for all specialized AI Business Agents."""
    
    def __init__(self, name: str, role_description: str, system_prompt: str):
        self.name = name
        self.role_description = role_description
        self.system_prompt = system_prompt
        self.tools: List[Dict[str, Any]] = []
        self._tool_handlers: Dict[str, Any] = {}
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY) if settings.ANTHROPIC_API_KEY else None

    def register_tool(self, name: str, description: str, input_schema: Dict[str, Any], handler: Any):
        """Register an MCP tool handler for this agent."""
        tool_def = {
            "name": name,
            "description": description,
            "input_schema": input_schema
        }
        self.tools.append(tool_def)
        self._tool_handlers[name] = handler

    def execute(self, user_query: str) -> Dict[str, Any]:
        """Execute agent workflow using Claude tool calling or direct tool resolution fallback."""
        logger.info(f"[{self.name}] Executing query: '{user_query}'")

        if not self.client:
            # Fallback mock mode when ANTHROPIC_API_KEY is not set
            return self._execute_heuristic(user_query)

        try:
            response = self.client.messages.create(
                model=settings.DEFAULT_CLAUDE_MODEL,
                max_tokens=1024,
                system=self.system_prompt,
                messages=[{"role": "user", "content": user_query}],
                tools=self.tools if self.tools else None
            )

            # Check if Claude called a tool
            if response.stop_reason == "tool_use":
                tool_use = next(block for block in response.content if block.type == "tool_use")
                tool_name = tool_use.name
                tool_input = tool_use.input
                
                logger.info(f"[{self.name}] Claude selected tool '{tool_name}' with input: {tool_input}")
                
                if tool_name in self._tool_handlers:
                    tool_result = self._tool_handlers[tool_name](**tool_input)
                    return {
                        "agent": self.name,
                        "tool_used": tool_name,
                        "tool_input": tool_input,
                        "result": tool_result,
                        "status": "success"
                    }

            # Text response from Claude
            text_content = next(block.text for block in response.content if block.type == "text")
            return {
                "agent": self.name,
                "response": text_content,
                "status": "success"
            }
            
        except Exception as e:
            logger.error(f"[{self.name}] Error executing Claude API: {e}")
            return self._execute_heuristic(user_query)

    def _execute_heuristic(self, user_query: str) -> Dict[str, Any]:
        """Heuristic execution fallback when Anthropic API key is not configured."""
        query_lower = user_query.lower()

        for tool_name, handler in self._tool_handlers.items():
            if "booking" in query_lower and ("get_daily_bookings" in tool_name or "get_booking_details" in tool_name):
                res = handler()
                return {"agent": self.name, "tool_used": tool_name, "result": res, "mode": "heuristic_fallback"}
            elif ("cancellation" in query_lower or "sop" in query_lower or "policy" in query_lower or "procedure" in query_lower) and "search_sharepoint_sop" in tool_name:
                res = handler(query=user_query)
                return {"agent": self.name, "tool_used": tool_name, "result": res, "mode": "heuristic_fallback"}
            elif ("email" in query_lower or "mail" in query_lower or "send" in query_lower) and "create_email_draft" in tool_name:
                res = handler(recipient="customer@example.com", subject="Follow-up", body="Thank you for booking with us.")
                return {"agent": self.name, "tool_used": tool_name, "result": res, "mode": "heuristic_fallback"}

        return {
            "agent": self.name,
            "response": f"Processed query '{user_query}' through {self.name} system prompt rules.",
            "status": "success"
        }
