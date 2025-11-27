import os
import sys
from dotenv import load_dotenv

# Import LangChain components
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import GoogleSerperAPIWrapper

# --- 1. SETUP & VALIDATION ---
load_dotenv()

def validate_env():
    """Ensures keys exist before crashing mid-script."""
    # We now only need GROQ and SERPER. Google is removed for stability.
    required_keys = ["GROQ_API_KEY", "SERPER_API_KEY"]
    missing = [key for key in required_keys if not os.getenv(key)]
    if missing:
        print(f"\n❌ CRITICAL ERROR: Missing keys in .env: {', '.join(missing)}")
        print("   Get Serper Key (Free) at: https://serper.dev/")
        print("   Get Groq Key (Free) at: https://console.groq.com/")
        sys.exit(1)

validate_env()

print("🚀 Initializing Synth-Mind (Tiered Llama Architecture)...")

# --- 2. INITIALIZE COMPONENTS ---

# TOOL: Google Search (via Serper)
# Validated: Working perfectly in your previous run.
search_tool = GoogleSerperAPIWrapper()

# MODEL A: The Strategist (High Intelligence)
# We use the massive 70B model for deep thinking.
llm_strategist = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_retries=2
)

# MODEL B: The Editor (High Speed)
# We use the 8B "Instant" model for formatting. It is blazing fast.
llm_editor = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3, # Lower temp for consistent formatting
    max_retries=2
)

# --- 3. DEFINE PROMPTS ---

strategist_prompt = ChatPromptTemplate.from_template(
    """
    You are a Senior Tech Analyst. 
    Analyze the following Google Search data about specific trends.

    RAW DATA:
    {raw_data}

    TOPIC:
    {topic}

    Identify:
    1. The "Big Picture" Trend.
    2. A specific market opportunity.
    3. A critical technical or market risk.
    """
)

editor_prompt = ChatPromptTemplate.from_template(
    """
    You are a Tech Journalist. 
    Turn this analysis into a clean, professional Markdown report.
    
    Structure:
    # 📑 {topic} Report
    ## 🧐 Executive Summary
    ## 🚀 The Opportunity
    ## ⚠️ The Risks
    
    ANALYSIS:
    {analysis}
    """
)

# --- 4. ORCHESTRATION PIPELINE ---

def run_research_pipeline(topic):
    print(f"\n🔎 STEP 1: Googling '{topic}' via Serper API...")
    try:
        raw_data = search_tool.run(f"latest news trends {topic} current year")
        print("   ✅ Data retrieved successfully.")
    except Exception as e:
        print(f"   ❌ Search failed: {e}")
        return

    print("\n🧠 STEP 2: Strategist analyzing data (Llama 3.3 70B)...")
    try:
        chain_one = strategist_prompt | llm_strategist
        analysis_result = chain_one.invoke({"raw_data": raw_data, "topic": topic})
        print("   ✅ Analysis complete.")
    except Exception as e:
        print(f"   ❌ Analysis failed: {e}")
        return

    print("\n✍️ STEP 3: Editor compiling report (Llama 3.1 8B)...")
    try:
        chain_two = editor_prompt | llm_editor
        final_report = chain_two.invoke({"analysis": analysis_result.content, "topic": topic})
        print("   ✅ Report generated.")
    except Exception as e:
        print(f"   ❌ Editing failed: {e}")
        return

    return final_report.content

# --- 5. EXECUTION ---

if __name__ == "__main__":
    user_topic = input("\n💡 Enter a topic to research: ")
    if user_topic:
        report = run_research_pipeline(user_topic)
        if report:
            print("\n\n" + "="*40)
            print("📝 FINAL REPORT")
            print("="*40 + "\n")
            print(report)