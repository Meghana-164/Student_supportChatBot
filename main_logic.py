from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# === Model Setup ===
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)  # Use -1 for CPU

# === Embedding + FAISS DB ===
embedder = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
documents = []
metadatas = []

# === Web Scraping ===
def scrape_text_from_url(url, max_paragraphs=5):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs[:max_paragraphs]])
        return text
    except Exception as e:
        return f"Failed to scrape: {e}"

def add_to_vector_db(text, source):
    embedding = embedder.encode([text])[0]
    documents.append(text)
    metadatas.append({"source": source})
    index.add(np.array([embedding]))

# === RAG Answer Generator ===
def generate_answer(user_query):
    links = list(search(user_query, num_results=3))

    for url in links:
        content = scrape_text_from_url(url)
        if content and "Failed to scrape" not in content:
            add_to_vector_db(content, url)

    query_vec = embedder.encode([user_query])[0]
    D, I = index.search(np.array([query_vec]), k=2)

    if len(I[0]) == 0:
        return "Sorry, I couldn't find relevant information."

    context = "\n\n".join([documents[i] for i in I[0]])

    prompt = f"Based on the following, answer the question clearly.\n\nContext:\n{context}\n\nQuestion: {user_query}\nAnswer:"
    response = llm_pipeline(prompt, max_new_tokens=600, do_sample=True, temperature=0.7)[0]["generated_text"]

    if "Answer:" in response:
        answer_part = response.split("Answer:")[1]
        clean_answer = answer_part.split("Question:")[0].strip()
    else:
        clean_answer = response.strip()

    return clean_answer
