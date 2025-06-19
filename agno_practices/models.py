import os
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Access your API keys from environment variables
openai_key = os.environ.get('OPENAI_API_KEY')
openai_base_url = os.environ.get('OPENAI_BASE_URL')

# create a openai model and import for use
openai_gpt_4o = OpenAIChat(id="gpt-4o", base_url=openai_base_url)

# Export the model for use in other files
__all__ = ['openai_gpt_4o']
