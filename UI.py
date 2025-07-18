import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re


@st.cache_data
def load_data():
    df = pd.read_csv("qa_data.csv")  
    return df

df = load_data()

model = SentenceTransformer('all-MiniLM-L6-v2')
question_embeddings = model.encode(df['question'].tolist(), convert_to_tensor=True)

# Retrieval function
def get_best_answer(user_question, top_k=1):
    user_embedding = model.encode([user_question], convert_to_tensor=True)
    scores = cosine_similarity(user_embedding, question_embeddings)[0]
    top_idx = np.argsort(scores)[::-1][:top_k]
    return [(df['question'].iloc[i], df['answer'].iloc[i], scores[i]) for i in top_idx]

diseases = ["leukemia", "cancer", "diabetes", "asthma", "flu"]
treatments = ["chemotherapy", "radiation", "transplant", "surgery"]
symptoms = ["fever", "pain", "fatigue", "headache", "cough"]

def basic_entity_recognition(text):
    found = []
    for word in diseases:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            found.append((word, "DISEASE"))
    for word in treatments:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            found.append((word, "TREATMENT"))
    for word in symptoms:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            found.append((word, "SYMPTOM"))
    return found


st.title("🩺 Medical Q&A Chatbot")
user_q = st.text_input("Ask your medical question:")

if user_q:
    results = get_best_answer(user_q)
    match_q, ans, score = results[0]

    st.subheader("🧠 Matched Question:")
    st.write(match_q)
    st.subheader("📋 Answer:")
    st.write(ans)

    st.subheader("🧬 Extracted Entities:")
    entities = basic_entity_recognition(ans)
    if entities:
        for ent, label in entities:
            st.write(f"• {ent} — {label}")
    else:
        st.write("No entities detected.")
