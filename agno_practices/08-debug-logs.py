from agno.agent import Agent
from agno_practices import openai_gpt_4o
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=openai_gpt_4o,
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
    debug_mode=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)

# python -m agno_practices.08-debug-logs
# DEBUG ************************ Agent ID: ab1ed48e-ef14-499e-9e9e-e437ab4e7909 ***********************              
# DEBUG *********************** Session ID: 1d35f6cd-df82-4c67-9c7a-5b72090e9b87 **********************              
# DEBUG Processing tools for model                                                                                   
# DEBUG Added tool get_current_stock_price from yfinance_tools                                                       
# DEBUG ******************** Agent Run Start: 6caec9da-007b-479f-99bc-c22d4b215d77 ********************              
# DEBUG --------------------------------- OpenAI Response Stream Start --------------------------------              
# DEBUG ---------------------------------------- Model: gpt-4o ----------------------------------------              
# DEBUG ============================================ system ===========================================              
# DEBUG <instructions>                                                                                               
#       Use tables to display data. Don't include any other text.                                                    
#       </instructions>                                                                                              
                                                                                                                   
#       <additional_information>                                                                                     
#       - Use markdown to format your answers.                                                                       
#       </additional_information>                                                                                    
# DEBUG ============================================= user ============================================              
# DEBUG What is the stock price of Apple?                                                                            
# DEBUG ========================================== assistant ==========================================              
# DEBUG Tool Calls:                                                                                                  
#         - ID: 'call_67NepYv47BCyoxdwt3CPvuLk'                                                                      
#           Name: 'get_current_stock_price'                                                                          
#           Arguments: 'symbol: AAPL'                                                                                
# DEBUG ******************************************  METRICS  ******************************************              
# DEBUG * Tokens:                      input=103, output=18, total=121                                               
# DEBUG * Prompt tokens details:       {'audio_tokens': 0, 'cached_tokens': 0, 'text_tokens': 0, 'image_tokens': 0}  
# DEBUG * Completion tokens details:   {'audio_tokens': 0, 'reasoning_tokens': 0, 'text_tokens': 0}                  
# DEBUG * Time:                        2.2928s                                                                       
# DEBUG * Tokens per second:           7.8507 tokens/s                                                               
# DEBUG * Time to first token:         2.2175s                                                                       
# DEBUG ******************************************  METRICS  ******************************************              
# DEBUG Running: get_current_stock_price(symbol=AAPL)                                                                
# DEBUG Fetching current price for AAPL                                                                              
# DEBUG ============================================= tool ============================================              
# DEBUG Tool call Id: call_67NepYv47BCyoxdwt3CPvuLk                                                                  
# DEBUG Error fetching current price for AAPL: Too Many Requests. Rate limited. Try after a while.                   
# DEBUG ****************************************  TOOL METRICS  ***************************************              
# DEBUG * Time:                        2.2404s                                                                       
# DEBUG ****************************************  TOOL METRICS  ***************************************              
# DEBUG ========================================== assistant ==========================================              
# DEBUG | **Stock** | **Price**   | **Error**                                |                                       
#       |-----------|-------------|------------------------------------------|                                       
#       | Apple     | N/A         | Too Many Requests. Rate limited.         |                                       
# DEBUG ******************************************  METRICS  ******************************************              
# DEBUG * Tokens:                      input=150, output=42, total=192                                               
# DEBUG * Prompt tokens details:       {'audio_tokens': 0, 'cached_tokens': 0, 'text_tokens': 0, 'image_tokens': 0}  
# DEBUG * Completion tokens details:   {'audio_tokens': 0, 'reasoning_tokens': 0, 'text_tokens': 0}                  
# DEBUG * Time:                        3.3100s                                                                       
# DEBUG * Tokens per second:           12.6889 tokens/s                                                              
# DEBUG * Time to first token:         2.6422s                                                                       
# DEBUG ******************************************  METRICS  ******************************************              
# DEBUG ---------------------------------- OpenAI Response Stream End ---------------------------------              
# DEBUG Added RunResponse to Memory                                                                                  
# DEBUG ********************* Agent Run End: 6caec9da-007b-479f-99bc-c22d4b215d77 *********************              
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                 ┃
# ┃ What is the stock price of Apple?                                                                               ┃
# ┃                                                                                                                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                 ┃
# ┃ • get_current_stock_price(symbol=AAPL)                                                                          ┃
# ┃                                                                                                                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (7.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                 ┃
# ┃                                                                                                                 ┃
# ┃                                                                                                                 ┃
# ┃   Stock   Price   Error                                                                                         ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                             ┃
# ┃   Apple   N/A     Too Many Requests. Rate limited.                                                              ┃
# ┃                                                                                                                 ┃
# ┃                                                                                                                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛