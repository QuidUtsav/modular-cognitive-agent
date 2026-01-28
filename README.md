# 🧠 Modular Cognitive Agent

![Python](https://img.shields.io/badge/Python-3.14.2%2B-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-ee4c2c?style=for-the-badge&logo=pytorch)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?style=for-the-badge&logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A local, deterministic AI system designed for **controllable reasoning** and **retrieval-augmented generation (RAG)**.

Unlike standard chatbot wrappers that rely solely on probabilistic generation, this system uses a "Router-Controller" architecture to decide *how* to answer before generating text—switching dynamically between casual conversation, internal knowledge retrieval, and real-time web search.

---

## 🚀 Key Capabilities

### 1. 🧠 Semantic Routing (The "Brain")
The system doesn't just guess; it classifies intent.
- **Chat Mode:** Handles greetings and small talk instantly.
- **RAG Mode:** Detects when a user asks about specific stored documents.
- **Web Mode:** (In Progress) Detects questions requiring real-time data.

### 2. 📚 Local RAG Pipeline
- **Zero-Cloud Dependency:** Chunks, embeds, and retrieves knowledge locally using `sentence-transformers`.
- **Hallucination Guardrails:** If retrieval confidence is low (< 0.3), the system explicitly admits ignorance rather than fabricating facts.

### 3. 🛡️ Modular Architecture
- **Decoupled Logic:** The reasoning engine is separate from the generation engine.
- **Scalable Tools:** New capabilities (e.g., Calculator, OS Control) can be added as isolated modules without breaking the core loop.

---

## 🛠️ System Architecture

The project follows a **Manager-Worker** pattern. The `Controller` acts as the central brain, delegating tasks to specialized workers.

```mermaid
graph TD
    User[User Input] --> Controller[Controller (Manager)]
    
    subgraph "Decision Layer"
    Controller --> Router{Semantic Router}
    end
    
    subgraph "Execution Layer"
    Router -- "Casual Chat" --> Chat[Chat Module]
    Router -- "Specific Fact" --> RAG[RAG Pipeline]
    Router -- "Live Info" --> Web[Web Search Tool]
    end
    
    subgraph "Data Layer"
    RAG --> VectorDB[(Local Vector Store)]
    Web --> Internet((Internet))
    end
    
    Chat --> Response
    RAG --> Response
    Web --> Response
    Response --> User

📂 Project Structure
jarvis/
├── app.py                 # Main Entry Point (CLI Interface)
├── data/
│   ├── document.txt       # Local Knowledge Base (Source of Truth)
│   └── store.json         # Persistent Memory (JSON DB)
├── jarvis/
│   ├── core/
│   │   ├── controller.py  # Orchestrates the flow
│   │   ├── reasoning.py   # Semantic Intent Classification
│   │   └── intent.py      # Hardcoded social rules
│   ├── memory/
│   │   ├── long_term.py   # Manages JSON storage
│   │   └── short_term.py  # Manages active session context
│   ├── retrieval/
│   │   └── rag.py         # Vector Search + Generation Logic
│   └── tools/
│       └── web_search.py  # External API Interface

🤖 Tech Stack
Component,Technology,Role
LLM,google/flan-t5-base,Text Generation (runs locally on CPU).
Embeddings,all-MiniLM-L6-v2,Converts text to vectors for search.
Routing,scikit-learn,Cosine Similarity for intent classification.
Search,DuckDuckGo,Real-time internet access (Headless).

💻 Usage
1. Setup Environment
# Clone the repo
git clone [https://github.com/yourusername/modular-cognitive-agent.git](https://github.com/yourusername/modular-cognitive-agent.git)

# Install dependencies
pip install torch transformers scikit-learn sentence-transformers duckduckgo-search

2. Run the Agent
python app.py

3. Example Interaction
You: Hello!
[DEBUG] Strategy: chat (Confidence: 0.98)
Agent: I'm Jarvis — an AI assistant. I'm still learning about myself.

You: What is in the document?
[DEBUG] Strategy: needs_retrieval (Confidence: 0.85)
[DEBUG] Retrieved Chunk ID: 2
Agent: The document contains security protocols for the server reset procedure.


👨‍💻 Author

Built as a study in Applied AI Engineering—moving beyond API wrappers to build deterministic, controllable systems.