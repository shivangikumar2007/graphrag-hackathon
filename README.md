# graphrag-hackathon
an example of # 🚀 GraphRAG vs Traditional RAG vs Basic LLM

A hackathon project demonstrating how GraphRAG powered by TigerGraph improves retrieval quality, speed, scalability, and cost efficiency compared to traditional Retrieval-Augmented Generation (RAG) and standard LLM pipelines.

---

# 📌 Problem Statement

Traditional LLMs hallucinate and traditional RAG systems retrieve unstructured chunks of text, often leading to inaccurate or inefficient answers.

This project demonstrates how GraphRAG can:
- retrieve structured relationships
- reduce token usage
- improve retrieval speed
- provide context-aware reasoning

using a graph database powered by TigerGraph.

---

# 🧠 Project Architecture

User Question
↓
Basic LLM / RAG / GraphRAG Pipeline
↓
TigerGraph retrieves connected entities
↓
Graph-based contextual retrieval
↓
Structured response generation

---

# ⚡ Features

✅ Basic LLM Pipeline  
✅ Traditional RAG Pipeline  
✅ GraphRAG Pipeline  
✅ TigerGraph Integration  
✅ Book Knowledge Graph  
✅ Graph-based Retrieval  
✅ Cost Comparison  
✅ Token Usage Comparison  
✅ Response Time Comparison  
✅ Streamlit Interface  

---

# 🛠️ Tech Stack

- Python
- Streamlit
- TigerGraph
- Pandas
- Transformers
- Sentence Transformers
- Scikit-learn

---

# 📂 Dataset

The dataset contains 80+ books with:
- title
- author
- genre
- context
- summary
- character arcs

The data is transformed into a knowledge graph using TigerGraph.

---

# 🔗 Graph Schema

## Vertex Types
- Book
- Author
- Genre
- Context
- Character

## Edge Types
- written_by
- belongs_to
- has_context
- has_character

---

# 🚀 How to Run

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Import books into TigerGraph

```bash
python import_books.py
```

## 3. Run Streamlit app

```bash
python -m streamlit run app.py
```

---

# 📊 Comparison

| Pipeline | Speed | Cost | Retrieval Quality |
|---|---|---|---|
| Basic LLM | Slow | High | Medium |
| Traditional RAG | Medium | Medium | High |
| GraphRAG | Fast | Low | Very High |

---

# 🧠 Why GraphRAG Wins

- Structured retrieval using graph relationships
- Lower token usage
- Faster contextual retrieval
- Better scalability
- Improved reasoning using connected entities

---

# 🎯 Example Queries

- author of 9 Noovember
- which book of Shakespeare is a tragedy
- fantasy books
- leisure books
- murder mystery books

---

# 👨‍💻 Future Improvements

- Real-time graph traversal
- LLM-enhanced graph reasoning
- Vector embeddings integration
- Recommendation system
- Character relationship visualization

---

# 🏆 Hackathon Project

Built to demonstrate the practical advantages of GraphRAG over traditional retrieval systems using TigerGraph.how graphrag is better with the help of books data
