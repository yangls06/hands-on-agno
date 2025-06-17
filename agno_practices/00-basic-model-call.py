from agno.agent import Agent
from agno_practices import openai_gpt_4o
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=openai_gpt_4o,
    markdown=True,
)
agent.print_response("What is AI Agent?", stream=True)

# HOW TO RUN
# (workspace) ~/workspace$ python -m agno_practices.00-basic-model-call
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                            ┃
# ┃ What is AI Agent?                                                                                          ┃
# ┃                                                                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (4.6s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                            ┃
# ┃ An AI agent is a software entity that uses artificial intelligence techniques to perceive its environment  ┃
# ┃ through sensors, make decisions, and take actions to achieve specific goals. It is an autonomous system    ┃
# ┃ that interacts with its environment, continually learning and adapting based on feedback or new data. AI   ┃
# ┃ agents can range from simple programs to complex systems, and they are designed to perform tasks that      ┃
# ┃ typically require human intelligence.                                                                      ┃
# ┃                                                                                                            ┃
# ┃ Here are some key characteristics of AI agents:                                                            ┃
# ┃                                                                                                            ┃
# ┃  1 Autonomy: AI agents operate independently without human intervention, making decisions based on their   ┃
# ┃    programming and the information available to them.                                                      ┃
# ┃  2 Reactivity: They perceive their environment and respond or adapt to changes, ensuring they remain       ┃
# ┃    aligned with their objectives.                                                                          ┃
# ┃  3 Proactivity: Beyond reacting, AI agents can take initiative, anticipate future states, and act to       ┃
# ┃    achieve their goals.                                                                                    ┃
# ┃  4 Social Ability: Some AI agents can interact with other agents or humans, sharing information and        ┃
# ┃    collaborating to reach objectives.                                                                      ┃
# ┃  5 Learning: Many AI agents incorporate machine learning techniques that allow them to improve their       ┃
# ┃    performance over time as they accumulate more data.                                                     ┃
# ┃                                                                                                            ┃
# ┃ AI agents are employed in various applications, including:                                                 ┃
# ┃                                                                                                            ┃
# ┃  • Robotics: Navigating and interacting with physical environments.                                        ┃
# ┃  • Virtual Assistants: Such as Siri or Alexa, processing natural language and managing tasks.              ┃
# ┃  • Game AI: Controlling non-player characters that adapt to player actions.                                ┃
# ┃  • Autonomous Vehicles: Navigating roads and making driving decisions.                                     ┃
# ┃  • Healthcare: Analyzing data to assist in diagnostics or treatment plans.                                 ┃
# ┃                                                                                                            ┃
# ┃ AI agents play a crucial role in advancing automation and intelligent systems across industries, enhancing ┃
# ┃ efficiency and enabling new capabilities.                                                                  ┃
# ┃                                                                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# (workspace) ~/workspace$
