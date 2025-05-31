# 🎓 Student Support Chatbot

This is an AI-powered **Student Support Chatbot** that assists students with academic queries by combining **web scraping**, **sentence embedding**, **vector search (FAISS)**, and **LLM-based text generation** using **TinyLlama**.

---

## Features

-  **Real-time web search and scraping** of academic content.  
-  **Retrieval-Augmented Generation (RAG)** using FAISS and `sentence-transformers`.  
-  Human-like responses using **TinyLlama-1.1B-Chat-v1.0** for inference.  
-  Clean and easy-to-use **Streamlit** user interface.  

---

##  Project Structure

```
student_chatbot/
│
├── main_logic.py         # Core RAG + generation logic
├── UI.py                 # Streamlit frontend
├── requirements.txt      # Required dependencies with versions
└── README.md             # You're reading this file
└── Studentsupport.ipnb   # Just for reference (not used for running,standard version is the main_logic.py file )
```

---

## Tech Stack

- Python 3.12.2 
- Transformers (TinyLlama)  
- FAISS  
- Sentence-Transformers  
- Streamlit (UI)  

---

##  Python Version

```bash
Python 3.12.2
```

---

##  Installation & Setup

1. **Clone or Download** the project.

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run UI.py
   ```
4. To enable GPU usage, change device=-1 to device=0 in main_logic.py.

---

##  How It Works (Detailed Explanation)

### 1.  Web Scraping

Uses `requests` and `BeautifulSoup` to fetch and clean content from the top 3 Google search results.

### 2.  Sentence Embeddings + FAISS

Embeds text with `all-MiniLM-L6-v2` and uses FAISS for similarity search.

### 3.  Retrieval-Augmented Generation (RAG)

Combines query-relevant content into a prompt and sends it to TinyLlama for answer generation.

### 4.  Prompt Handling and Answer Extraction

Extracts the "Answer:" section from the generated text.

### 5.  User Interface

Streamlit UI to ask questions, get answers, and show styled results.

---



##  Dependencies

Key libraries:

- `transformers`
- `sentence-transformers`
- `faiss-cpu`
- `beautifulsoup4`
- `requests`
- `googlesearch-python`
- `streamlit`

---

## Notes

- `max_new_tokens=600` is set for long answers.  
- If responses are trimmed, try rephrasing your question.
---
