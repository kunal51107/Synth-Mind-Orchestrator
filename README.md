# 🧠 Synth-Mind Orchestrator

![Python]
![Architecture]
![Groq]
![Streamlit]

**A Production-Grade Multi-Agent Research System using Tiered Intelligence Architecture.**

## Engineering Architecture

This project implements a **Deterministic Chain-of-Thought Pipeline** that optimizes for latency and reasoning depth:

1.  **Data Layer (The Scout):** * **Tool:** `Google Serper API`
    * **Role:** Fetches real-time, non-hallucinated web data.
2.  **Reasoning Layer (The Strategist):** * **Model:** `Llama 3.3 70B` (via Groq)
    * **Role:** Performs deep SWOT analysis and identifies hidden market patterns. We use the 70B parameter model here because reasoning requires high "cognitive" capacity.
3.  **Presentation Layer (The Editor):** * **Model:** `Llama 3.1 8B` (via Groq)
    * **Role:** Synthesizes insights into a clean Markdown report. We use the 8B model here because formatting is a low-complexity task, allowing for sub-second generation speeds.

---

## Tech Stack

* **Orchestration:** LangChain (Python)
* **Inference Engine:** Groq (Llama 3.3 & 3.1)
* **Frontend:** Streamlit
* **Search Tool:** Serper Dev (Google Search API)

---

## Setup & Installation

**1. Clone the Repository**
```bash
git clone [https://github.com/YOUR_USERNAME/Synth-Mind-Orchestrator.git](https://github.com/YOUR_USERNAME/Synth-Mind-Orchestrator.git)
cd Synth-Mind-Orchestrator

python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

GROQ_API_KEY=gsk_...
SERPER_API_KEY=...

streamlit run app.py