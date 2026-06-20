# GreenCampus AI 🌿🤖

An intelligent, lightweight Retrieval-Augmented Generation (RAG) assistant designed to provide accurate insights on campus sustainability practices, energy conservation, waste management, and SDG tracking.

---

## 🚀 Key Features & Architecture
Unlike heavy, abstract frameworks, this system is built using a **custom, LangChain-free RAG pipeline**. This approach prioritizes minimal execution overhead, absolute transparency over data flow, and precise retrieval control.

*   **Semantic Data Ingestion:** Systematically processes unstructured campus guidelines across specialized sub-domains (`Data/`).
*   **Vector Embeddings:** Uses `sentence-transformers` to map campus intelligence into high-dimensional vector spaces.
*   **Localized Context Matching:** Implements native similarity metrics to fetch the exact context needed for user prompts, preventing AI hallucinations.
*   **Streamlit Interface:** A responsive, interactive user interface designed for intuitive exploration of sustainability data.

---

## 🛠️ Tech Stack
*   **Core Logic:** Python 3.9+
*   **UI Framework:** Streamlit
*   **Embeddings & Search:** SentenceTransformers, NumPy
*   **Environment Management:** Virtualenv

---

## 📦 Project Structure
```text
IBM_AI/
│
├── app.py                  # Core application entry point & RAG pipeline
├── .gitignore              # Prevents staging system dependencies & venv bloat
├── README.md               # Project documentation and architecture guide
├── LICENSE                 # Repository license terms
└── Data/                   # Domain-specific knowledge base
    ├── energy_conservation.txt
    ├── sdg_overview.txt
    ├── sustainable_transport.txt
    ├── waste_management.txt
    └── water_conservation.txt