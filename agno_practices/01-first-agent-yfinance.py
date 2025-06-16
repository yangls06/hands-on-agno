from agno.agent import Agent
from agno_practices import openai_gpt_4o
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=openai_gpt_4o,
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)
