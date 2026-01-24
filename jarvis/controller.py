from jarvis.core.reasoning import decide_strategy
from jarvis.retrieval.rag import rag_model
from jarvis.core.intent import handle_social_conversation, SOCIAL_ACT_RESPONSES
import random

def handle_query(query: str):
    strategy = decide_strategy(query)

    if strategy == "chat":
        social_intent = handle_social_conversation(query.lower())
        if social_intent and social_intent in SOCIAL_ACT_RESPONSES:
            return random.choice(SOCIAL_ACT_RESPONSES[social_intent])
        return rag_model("system_identity.txt", query)

    if strategy in ["needs_retrieval", "needs_reasoning", "direct_answer"]:
        return rag_model("document.txt", query)

    return "I am not sure how to handle that yet."
