from typing import Iterator
from agno.agent import Agent, RunResponse
from agno_practices import openai_gpt_4o
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import Workflow

class CacheWorkflow(Workflow):
  # Add agents or teams as attributes on the workflow
  agent = Agent(model=openai_gpt_4o)
  
  # Write logic in the run method
  def run(self, message: str) -> Iterator[RunResponse]:
    logger.info(f"Checking cache for '{message}'")
    # Check if the output is already cached:
    if self.session_state.get(message):
      logger.info(f"Cache hit for '{message}'")
      yield RunResponse(
        run_id = self.run_id, content=self.session_state.get(message)
      )
      return

    logger.info(f"Cache miss for '{message}'")
    # run the agent and yield the response
    yield from self.agent.run(message, stream=True)

    # Cache the response
    self.session_state[message] = self.agent.run_response.content

if __name__ == "__main__":
  workflow = CacheWorkflow()

  # Run the workflow
  response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")

  # Print the response
  pprint_run_response(response, markdown=True, show_time=True)

  # Run the workflow again with the same message
  response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")
  # Print the response
  pprint_run_response(response, markdown=True, show_time=True)


# (.venv) ~/workspace$ python -m agno_practices.05-agentic-workflow
# INFO Checking cache for 'Tell me a joke.'                                                          
# INFO Cache miss for 'Tell me a joke.'                                                              
# ╭──────────┬──────────────────────────────────────────────────────────────────────────────────────╮
# │ Response │ Sure! Here's one for you:                                                            │
# │ (2.1s)   │                                                                                      │
# │          │ Why did the scarecrow win an award?                                                  │
# │          │ Because he was outstanding in his field! 🌾                                          │
# ╰──────────┴──────────────────────────────────────────────────────────────────────────────────────╯
# INFO Checking cache for 'Tell me a joke.'                                                          
# INFO Cache hit for 'Tell me a joke.'                                                               
# WARNING  Workflow.run() should only yield RunResponseEvent objects, got: <class                    
#          'agno.run.response.RunResponse'>                                                          
# ╭──────────┬──────────────────────────────────────────────────────────────────────────────────────╮
# │ Response │                                                                                      │
# │ (0.0s)   │                                                                                      │
# ╰──────────┴──────────────────────────────────────────────────────────────────────────────────────╯
# (.venv) ~/workspace$ 
