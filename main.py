from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import search_tool, wikipedia_tool


load_dotenv()

class ResponseModel(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]

# Initialize the Anthropic chat model
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser = PydanticOutputParser(pydantic_object=ResponseModel)

# Define system prompt for the agent
system_prompt = """You are a helpful research assistant that will help generate a research paper.
Answer the user query and use available tools when needed.
Format your response as JSON with the following structure:
{format_instructions}"""

# Create tools list
tools = [search_tool, wikipedia_tool]

# Create agent using the modern LangChain API (LangGraph)
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt.format(format_instructions=parser.get_format_instructions())
)

# Get query from user
query = input("What can I help you with? ")

# Run the agent directly (no AgentExecutor needed in this version)
try:
    print("\n--- Running Agent ---")
    response = agent.invoke({"messages": [{"role": "user", "content": query}]})
    
    print("\n--- Agent Response ---")
    print(response)
    
    # Extract the assistant's response
    if "messages" in response:
        for msg in response["messages"]:
            if msg.get("role") == "assistant":
                content = msg.get("content", "")
                print(f"\nAssistant: {content}")
                
                # Try to parse as structured format
                try:
                    structured = parser.parse(content)
                    print("\n--- Parsed Structured Response ---")
                    print(f"Topic: {structured.topic}")
                    print(f"Summary: {structured.summary}")
                    print(f"Sources: {structured.source}")
                    print(f"Tools Used: {structured.tools_used}")
                except Exception as e:
                    print(f"Note: Response wasn't in expected format: {e}")
                    
except Exception as e:
    print(f"Error running agent: {e}")
    import traceback
    traceback.print_exc()