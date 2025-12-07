"""langgraph_chatbot package initialization.

This package contains the deep research agent implementation with modules
for prompts, state management, and research workflows.
"""

# Import key modules to make them available at package level
from .prompts import *
from .state_scope import *
from .research_agent_scope import *

__all__ = [
    # From prompts.py
    'clarify_with_user_instructions',
    'transform_messages_into_research_topic_prompt',
    'research_agent_prompt',
    'summarize_webpage_prompt',
    'research_agent_prompt_with_mcp',
    'lead_researcher_prompt',
    'compress_research_system_prompt',
    'compress_research_human_message',
    'final_report_generation_prompt',
    'BRIEF_CRITERIA_PROMPT',
    'BRIEF_HALLUCINATION_PROMPT',

    # From state_scope.py
    'AgentInputState',
    'AgentState',
    'ClarifyWithUser',
    'ResearchQuestion',

    # From research_agent_scope.py
    'get_today_str',
    'clarify_with_user',
    'write_research_brief',
    'scope_research'
]