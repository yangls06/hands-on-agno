from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno_practices import openai_gpt_4o
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

memory = Memory(
    # Use any model for creating and managing memories
    model=openai_gpt_4o,
    # Store memories in a SQLite database
    db=SqliteMemoryDb(table_name="user_memories", db_file="tmp/agent.db"),
    # We disable deletion by default, enable it if needed
    delete_memories=True,
    clear_memories=True,
)

agent = Agent(
    model=openai_gpt_4o,
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True,
                      analyst_recommendations=True,
                      company_info=True,
                      company_news=True),
    ],
    # User ID for storing memories, `default` if not provided
    user_id="Andy",
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Only include the report in your response. No other text.",
    ],
    memory=memory,
    # Let the Agent manage its memories
    enable_agentic_memory=True,
    markdown=True,
)

if __name__ == "__main__":
    # This will create a memory that "ava's" favorite stocks are NVIDIA and TSLA
    agent.print_response(
        "My favorite stocks are NVIDIA and TSLA",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
    # This will use the memory to answer the question
    agent.print_response(
        "Can you compare my favorite stocks?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )

# (workspace) ~/workspace$ PYTHONPATH=/home/runner/workspace python agno_practices/03-agent-with-memory-and-reasonning.py
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                        ┃
# ┃ My favorite stocks are NVIDIA and TSLA                                                 ┃
# ┃                                                                                        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                        ┃
# ┃ • update_user_memory(task=Add that the user's favorite stocks are NVIDIA and TSLA.)    ┃
# ┃                                                                                        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (7.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                        ┃
# ┃ I've noted that your favorite stocks are NVIDIA and TSLA. How can I assist you with    ┃
# ┃ them today?                                                                            ┃
# ┃                                                                                        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# HTTP Error 401:
# HTTP Error 401:
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                        ┃
# ┃ Can you compare my favorite stocks?                                                    ┃
# ┃                                                                                        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                        ┃
# ┃ • get_current_stock_price(symbol=NVDA)                                                 ┃
# ┃ • get_current_stock_price(symbol=TSLA)                                                 ┃
# ┃ • get_company_info(symbol=NVDA)                                                        ┃
# ┃ • get_company_info(symbol=TSLA)                                                        ┃
# ┃ • get_analyst_recommendations(symbol=NVDA)                                             ┃
# ┃ • get_analyst_recommendations(symbol=TSLA)                                             ┃
# ┃                                                                                        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (14.8s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                        ┃
# ┃ Here's a comparison of NVIDIA and Tesla based on recent data:                          ┃
# ┃                                                                                        ┃
# ┃                                 Current Stock Prices:                                  ┃
# ┃                                                                                        ┃
# ┃                                                                                        ┃
# ┃   Stock    Current Price (USD)                                                         ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                        ┃
# ┃   NVIDIA   145.07                                                                      ┃
# ┃   Tesla    325.65                                                                      ┃
# ┃                                                                                        ┃
# ┃                                                                                        ┃
# ┃                                  Company Information:                                  ┃
# ┃                                                                                        ┃
# ┃                                                                                        ┃
# ┃   Attribute            NVIDIA Corporation   Tesla, Inc.                                ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                        ┃
# ┃   Sector               Technology           Consumer Cyclical                          ┃
# ┃   Industry             Semiconductors       Auto Manufacturers                         ┃
# ┃   Market Cap (USD)     3.54 Trillion        1.05 Trillion                              ┃
# ┃   EPS                  3.10                 1.74                                       ┃
# ┃   P/E Ratio            46.80                187.16                                     ┃
# ┃   52 Week Low (USD)    86.62                179.66                                     ┃
# ┃   52 Week High (USD)   153.13               488.54                                     ┃
# ┃   Employees            36,000               125,665                                    ┃
# ┃   Revenue Growth       69.2%                -9.2%                                      ┃
# ┃   Gross Margins        70.1%                17.7%                                      ┃
# ┃   EBITDA (USD)         88.25 Billion        12.55 Billion                              ┃
# ┃                                                                                        ┃
# ┃                                                                                        ┃
# ┃                                Analyst Recommendations:                                ┃
# ┃                                                                                        ┃
# ┃                                                                                        ┃
# ┃   Period      NVIDIA (NVDA) - Recommendations     Tesla (TSLA) - Recommendations       ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ┃
# ┃   Current     Strong Buy: 12, Buy: 46, Hold: 6,   Strong Buy: 7, Buy: 14, Hold: 16,    ┃
# ┃               Sell: 1, Strong Sell: 0             Sell: 7, Strong Sell: 3              ┃
# ┃   -1 Month    Strong Buy: 12, Buy: 44, Hold: 6,   Strong Buy: 7, Buy: 16, Hold: 14,    ┃
# ┃               Sell: 1, Strong Sell: 0             Sell: 8, Strong Sell: 3              ┃
# ┃   -2 Months   Strong Buy: 12, Buy: 44, Hold: 7,   Strong Buy: 7, Buy: 16, Hold: 14,    ┃
# ┃               Sell: 1, Strong Sell: 0             Sell: 9, Strong Sell: 2              ┃
# ┃   -3 Months   Strong Buy: 11, Buy: 47, Hold: 5,   Strong Buy: 7, Buy: 16, Hold: 14,    ┃
# ┃               Sell: 0, Strong Sell: 0             Sell: 9, Strong Sell: 2              ┃
# ┃                                                                                        ┃
# ┃                                                                                        ┃
# ┃                                    Company Summary:                                    ┃
# ┃                                                                                        ┃
# ┃ NVIDIA Corporation: A leader in computing infrastructure providing graphics, compute,  ┃
# ┃ and networking solutions worldwide. NVIDIA specializes in data center computing, AI    ┃
# ┃ solutions, automotive platforms, and more.                                             ┃
# ┃                                                                                        ┃
# ┃ Tesla, Inc.: Tesla designs and manufactures electric vehicles and energy               ┃
# ┃ generation/storage systems. Tesla's offerings include solar energy products and        ┃
# ┃ services related to electric vehicles worldwide.                                       ┃
# ┃                                                                                        ┃
# ┃                                        Sources:                                        ┃
# ┃                                                                                        ┃
# ┃  • NVIDIA Corporation Website                                                          ┃
# ┃  • Tesla Inc. Website                                                                  ┃
# ┃                                                                                        ┃
# ┃ Feel free to reach out if you need more insights on any specific aspect!               ┃
# ┃                                                                                        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# (workspace) ~/workspace$
