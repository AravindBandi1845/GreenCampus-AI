import os
import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="GreenCampus AI",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 GreenCampus AI")
st.subheader("Intelligent Sustainability Knowledge Assistant")

# ==========================================
# FIND DATA FOLDER
# ==========================================

data_folder = "data"

if not os.path.exists(data_folder):
    data_folder = "Data"

if not os.path.exists(data_folder):
    st.error("⚠️ Data folder not found! Create a folder named 'data'.")
    st.stop()

# ==========================================
# TEXT CHUNKING
# ==========================================

def split_text_into_chunks(text, chunk_size=100, chunk_overlap=20):
    chunks = []
    words = text.split()
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - chunk_overlap

    return chunks

# ==========================================
# LOAD KNOWLEDGE BASE
# ==========================================

def load_knowledge_base(folder):
    all_chunks = []
    chunk_sources = []

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()

                if text:
                    chunks = split_text_into_chunks(text)

                    for chunk in chunks:
                        all_chunks.append(chunk)
                        chunk_sources.append(file)

    return all_chunks, chunk_sources

documents, sources = load_knowledge_base(data_folder)

if len(documents) == 0:
    st.warning("⚠️ No text files found inside the data folder.")
    st.stop()

# ==========================================
# LOAD MODEL
# ==========================================

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# ==========================================
# BUILD FAISS INDEX
# ==========================================

@st.cache_resource
def build_index(_documents):
    embeddings = model.encode(
        _documents,
        show_progress_bar=False
    )

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index

index = build_index(documents)

# ==========================================
# CHAT HISTORY
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! I am GreenCampus AI 🌱. "
                "Ask me about waste management, water conservation, "
                "energy conservation, climate action, sustainable transportation, "
                "sustainable campuses, or SDGs."
            )
        }
    ]

# Display old messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ==========================================
# USER INPUT
# ==========================================

query = st.chat_input("Ask a sustainability question...")

if query:

    with st.chat_message("user"):
        st.write(query)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Create query embedding

    query_embedding = model.encode(
        [query],
        show_progress_bar=False
    )

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    )

    # Retrieve best matching chunk

    distances, indices = index.search(
        query_embedding,
        k=1
    )

    DISTANCE_THRESHOLD = 1.3

    response = None
    source_text = "Knowledge Base"

    best_distance = distances[0][0]
    best_index = indices[0][0]

    if best_index != -1 and best_distance <= DISTANCE_THRESHOLD:
        response = documents[best_index]
        source_text = sources[best_index]
    else:
        response = (
            "I could not find relevant information in the sustainability knowledge base.\n\n"
            "Please ask about:\n"
            "- Waste Management\n"
            "- Water Conservation\n"
            "- Energy Conservation\n"
            "- Climate Action\n"
            "- Sustainable Transportation\n"
            "- Sustainable Campuses\n"
            "- Sustainable Development Goals (SDGs)"
        )

    # Display response

    with st.chat_message("assistant"):
        st.write(response)
        st.caption(f"📚 Source File: {source_text}")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
