from agno.agent import Agent
from agno_practices import openai_gpt_4o
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType

# Load agno document for the URL
knowledge = UrlKnowledge(urls=["https://docs.agno.com/introduction.md"],
                         vector_db=LanceDb(
                             uri="tmp/lancedb",
                             table_name="agno_docs",
                             search_type=SearchType.hybrid,
                             embedder=OpenAIEmbedder(
                                 id='text-embedding-3-small', dimensions=1536),
                         ))
# Store agent sessions in SQLite
storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

# the	agent
agent = Agent(
    name="Agno Asist",
    model=openai_gpt_4o,
    instructions=[
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
  # Load the knowledge base, comment out after first run
  # Set recreate to True to recreate the knowledge base if needed
  agent.knowledge.load(recreate=True)
  agent.print_response("What is Agno?", stream=True)
