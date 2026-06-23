
# 🌱 GreenCampus AI

### Intelligent Sustainability Knowledge Assistant

GreenCampus AI is an AI-powered sustainability knowledge assistant developed as part of the IBM SkillsBuild + 1M1B AI & Sustainability Virtual Internship.

The system enables students, faculty, and administrators to quickly access sustainability-related information through a conversational interface. Instead of manually searching through multiple documents, users can ask questions in natural language and receive relevant information from a verified sustainability knowledge base.

---

## 🌍 Sustainable Development Goals (SDGs)

This project primarily supports:

- SDG 11 – Sustainable Cities and Communities
- SDG 12 – Responsible Consumption and Production
- SDG 13 – Climate Action

By improving access to sustainability knowledge, GreenCampus AI encourages environmentally responsible practices across educational institutions.

---

## 🚀 Live Demo

🔗 [https://greencampus-ai-demo.streamlit.app/](https://greencampus-ai-3ownmhea8jdzwotdsfqe8o.streamlit.app/)

> If the application is inactive, please wait a few seconds while Streamlit initializes the service.

---

## 📖 Project Overview

Many sustainability guidelines are distributed across reports, notices, and policy documents, making information difficult to access quickly.

GreenCampus AI addresses this challenge by providing:

- Instant access to sustainability information
- Natural language question answering
- Source-based knowledge retrieval
- Improved awareness of sustainability practices

---

## ⚙️ How It Works

1. User submits a sustainability-related question.
2. The question is converted into an embedding using Sentence Transformers.
3. FAISS performs semantic similarity search.
4. The most relevant knowledge chunk is retrieved.
5. The response is displayed along with its source document.

---

## ✨ Key Features

### 📄 Verified Knowledge Retrieval
Responses are generated from verified sustainability documents.

### 🔍 Semantic Search
Uses vector similarity search to identify the most relevant information.

### 📚 Source Transparency
Displays the originating source file for every response.

### 🛡️ Domain-Specific Responses
Designed specifically for sustainability-related topics.

### 🚫 Out-of-Domain Query Handling
Politely informs users when information is unavailable in the knowledge base.

---

## 🛠 Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Embeddings | Sentence Transformers |
| Vector Search | FAISS |
| Language | Python |
| Knowledge Base | Sustainability Text Documents |

---

## 📂 Knowledge Base Topics

The system currently supports:

- Waste Management
- Water Conservation
- Energy Conservation
- Climate Action
- Sustainable Transportation
- Sustainable Campus Practices
- Sustainable Development Goals (SDGs)

---

## 📁 Project Structure

```text
GreenCampus-AI/
│
├── Data/
│   ├── waste_management.txt
│   ├── water_conservation.txt
│   ├── energy_conservation.txt
│   ├── climate_action.txt
│   ├── sustainable_transport.txt
│   ├── sustainable_campus.txt
│   └── sdg_overview.txt
│
├── app.py
├── requirements.txt
└── README.md
````
---

## 🌱 Expected Impact

* Faster access to sustainability information
* Improved environmental awareness
* Better engagement with campus sustainability initiatives
* Support for SDG-focused educational activities

---

## 👨‍💻 Developed By

**Aravind Bandi**
B.Tech – Computer Science and Engineering (AI & ML)
Guru Nanak Institute of Technology

Developed as part of the **IBM SkillsBuild + 1M1B AI & Sustainability Virtual Internship (2026)**.


