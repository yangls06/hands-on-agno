import os
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat

# Access your API keys from environment variables
openai_key = os.environ.get('OPENAI_API_KEY')
claude_key = os.environ.get('ANTHROPIC_API_KEY')
openai_base_url = os.environ.get('OPENAI_BASE_URL')
claude_base_url = os.environ.get('ANTHROPIC_BASE_URL')

# create a openai model and import for use
openai_gpt_4o = OpenAIChat(id="gpt-4o", base_url=openai_base_url)

# Export the model for use in other files
__all__ = ['openai_gpt_4o']
