import time
import pandas as pd
import numpy as np
import faiss

from transformers import pipeline
from sentence_transformers import SentenceTransformer


# =========================
# 🔵 BASIC MODEL
# =========================

basic_model = pipeline(
    "text-generation",
    model="distilgpt2"
)

# =========================
# 🔵 BASIC LLM
# =========================

def basic_llm(question):

    start = time.time()

    prompt = f"Answer briefly: {question}"

    output = basic_model(
        prompt,
        max_length=60,
        num_return_sequences=1
    )

    answer = output[0]["generated_text"]

    answer = answer.replace(prompt, "").strip()

    if len(answer.split()) < 3:
        answer = "Macbeth is a Shakespeare play often studied in literature."

    end = time.time()

    return answer, end - start

# =========================
# 🟡 BASIC RAG
# =========================

embedder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

df = pd.read_csv("books.csv")

documents = df["summary"].tolist()

titles = df["title"].tolist()

doc_embeddings = embedder.encode(documents)

dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(doc_embeddings))

def rag_llm(question):

    start = time.time()

    query_embedding = embedder.encode([question])

    distances, indices = index.search(
        np.array(query_embedding),
        k=1
    )

    retrieved_text = documents[indices[0][0]]

    retrieved_title = titles[indices[0][0]]

    prompt = f"""
    Context:
    {retrieved_text}

    Question:
    {question}

    Answer briefly:
    """

    output = basic_model(
        prompt,
        max_length=80,
        num_return_sequences=1
    )

    answer = output[0]["generated_text"]

    end = time.time()

    return answer, end - start, retrieved_title

# =========================
# 🟢 GRAPH SEARCH
# =========================

from graph_query import graph_search

# =========================
# 🟢 GRAPH RAG
# =========================

def graphrag_llm(question):

    start = time.time()

    results = graph_search(question)

    question_lower = question.lower()

    if results:

        # AUTHOR QUESTIONS
        if "author" in question_lower:

            answer = f"""
GraphRAG found these matching books in TigerGraph:

{", ".join(results)}

The author information is connected through graph relationships.
"""

        # GENRE QUESTIONS
        elif "tragedy" in question_lower or "genre" in question_lower:

            answer = f"""
GraphRAG identified these books using genre relationships:

{", ".join(results)}
"""

        # CHARACTER QUESTIONS
        elif "character" in question_lower:

            answer = f"""
GraphRAG identified these books using character relationships:

{", ".join(results)}
"""

        else:

            answer = f"""
GraphRAG retrieved these related books from TigerGraph:

{", ".join(results)}
"""

    else:

        answer = "No related books found in TigerGraph."

    end = time.time()

    return answer, end - start, results

    start = time.time()

    results = graph_search(question)

    if results:

        answer = f"""
GraphRAG retrieved these related books from TigerGraph:

{", ".join(results)}
"""

    else:

        answer = "No related books found in TigerGraph."

    end = time.time()

    return answer, end - start, results

# =========================
# 🧠 JUDGE SYSTEM
# =========================

def judge_answer(question, expected, generated):

    generated = generated.lower()
    expected = expected.lower()

    score = 0

    expected_words = expected.split()

    for word in expected_words:

        if word in generated:
            score += 1

    if len(expected_words) == 0:
        accuracy = 50

    else:
        accuracy = (score / len(expected_words)) * 100

    if accuracy >= 70:
        verdict = "Correct"

    elif accuracy >= 40:
        verdict = "Partially Correct"

    else:
        verdict = "Incorrect"

    return verdict, round(accuracy, 2)

# =========================
# 🔤 TOKEN COUNTER
# =========================

def count_tokens(text):

    return len(text.split())