# --- REPLACEMENT FOR interface.py ---
import streamlit as st
import time

# We only need the Controller now! 
# It handles reasoning, RAG, and tools internally.
from jarvis.controller import handle_query

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")
st.title("🤖 Jarvis Assistant")
st.caption("Week 2 Build: Modular Architecture")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("What is on your mind?"):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Processing..."):
        
        # --- THE MAGIC CHANGE ---
        # We let the controller handle EVERYTHING (Strategy, RAG, Search, Social)
        # This keeps your web app perfectly synced with your terminal app.
        response = handle_query(prompt) 
        
        time.sleep(0.5)

    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})