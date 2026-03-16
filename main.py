from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
# Initialize the OpenAI and Anthropic chat models
# openai_llm = ChatOpenAI(model="gpt-4-0613")
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")





