# Advanced Research Agent

Advanced Research Agent is an AI-powered tool designed to automate the process of researching developer tools, frameworks, and technologies. It leverages LLMs and web scraping to extract, analyze, and recommend the best solutions for your development needs.

## 🚀 Advanced Features

- **Automated Web Search & Scraping**
  - Integrates with Firecrawl for deep web search and content extraction
  - Scrapes articles, documentation, and official sites for up-to-date information
- **Intelligent Tool Extraction**
  - Uses LLMs to extract tool, library, and service names from unstructured text
  - Identifies open-source and commercial alternatives
- **Comparative Analysis**
  - Analyzes features, tech stack, pricing, and integration capabilities
  - Summarizes pros/cons and use cases for each tool
- **Customizable Prompt Engineering**
  - Modular prompt templates for different research tasks
  - Easily extend or adapt for new domains
- **Multi-Step Workflow Orchestration**
  - State machine-based workflow (LangGraph) for robust, extensible research pipelines
  - Each step is modular and testable
- **LLM-Powered Recommendations**
  - Generates developer-focused recommendations based on extracted data
  - Highlights cost, scalability, and integration trade-offs
- **Structured Output**
  - Returns results as Pydantic models for easy downstream use
  - Ready for integration with UIs, APIs, or further automation
- **CLI Interface**
  - Simple command-line interface for interactive research
- **Extensible Architecture**
  - Add new research steps, data sources, or LLMs with minimal changes

## 🧩 Extending the Agent
- Add new workflow steps by defining methods in `workflow.py` and registering them in the state graph.
- Integrate additional LLMs or APIs by updating the `llm` attribute in the `Workflow` class.
- Plug in new data sources (APIs, databases) by extending `firecrawl.py`.

## ⚙️ Configuration & Customization
- **Prompts:**
  - Edit `src/prompts.py` to customize LLM prompt templates for extraction, analysis, or recommendations.
- **Workflow:**
  - Modify or extend `src/workflow.py` to add new research steps or change the pipeline.
- **Web Scraping:**
  - Adjust `src/firecrawl.py` to change scraping logic or integrate new data sources.
- **Models:**
  - Update `src/models.py` to add new fields or output formats.

## Features
- Automated web search and scraping for technology comparisons
- Extraction of tool and service names from articles
- In-depth analysis and recommendations using LLMs
- Modular workflow for easy extension

## Project Structure
```
advanced-agent/
├── main.py                # Entry point for the agent
├── pyproject.toml         # Project dependencies and configuration
├── README.md              # Project documentation
├── src/
│   ├── __init__.py
│   ├── firecrawl.py       # Web scraping and search integration
│   ├── models.py          # Data models (Pydantic)
│   ├── prompts.py         # Prompt templates for LLMs
│   └── workflow.py        # Main workflow logic
└── ...
simple-agent/
└── ...
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ramzi-bouzaiene/Advanced-Research-Agent.git
   cd Advanced-Research-Agent/advanced-agent
   ```
2. Create and activate a Python virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   # or if using poetry:
   poetry install
   ```

## Usage
Run the main agent:
```sh
python main.py
```
You will be prompted to enter a developer tools query (e.g., `firebase`, `react`). The agent will search, extract, and analyze relevant tools and provide recommendations.

## Configuration
- Prompts and workflow logic can be customized in `src/prompts.py` and `src/workflow.py`.
- Web scraping/search logic is in `src/firecrawl.py`.
