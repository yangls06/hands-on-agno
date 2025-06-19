from agno.agent import Agent
from agno_practices import openai_gpt_4o
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

agent_storage: str = "tmp/agents.db"

web_agent = Agent(
    name="Web Agent",
    model=openai_gpt_4o,
    tools=[DuckDuckGoTools()],
    instructions="Always includes sources",
    # storage the agent sessions in a sqlite database
    storage=SqliteStorage(table_name="web_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True)

finance_agent = Agent(name="Finance Agent",
                      model=openai_gpt_4o,
                      tools=[
                          YFinanceTools(stock_price=True,
                                        analyst_recommendations=True,
                                        company_info=True,
                                        company_news=True)
                      ],
                      instructions=["Always use tables to display data."],
                      add_datetime_to_instructions=True,
                      add_history_to_messages=True,
                      num_history_responses=5,
                      markdown=True)

playground_app = Playground(agents=[web_agent, finance_agent])
app = playground_app.get_app()

if __name__ == "__main__":
    playground_app.serve("playground:app", reload=True)

# source .venv/bin/activate
# pip install openai duckduckgo-search yfinance sqlalchemy 'fastapi[standard]' agno
