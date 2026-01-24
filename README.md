🧠 Jarvis: Modular RAG Assistant (Week 2)


A local, modular Personal AI Assistant built with Python, Hugging Face, and Scikit-Learn.

    Status: ✅ Week 2 Complete (RAG & Reasoning) Focus: Architecture, Local Retrieval, and Hallucination Control.

Unlike simple API wrappers, Jarvis is designed as a cognitive system. It doesn't just guess; it reasons about how to answer a question—whether to chat casually, use internal logic, or retrieve facts from a local knowledge base (RAG).
🚀 Week 2: The "Brain" Upgrade

In Week 2, the system evolved from a simple intent classifier into a Retrieval-Augmented Generation (RAG) pipeline.
Key New Capabilities

    📚 Local RAG System: Can read, chunk, and "learn" from local documents (document.txt) without uploading data to the cloud.

    🧠 Decision Engine: A dedicated reasoning.py module that decides strategy (chat vs. retrieval vs. direct_answer) before acting.

    🛡️ Hallucination Guardrails: If the retrieval score is low (< 0.3), Jarvis explicitly admits "I don't know" rather than making things up.

    🏗️ Modular Architecture: Refactored from a single script into a scalable package structure (core, retrieval, memory).

🛠️ System Architecture

The project follows a "Manager-Worker" pattern to separate concerns.

graph TD
    A[User Input] --> B[app.py (Manager)]
    B --> C{Reasoning Engine}
    C -- "Hello" --> D[Chat Module]
    C -- "Explain X" --> E[RAG Pipeline]
    
    subgraph "RAG Pipeline"
    E --> F[Vector Search (TF-IDF/Cosine)]
    F --> G[Retrieve Context]
    G --> H[Generator (Flan-T5)]
    end
    
    D --> I[Output]
    H --> I

📂 File Structure
    jarvis/
    ├── app.py                 # The Main Entry Point (The Manager)
    ├── data/
    │   └── document.txt       # Local Knowledge Base
    ├── jarvis/
    │   ├── core/
    │   │   ├── reasoning.py   # Decides Strategy (Chat vs. RAG)
    │   │   ├── generation.py  # Wraps LLM (Flan-T5)
    │   │   └── embeddings.py  # Handles Chunking & Vector Encoding
    │   └── retrieval/
    │       └── rag.py         # Combines Search + Generation

🤖 Tech Stack & Models
Component,Technology / Model,Role
Generator,google/flan-t5-base,Generates natural language answers from context.
Embeddings,all-MiniLM-L6-v2,Converts text into vector numbers for search.
Similarity,Cosine Similarity,Math used to find the best matching paragraph.
Framework,PyTorch & Transformers,The backbone for running models locally.

⚡ How It Works (The Logic Flow)

    Input Normalization: User text is cleaned (lowercased, special characters removed).

    Strategy Decision:

        If the user asks "How are you?", the Chat Strategy handles it instantly.

        If the user asks "Based on the document...", the Retrieval Strategy kicks in.

    Retrieval (If needed):

        The system loads document.txt, splits it into chunks, and caches the embeddings.

        It finds the top 3 chunks most similar to the question.

    Generation:

        The LLM receives a prompt: "Answer using ONLY this context..."

        If context is missing or irrelevant, it returns a fallback response.

💻 Usage
1. Setup

Ensure you have the required libraries installed:
    pip install transformers torch scikit-learn sentence-transformers

This is a huge milestone! You’ve moved from a simple text classifier to a full Retrieval-Augmented Generation (RAG) system with a modular architecture. That is a serious jump in complexity.

Here is a professional, high-impact README.md tailored for your Week 2 completion. It highlights your move to "Systems Engineering" and the new capabilities like RAG, Reasoning, and Modular Design.

You can copy-paste this directly into your README.md file.
🧠 Jarvis: Modular RAG Assistant (Week 2)

A local, modular Personal AI Assistant built with Python, Hugging Face, and Scikit-Learn.

    Status: ✅ Week 2 Complete (RAG & Reasoning) Focus: Architecture, Local Retrieval, and Hallucination Control.

Unlike simple API wrappers, Jarvis is designed as a cognitive system. It doesn't just guess; it reasons about how to answer a question—whether to chat casually, use internal logic, or retrieve facts from a local knowledge base (RAG).
🚀 Week 2: The "Brain" Upgrade

In Week 2, the system evolved from a simple intent classifier into a Retrieval-Augmented Generation (RAG) pipeline.
Key New Capabilities

    📚 Local RAG System: Can read, chunk, and "learn" from local documents (document.txt) without uploading data to the cloud.

    🧠 Decision Engine: A dedicated reasoning.py module that decides strategy (chat vs. retrieval vs. direct_answer) before acting.

    🛡️ Hallucination Guardrails: If the retrieval score is low (< 0.3), Jarvis explicitly admits "I don't know" rather than making things up.

    🏗️ Modular Architecture: Refactored from a single script into a scalable package structure (core, retrieval, memory).

🛠️ System Architecture

The project follows a "Manager-Worker" pattern to separate concerns.
Code snippet

graph TD
    A[User Input] --> B[app.py (Manager)]
    B --> C{Reasoning Engine}
    C -- "Hello" --> D[Chat Module]
    C -- "Explain X" --> E[RAG Pipeline]
    
    subgraph "RAG Pipeline"
    E --> F[Vector Search (TF-IDF/Cosine)]
    F --> G[Retrieve Context]
    G --> H[Generator (Flan-T5)]
    end
    
    D --> I[Output]
    H --> I

📂 File Structure
Plaintext

jarvis/
├── app.py                 # The Main Entry Point (The Manager)
├── data/
│   └── document.txt       # Local Knowledge Base
├── jarvis/
│   ├── core/
│   │   ├── reasoning.py   # Decides Strategy (Chat vs. RAG)
│   │   ├── generation.py  # Wraps LLM (Flan-T5)
│   │   └── embeddings.py  # Handles Chunking & Vector Encoding
│   └── retrieval/
│       └── rag.py         # Combines Search + Generation

🤖 Tech Stack & Models
Component	Technology / Model	Role
Generator	google/flan-t5-base	Generates natural language answers from context.
Embeddings	all-MiniLM-L6-v2	Converts text into vector numbers for search.
Similarity	Cosine Similarity	Math used to find the best matching paragraph.
Framework	PyTorch & Transformers	The backbone for running models locally.
⚡ How It Works (The Logic Flow)

    Input Normalization: User text is cleaned (lowercased, special characters removed).

    Strategy Decision:

        If the user asks "How are you?", the Chat Strategy handles it instantly.

        If the user asks "Based on the document...", the Retrieval Strategy kicks in.

    Retrieval (If needed):

        The system loads document.txt, splits it into chunks, and caches the embeddings.

        It finds the top 3 chunks most similar to the question.

    Generation:

        The LLM receives a prompt: "Answer using ONLY this context..."

        If context is missing or irrelevant, it returns a fallback response.

💻 Usage
1. Setup

Ensure you have the required libraries installed:

    pip install transformers torch scikit-learn sentence-transformers

2. Run Jarvis

Execute the main application:

    python app.py

3. Example Interaction

You: Who are you?
[DEBUG] strategy=chat
Jarvis: I am just here to help you 🙂

You: How do I reset the device?
[DEBUG] strategy=needs_retrieval
[DEBUG] score=0.85 chunk_id=4
Jarvis: To reset the device, hold the power button for 10 seconds.

🚧 Current Limitations

    Short-Term Memory: Jarvis handles one question at a time. It doesn't yet remember "What did I just ask?".

    Single Document: Currently optimized for reading one text file at a time.

    Speed: First run is slow due to model downloading/loading.

🛣️ Roadmap: Week 3

    🧠 Conversation History: Implement memory so Jarvis remembers the context of the chat.

    🛠️ Tool Use: Allow Jarvis to perform actions (e.g., "Write this to a file" or "Calculate this").

    ⚡ Speed Optimization: Implement better caching to speed up repeated queries.

👨‍💻 About the Author

This project is a journey into Applied AI Engineering—moving beyond API calls to building deterministic, controllable AI systems from scratch.