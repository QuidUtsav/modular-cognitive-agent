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
from jarvis.memory.extractor import extract_user_facts
from jarvis.memory.long_term import LongTermMemory


st_memory = ShortTermMemory(max_turns=5)
lt_memory = LongTermMemory()


def handle_query(query: str):
    
#Store long-term facts 
    facts = extract_user_facts(query) 
    if facts: 
        saved_items=[] 
        for fact in facts: 
            lt_memory.store_fact( 
                mem_type=fact["type"], 
                key=fact["key"], value=fact["value"], 
                confidence=fact["confidence"], 
                source=fact["source"] 
                ) 
        saved_items.append(f"{fact['key']}: {fact['value']}") 
        response=f"Got it! I've noted that you {', '.join(saved_items)}." 
        st_memory.add(query, response) 
        return response
        
    # Check long-term memory for an answer
    memory_answer = lt_memory.answer_from_memory(query)
    if memory_answer:
        return memory_answer
    
    # Decide strategy
    strategy = decide_strategy(query)
    print(f"[DEBUG] strategy={strategy}")

    memory_context = st_memory.get_context()
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

    st_memory.add(query, response)

    return response
