# AI Research Assistant Chatbot

An intelligent AI-powered research assistant built with Python that leverages advanced language models to generate comprehensive research papers with structured outputs, summaries, and source citations.

## Overview

The **AI Research Assistant Chatbot** is an AI agent designed to help users research topics and generate well-structured research content. It utilizes Claude 3.5 Sonnet from Anthropic as its backbone LLM, integrated with LangChain for seamless orchestration and Wikipedia for real-time information retrieval.

The chatbot processes user queries and returns structured responses containing:
- **Topic**: The research topic in focus
- **Summary**: A detailed summary of the research findings
- **Sources**: Cited sources used in the research
- **Tools Used**: List of tools utilized to gather information

## Features

✨ **Intelligent Query Processing** - Understands complex research questions and generates relevant responses  
🔍 **Wikipedia Integration** - Access to real-time information from Wikipedia for comprehensive research  
🤖 **Advanced LLM** - Powered by Claude 3.5 Sonnet for high-quality responses  
📊 **Structured Output** - Returns data in a validated, structured format using Pydantic  
🔐 **Environment Management** - Secure handling of API keys and environment variables  
💾 **Type Safety** - Strong typing with Pydantic models for data validation  

## Technologies & Libraries

### Core Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| **langchain** | Latest | LLM orchestration and agent framework |
| **langchain-community** | Latest | Community integrations for LangChain |
| **langchain-openai** | Latest | OpenAI API integration |
| **langchain-anthropic** | Latest | Anthropic Claude API integration |
| **wikipedia** | Latest | Wikipedia API wrapper for information retrieval |
| **pydantic** | Latest | Data validation using Python type annotations |
| **python-dotenv** | Latest | Environment variable management |

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- An Anthropic API key (for Claude models)

### Step 1: Clone the Repository
```bash
cd AI_Chatbot
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv .venv

# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the project root directory:
```
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Usage

### Basic Usage
```python
python main.py
```

The chatbot will process the configured query and return a structured response with research data.

### Example Query
```python
# The agent will automatically process this query:
# "What is the impact of climate change on earth"

# Expected Output Structure:
# {
#   "topic": "Impact of Climate Change on Earth",
#   "summary": "Detailed research summary...",
#   "source": ["Wikipedia", "..."],
#   "tools_used": ["wikipedia_search", "claude_llm"]
# }
```

## Project Structure
```
AI_Chatbot/
├── main.py                 # Main chatbot script with LLM logic
├── tools.py               # Utility tools and custom functions
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .venv/                 # Virtual environment (created during setup)
└── README.md             # Project documentation
```

## Key Components

### ResponseModel (Pydantic)
A structured data model that ensures all responses follow a consistent format:
- `topic`: Research topic string
- `summary`: Detailed summary of findings
- `source`: List of information sources
- `tools_used`: List of tools utilized

### LangChain Integration
- **ChatPromptTemplate**: Constructs multi-message prompts for the LLM
- **ChatAnthropic**: Interface to Claude 3.5 Sonnet model
- **PydanticOutputParser**: Parses LLM output into structured Pydantic models

## Configuration

### Supported Models
- **Primary**: Claude 3.5 Sonnet (Recommended)
- **Alternative**: GPT-4 (uncomment in `main.py`)

### Environment Variables
Add these to your `.env` file:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'langchain'`
- **Solution**: Ensure virtual environment is activated and run `pip install -r requirements.txt`

**Issue**: `API Key Error`
- **Solution**: Verify your `.env` file exists and contains a valid `ANTHROPIC_API_KEY`

**Issue**: `Wikipedia connection error`
- **Solution**: Check internet connectivity and ensure `wikipedia` package is installed

## License

This project is available for educational and development purposes.

## Contact & Support

For questions or issues, please refer to the LangChain documentation or Anthropic's Claude API documentation.

---

**Last Updated**: March 2026  
**Python Version**: 3.8+
