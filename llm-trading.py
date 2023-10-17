'''
RBI - Research, backtest, implement
LLMs - RBI 
'''

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
import langchainkeys as l 
import time 


###### RBI SYSTEM ########

#### RESEARCH LLM ########
# research trading strategies
llm_research = OpenAI(openai_api_key=l.open_ai_key, temperature=0) # initialize openai LLM for the research

research_template = """look at the recent market data for bitcoin and make a trading strategy for it. use {indicator} and 2 others of your choice. over the last {time_period} days """

research_prompt = PromptTemplate(template=research_template, input_variables=["indicator", "time_period"])

# create an llmchain for research
research_chain = LLMChain(prompt=research_prompt, llm=llm_research)

# generate trading strategies 
research_result = research_chain.run({"indicator": "RSI", "time_period": "30"})


time.sleep(8756) # to not go passed

#### BACKTEST LLM ########
# use the ideas that the LLM above came up with and build a backtest
backtesting_strategies = research_result.output 

# implement the backtesing logic 
#TODO - #backtestint_code =

#### BUG TESTING LLM ######
llm_debugging = OpenAI(openai_api_key=l.open_ai_key, temperature=0)

# define a prompt template for code debugging
debugging_template = """give the backtesting coe, identify and fix any coding bugs or issues"""

debugging_prompt = PromptTemplate(template=debugging_template)

# create chain for code debugging
debugging_chain = LLMChain(prompt=debugging_prompt, llm=llm_debugging)

debugging_result = debugging_chain.run(backesting_code)

# fix any coding bugs in the backtesting code
fixed_backtesting_code = debugging_result.output 