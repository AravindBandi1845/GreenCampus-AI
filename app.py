import os
import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="GreenCampus AI",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 GreenCampus AI")
st.subheader("AI-Powered Sustainability Assistant")

# =========================
# FIND DATA FOLDER
# =========================

data_folder = "data"

if not os.path.exists(data_folder):
    data_folder = "Data"

if not os.path.exists(data_folder):
    st.error("⚠️ Folder 'data' or 'Data' not found!")
    st.stop()

# =========================
# LOAD KNOWLEDGE BASE
# =========================

def load_knowledge_base(folder):
    docs = []
    files = []

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()

                if text:
                    docs.append(text)
                    files.append(file)

    return docs, files

documents, filenames = load_knowledge_base(data_folder)

if not documents:
    st.warning("⚠️ No text files found inside the data folder.")
    st.stop()

# =========================
# LOAD EMBEDDING MODEL
# =========================

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# =========================
# BUILD FAISS INDEX
# =========================

@st.cache_resource
def build_index(docs):
    embeddings = model.encode(
        docs,
        show_progress_bar=False
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index

index = build_index(documents)

# =========================
# CHAT HISTORY
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "Hello! I am your GreenCampus Assistant. Ask me anything about sustainability, waste management, water conservation, energy conservation, or SDGs."
        }
    ]

# Display chat history

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# =========================
# USER QUERY
# =========================

query = st.chat_input(
    "Type your sustainability question here..."
)

if query:

    # Show user message

    with st.chat_message("user"):
        st.write(query)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Convert query into embedding

    query_embedding = model.encode(
        [query],
        show_progress_bar=False
    )

    # Retrieve top 2 matching documents

    distances, indices = index.search(
        np.array(query_embedding),
        k=2
    )

    retrieved_text = ""
    source_files = []

    for idx in indices[0]:

        if idx != -1 and idx < len(documents):

            retrieved_text += documents[idx] + " "

            source_files.append(
                filenames[idx]
            )

    # Generate concise response

    sentences = retrieved_text.split(". ")

    relevant_sentences = []

    query_words = query.lower().split()

    for sentence in sentences:

        sentence_lower = sentence.lower()

        if any(
            word in sentence_lower
            for word in query_words
        ):
            relevant_sentences.append(sentence)

    if relevant_sentences:
        response = ". ".join(
            relevant_sentences[:4]
        )
    else:
        response = retrieved_text[:500]

    # Show assistant response

    with st.chat_message("assistant"):
        st.write(response)

        st.caption(
            "📚 Source Files: "
            + ", ".join(source_files)
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )