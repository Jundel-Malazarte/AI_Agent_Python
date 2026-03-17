from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

# Initialize the underlying implementations
duck_duck_search = DuckDuckGoSearchRun()
wikipedia_wrapper = WikipediaAPIWrapper()

# Define tools using decorators
@tool
def search_tool(query: str) -> str:
    """Search the web for information using DuckDuckGo"""
    return duck_duck_search.run(query)

@tool
def wikipedia_tool(query: str) -> str:
    """Search Wikipedia for information"""
    return wikipedia_wrapper.run(query)