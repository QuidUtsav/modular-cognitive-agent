import streamlit as st
import time
import random

# --- 1. Import ALL your Jarvis Modules ---
from jarvis.core.reasoning import decide_strategy
from jarvis.retrieval.rag import rag_model
# Don't forget these imports for the Chat logic!
from jarvis.core.intent import handle_social_conversation, SOCIAL_ACT_RESPONSES

# --- 2. Page Config ---
st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")

st.title("🤖 Jarvis Assistant")
st.caption("Week 2 Build: Modular RAG & Reasoning Engine")

# --- 3. Initialize Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 4. The Main Loop ---
if prompt := st.chat_input("What is on your mind?"):
    
    # Show User Message
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Jarvis Thinks
    with st.spinner("Thinking..."):
        
        # A. Decide Strategy
        strategy = decide_strategy(prompt)
        
        # B. Debug Sidebar
        with st.sidebar:
            st.write("### 🧠 Debug Brain")
            st.info(f"Strategy: **{strategy}**")
            # If you want to see the intent in the sidebar too:
            if strategy == "chat":
                 st.caption("Mode: Social or Identity")
        
        # --- C. The FIXED Logic (Same as your Terminal) ---
        response = ""
        
        if strategy == "chat":
            # 1. Try Social Greeting first (Fast)
            social_intent = handle_social_conversation(prompt.lower())
            
            if social_intent and social_intent in SOCIAL_ACT_RESPONSES:
                response = random.choice(SOCIAL_ACT_RESPONSES[social_intent])
            else:
                # 2. If not social, it's an Identity question (Slow)
                # Ensure you have 'system_identity.txt' in your folder!
                response = rag_model("system_identity.txt", prompt)

        elif strategy in ["needs_retrieval", "needs_reasoning", "direct_answer"]:
            # Standard RAG
            response = rag_model("document.txt", prompt)
            
        else:
            response = "I am not sure how to handle that yet."

        # Simulate typing speed
        time.sleep(0.5)

    # Show Assistant Message
    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})