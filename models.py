import os

# Access your API keys from environment variables
openai_key = os.environ.get('OPENAI_API_KEY')
claude_key = os.environ.get('ANTHROPIC_API_KEY')
openai_base_url = os.environ.get('OPENAI_BASE_URL')
claude_base_url = os.environ.get('ANTHROPIC_BASE_URL')

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat

agent = Agent(model=OpenAIChat(id="gpt-4o", base_url=openai_base_url),
              markdown=True)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
