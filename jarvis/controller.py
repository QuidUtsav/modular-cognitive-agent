from jarvis.core.reasoning import decide_strategy
from jarvis.retrieval.rag import rag_model
from jarvis.core.intent import handle_social_conversation, SOCIAL_ACT_RESPONSES
from jarvis.tools.web_search import web_search
from jarvis.core.generation import generate_text
from jarvis.memory.short_term import ShortTermMemory
from jarvis.prompts.templates import (
    chat_prompt,
    retrieval_prompt,
    web_prompt,
    reasoning_prompt
)
import random

memory = ShortTermMemory(max_turns=5)

def handle_query(query: str):
    strategy = decide_strategy(query)
    print(f"[DEBUG] strategy={strategy}")

    memory_context = memory.get_context()
    response = None  

    # ---- CHAT ----
    if strategy == "chat":
        social_intent = handle_social_conversation(query.lower())
        if social_intent and social_intent in SOCIAL_ACT_RESPONSES:
            response = random.choice(SOCIAL_ACT_RESPONSES[social_intent])
        else:
            response = "I'm Jarvis — an AI assistant I'm still learning about myself 🙂"

    # ---- WEB ----
    elif strategy == "needs_web":
        results = web_search(query)

        clean_snippets = [
            r["snippet"].strip()
            for r in results
            if len(r["snippet"].strip()) > 20
        ]

        context = "\n".join(clean_snippets)

        prompt = web_prompt(
            memory_context=memory_context,
            context=context,
            query=query
        )

        response = generate_text(prompt)

    # ---- RAG / RETRIEVAL ----
    elif strategy in ["needs_retrieval", "needs_reasoning", "direct_answer"]:
        retrieved_chunks = rag_model("document.txt", query)

        response = retrieved_chunks


    else:
        response = "I am not sure how to handle that yet."

    memory.add(query, response)

    return response
