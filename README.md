<<<<<<< HEAD
# Advanced AI Agents

A learning project focused on building personal AI agents and understanding the concepts behind modern agentic AI systems.

This repository documents my journey of learning Advanced AI through practical implementation.

## Current Implementation

### Simple AI Assistant

A command-line AI assistant powered by an LLM with function/tool calling capabilities.

**Features:**
- Interactive command-line conversation.
- Maintains conversation history using message roles.
- LLM-powered tool selection.
- Executes Python functions based on LLM tool calls.
- Returns tool execution results to the LLM for generating responses.
- Retrieves the current date and time through a custom tool.

## Tech Stack

- Python
- OpenAI Python SDK
- LLM API
- Function Calling / Tool Calling
- python-dotenv

## Project Structure

```text
.
├── simple_ai_assistant.py
├── tools.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/advanced-ai-agents.git
cd advanced-ai-agents
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` as a reference and provide your API configuration.

### 5. Run the assistant

```bash
python simple_ai_assistant.py
```

## Learning Roadmap

This project will evolve as I explore more advanced AI and agentic AI concepts through practical implementations.

- [x] Basic LLM-powered assistant
- [x] Conversation history management
- [x] Function / Tool calling
- [x] Current date and time tool
- [ ] Multiple custom tools
- [ ] Advanced tool execution workflows
- [ ] Multi-step agentic workflows
- [ ] Personal AI agents

*More implementations will be added as I progress.*
=======
# advanced-ai-agents
Building personal AI agents while learning advanced AI concepts, tool calling, agentic workflows, and LLM integrations.
>>>>>>> 692f2ee5f8a8863c1d3cb0408e196befa7981f03
