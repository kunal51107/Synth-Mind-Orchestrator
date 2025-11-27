# 🧠 Synth-Mind AI: Multi-Model Research Engine

A tiered AI research assistant that combines multiple language models to conduct intelligent web research, analysis, and report generation.

## 🌟 Features

- **Multi-Agent Architecture**: Specialized AI agents working in concert
- **Web Search Integration**: Real-time data gathering via Serper API
- **Tiered Intelligence**: 
  - 70B model for deep analysis
  - 8B model for efficient formatting
- **Professional Reports**: Auto-generated Markdown reports
- **Streamlit UI**: Clean, intuitive interface

## 🏗️ Architecture

```
┌─────────────┐
│   Scout     │ → Serper API (Google Search)
└──────┬──────┘
       ↓
┌─────────────┐
│ Strategist  │ → Llama 3.3 70B (Deep Analysis)
└──────┬──────┘
       ↓
┌─────────────┐
│   Editor    │ → Llama 3.1 8B (Report Formatting)
└──────┬──────┘
       ↓
   Final Report
```

### Agent Roles

1. **Scout**: Searches the web for current information on the topic
2. **Strategist**: Analyzes data to identify trends, opportunities, and risks
3. **Editor**: Transforms analysis into polished, structured reports

## Quick Start

### Prerequisites

- Python 3.8+
- GROQ API key ([Get one here](https://console.groq.com))
- Serper API key ([Get one here](https://serper.dev))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/synth-mind-ai.git
cd synth-mind-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

4. Run the application:
```bash
streamlit run app.py
```

## 📦 Dependencies

```
streamlit
langchain
langchain-groq
langchain-community
python-dotenv
google-search-results
```
## Usage

1. Enter a research topic (e.g., "Quantum Computing in Finance")
2. Click "Start Research Agent"
3. Watch the AI agents collaborate in real-time
4. Review the generated report with:
   - Executive Summary
   - Market Opportunities
   - Technical/Market Risks

## Use Cases

- **Market Research**: Analyze emerging tech trends
- **Competitive Intelligence**: Track industry developments
- **Investment Analysis**: Identify opportunities and risks
- **Technology Assessment**: Evaluate new technologies

## Configuration

The app uses a tiered model approach optimized for cost and performance:

- **Llama 3.3 70B**: Complex reasoning and analysis
- **Llama 3.1 8B**: Fast formatting and text generation

You can modify model selection in the `init_agents()` function.

## 🐛 Troubleshooting

**Missing API Keys Error**
- Ensure `.env` file exists in the root directory
- Verify both `GROQ_API_KEY` and `SERPER_API_KEY` are set

**Search Fails**
- Check Serper API quota and validity
- Verify internet connection

**LLM Errors**
- Confirm GROQ API key is valid
- Check model availability on GROQ platform

## Acknowledgments

- [GROQ](https://groq.com) for LLM inference
- [Serper](https://serper.dev) for search API
- [LangChain](https://langchain.com) for LLM orchestration
- [Streamlit](https://streamlit.io) for the UI framework

