import streamlit as st
from agents import paper_summary_agent

st.set_page_config(page_title="Multi-Agent App", layout="wide")
st.title("🤖 Multi-Agent Assistant")

agent_choice = st.sidebar.selectbox("Choose an Agent", ["Paper Summarizer"])

if agent_choice == "Paper Summarizer":
    paper_summary_agent.run()
