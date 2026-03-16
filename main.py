from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.tools import tool

load_dotenv()

class ResponseModel(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]

# Initialize the OpenAI and Anthropic chat models
# openai_llm = ChatOpenAI(model="gpt-4-0613")
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser = PydanticOutputParser(pydantic_object=ResponseModel)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
    ("system",
     """
    You are a helpful research assistant that will help generate a research paper.
    Answer the user query and necessary tools.
    Wrap the output in this format and provide no other text
    {format_instructions}
    """, 
    ),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

# Simple LLM invocation without agent
raw_response = llm.invoke(prompt.format(query="What is the impact of climate change on earth", agent_scratchpad=[], chat_history=[]))
print(raw_response)

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
except Exception as e:
    print(e)