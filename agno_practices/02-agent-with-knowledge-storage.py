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
  # agent.knowledge.load(recreate=True)
  agent.print_response("What is Agno?", stream=True)

# (workspace) ~/workspace$ PYTHONPATH=/home/runner/workspace python agno_practices/02-agent-with-knowledge-storage.py
# (workspace) ~/workspace$ python -m agno_practices.02-agent-with-knowledge-storage
# INFO Found 3 documents
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                             ┃
# ┃ What is Agno?                                                                               ┃
# ┃                                                                                             ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                             ┃
# ┃ • search_knowledge_base(query=Agno)                                                         ┃
# ┃                                                                                             ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (6.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                             ┃
# ┃ Agno is a full-stack framework used for building Multi-Agent Systems with features like     ┃
# ┃ memory, knowledge, and reasoning. It is designed to construct agent systems across five     ┃
# ┃ levels, ranging from agents equipped with tools and instructions to advanced agent          ┃
# ┃ workflows that include state and determinism. Here are the key characteristics of Agno:     ┃
# ┃                                                                                             ┃
# ┃   1 Model Agnostic: Supports over 23 model providers with no lock-in.                       ┃
# ┃   2 Highly Performant: Agents can instantiate in about 3μs, using approximately 6.5Kib of   ┃
# ┃     memory.                                                                                 ┃
# ┃   3 First Class Reasoning: Provides reasoning models and tools, essential for complex       ┃
# ┃     autonomous agents.                                                                      ┃
# ┃   4 Multi-Modality: Accepts various input forms like text, image, audio, and video, and     ┃
# ┃     similarly outputs them.                                                                 ┃
# ┃   5 Advanced Architecture: Offers an industry-leading multi-agent architecture with         ┃
# ┃     reasoning, memory, and shared context.                                                  ┃
# ┃   6 Agentic Search: Enables runtime information search using over 20 vector databases.      ┃
# ┃   7 Memory & Session Storage: Includes built-in drivers for long-term memory and session    ┃
# ┃     storage.                                                                                ┃
# ┃   8 Structured Outputs: Provides fully-typed responses through model-provided structured    ┃
# ┃     outputs or json_mode.                                                                   ┃
# ┃   9 Monitoring: Real-time agent session and performance monitoring capabilities.            ┃
# ┃                                                                                             ┃
# ┃ Agno is suitable for building real-world applications and offers tools for deploying agents ┃
# ┃ using pre-built FastAPI routes quickly.                                                     ┃
# ┃                                                                                             ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# (workspace) ~/workspace$
