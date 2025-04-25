# 🧠 Multi-Agent Streamlit App

Welcome to the **Multi-Agent Assistant App**!  
This app lets you run different intelligent agents inside one simple Streamlit interface.

✅ Powered by OpenAI (gpt-3.5 / gpt-4)  
✅ Expanding easily — add new agents anytime  
✅ Streamlined for document summarization and future extensions

---

## 📄 Current Available Agent

### 📚 Paper Summary Agent

- Upload one or more scientific papers in **PDF** format.
- The app will:
  - Read each paper
  - Summarize key sections:
    - Title
    - Authors
    - Year
    - Summary
    - Methodology
    - Results
    - Conclusion and Future Work
- Generates a **Microsoft Word document (.docx)** you can download.

---

## 🚀 How to Use the App

### 1. Install the Requirements

Make sure you have **Python 3.9+** installed.

Then install required packages:

```bash
pip install -r requirements.txt
```bash

## Create a .env file (copy from .env.example) and add your OpenAI key:
OPENAI_API_KEY=your-real-api-key-here

## Start the App
streamlit run streamlit_app.py
