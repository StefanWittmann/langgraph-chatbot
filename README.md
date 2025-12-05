# FD-Buddy Quick Start Guide

## Getting Started

First, clone the repository:
```bash
git clone https://github.com/StefanWittmann/fd-buddy.git
cd fd-buddy
```

## Setup Instructions

1. Initialize the project and set up the virtual environment:
```bash
uv init fd-buddy --python 3.13
uv sync
uv pip install "langgraph-cli[inmem]"
source .venv/bin/activate
```

2. Kill any existing processes on port 2024 (if needed):
```bash
lsof -ti:2024 | xargs kill -9
```

## Running the Application

1. Start the LangGraph development server:
```bash
uv run langgraph dev
```

2. The application will be available at `http://localhost:2024`

## Project Structure

- `agent.py`: Main agent implementation with LLM integration
- `fd-buddy.py`: Core application logic
- `requirements.txt`: Python dependencies
- `pyproject.toml`: Project configuration
- `langgraph.json`: LangGraph configuration

## Development Notes

- The agent uses Ollama for LLM capabilities (configured in `agent.py`)
- Make sure Ollama is running and accessible at `http://127.0.0.1:11434`
- The fallback logic has been removed from `agent.py` - the agent now relies directly on the LLM

## Troubleshooting

If you encounter issues:
1. Check that Ollama is running
2. Verify port 2024 is available
3. Ensure all dependencies are installed (`uv sync`)
4. Restart the development server if changes are made
