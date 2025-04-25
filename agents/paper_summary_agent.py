import os
import fitz  # PyMuPDF
import streamlit as st
import docx
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# === Load environment variables ===
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# === Initialize LLM ===
llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# === Streamlit App ===
st.set_page_config(page_title="📝 Paper Summary Agent", layout="wide")
st.title("📄 Paper Summary Generator")

uploaded_files = st.file_uploader(
    "Upload PDF papers", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    summaries = []
    for uploaded_file in uploaded_files:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = "\n".join(page.get_text() for page in doc)

        prompt = PromptTemplate(
            input_variables=["content"],
            template="""
You are an expert at reading and summarizing scientific papers.
Given the following full text of a paper, extract the following:
- Paper Title
- Authors
- Year
- Summary
- Methodology
- Results
- Conclusion and Future Work

Respond strictly in this format:
Title: <text>
Authors: <text>
Year: <text>
Summary: <text>
Methodology: <text>
Results: <text>
Conclusion and Future Work: <text>

Paper Text:
{content}
""",
        )

        formatted_prompt = prompt.format(
            content=text[:12000]
        )  # Limit to first 12000 chars to avoid token limits
        response = llm.predict(formatted_prompt)
        summaries.append(response)

    # === Create Word Document ===
    doc = docx.Document()
    doc.add_heading("Paper Summaries", level=0)

    for idx, summary in enumerate(summaries, 1):
        doc.add_heading(f"Paper {idx}", level=1)
        for line in summary.split("\n"):
            if line.strip():
                if any(section in line for section in ["Title:", "Authors:", "Year:"]):
                    doc.add_heading(line.strip(), level=2)
                else:
                    doc.add_paragraph(line.strip())

    output_path = "paper_summaries.docx"
    doc.save(output_path)

    with open(output_path, "rb") as f:
        st.download_button(
            label="Download Summaries Word Document",
            data=f,
            file_name="paper_summaries.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
