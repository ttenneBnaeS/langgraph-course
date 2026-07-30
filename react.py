from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num: float) -> float:
    """
    param num: a number to triple
    returns: the number tripled
    """
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]

llm = ChatAnthropic(model="claude-sonnet-5").bind_tools(tools)