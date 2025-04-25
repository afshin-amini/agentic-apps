import streamlit as st

# Set page config FIRST
st.set_page_config(page_title="Multi-Agent Assistant", layout="wide")

# === Sidebar Settings ===
st.sidebar.title("⚙️ Settings")
llm_choice = st.sidebar.selectbox(
    "Choose LLM Source", ["OpenAI API", "Ollama Local Model"]
)

# === LLM Selection ===
llm = None

if llm_choice == "OpenAI API":
    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI(temperature=0)
    st.sidebar.success("Using OpenAI (cloud)")

elif llm_choice == "Ollama Local Model":
    from langchain.llms import Ollama

    model_name = st.sidebar.text_input("Ollama Model Name", value="mistral")
    llm = Ollama(model=model_name)
    st.sidebar.success(f"Using Ollama Model: {model_name}")

# === Import your common agent ===
from agents import paper_summary_agent  # A *unified* agent that accepts llm

# === Streamlit App ===
st.title("🤖 Multi-Agent Assistant")

agent_choice = st.sidebar.selectbox("Choose an Agent", ["Paper Summarizer"])

if agent_choice == "Paper Summarizer":
    paper_summary_agent.run(llm)  # << Pass the LLM object here
