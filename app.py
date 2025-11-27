import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import GoogleSerperAPIWrapper

# Page Config
st.set_page_config(page_title="Synth-Mind AI", page_icon="🧠", layout="wide")

# Custom CSS for a professional look
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .main-header {
        font-size: 2.5rem; 
        color: #1E1E1E;
    }
</style>
""", unsafe_allow_html=True)

# --- SETUP ---
load_dotenv()

# Verify Keys Function
def validate_keys():
    if not os.getenv("GROQ_API_KEY") or not os.getenv("SERPER_API_KEY"):
        st.error("❌ Missing API Keys in .env file. Please add GROQ_API_KEY and SERPER_API_KEY.")
        st.stop()

validate_keys()

# --- INITIALIZE AGENTS (Cached for performance) ---
@st.cache_resource
def init_agents():
    # Tool
    search = GoogleSerperAPIWrapper()
    
    # Big Brain (Logic)
    strategist = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.5
    )
    
    # Fast Brain (Format)
    editor = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3
    )
    
    return search, strategist, editor

search_tool, llm_strategist, llm_editor = init_agents()

# --- PROMPTS ---
strategist_prompt = ChatPromptTemplate.from_template(
    """
    You are a Senior Tech Analyst. Analyze the following data.
    RAW DATA: {raw_data}
    TOPIC: {topic}
    Identify:
    1. The "Big Picture" Trend.
    2. A specific market opportunity.
    3. A critical technical or market risk.
    """
)

editor_prompt = ChatPromptTemplate.from_template(
    """
    You are a Tech Journalist. Turn this analysis into a clean Markdown report.
    Structure:
    # 📑 {topic} Report
    ## 🧐 Executive Summary
    ## 🚀 The Opportunity
    ## ⚠️ The Risks
    ANALYSIS: {analysis}
    """
)

# --- UI LAYOUT ---
st.title("🧠 Synth-Mind: Multi-Model Research Engine")
st.markdown("### Powered by Llama 3.3 (70B) & Llama 3.1 (8B)")

with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("Architecture: Tiered Logic")
    st.markdown("- **Scout:** Serper Dev (Google)")
    st.markdown("- **Strategist:** Llama 3.3 70B")
    st.markdown("- **Editor:** Llama 3.1 8B")

topic = st.text_input("Enter a topic to research:", placeholder="e.g., Quantum Computing in Finance")
run_btn = st.button("🚀 Start Research Agent")

if run_btn and topic:
    report_area = st.empty()
    
    with st.status("🤖 AI Agents at work...", expanded=True) as status:
        
        # Step 1: Search
        st.write("🔎 **Scout:** Searching the web...")
        try:
            raw_data = search_tool.run(f"latest news trends {topic} current year")
            st.write("✅ Data gathered.")
        except Exception as e:
            st.error(f"Search failed: {e}")
            st.stop()

        # Step 2: Analyze
        st.write("🧠 **Strategist:** Analyzing patterns (Llama 70B)...")
        chain_one = strategist_prompt | llm_strategist
        analysis_result = chain_one.invoke({"raw_data": raw_data, "topic": topic})
        st.write("✅ Analysis complete.")

        # Step 3: Write
        st.write("✍️ **Editor:** Writing final report (Llama 8B)...")
        chain_two = editor_prompt | llm_editor
        final_report = chain_two.invoke({"analysis": analysis_result.content, "topic": topic})
        st.write("✅ Report generated.")
        
        status.update(label="Research Complete!", state="complete", expanded=False)

    # Display Report
    st.divider()
    st.markdown(final_report.content)