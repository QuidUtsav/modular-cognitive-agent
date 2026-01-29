from modular_agent.core.embeddings import embed_query
from sklearn.metrics.pairwise import cosine_similarity
"""This module decides how the system should handle a user query."""

""" 
Labels:
1. direct_answer: The system will be able to provide a direct answer to the user's query.
2. needs_reasoning: The system needs to perform reasoning to answer the user's query.
3. needs_retrieval: The system needs to retrieve additional information to answer the user's query.
4. chat: The system should engage in a conversational manner to address the user's query.
"""
import re

def normalize(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

STRATEGIES = {
    "needs_web": (
        "search google, who is, what is, current events, latest news, weather, real-time facts, president, ceo,"
        "questions about current facts like who is the president, whats the weather, "
        "latest software versions, prices, news, or real-world information"
    ),
    "direct_answer": (
        "simple factual questions like how many months are in a year, "
        "basic math, or well known facts"
    ),
    "needs_reasoning": (
        "why and how questions that require explanation, logic, "
        "or step by step reasoning"
    ),
    "needs_retrieval": (
        "questions that must be answered using provided documents or text"
    ),
    "chat": (
        "greetings, casual conversation, small talk, thanks, or jokes"
    )
}


STRATEGY_EMBEDDINGS = {
    name: embed_query(desc)
    for name, desc in STRATEGIES.items()
}


"""Priority: chat → retrieval → reasoning → direct_answer
Retrieval is checked before reasoning because reasoning may depend on retrieved information."""

def semantic_routing(user_quer: str):
    query_emb = embed_query(user_quer)
    
    scores= {}
    for strategy, emb in STRATEGY_EMBEDDINGS.items():
        score = cosine_similarity([query_emb],[emb])[0][0]
        scores[strategy]=score
    best_strategy = max(scores, key= scores.get)
    confidence = scores[best_strategy]
    
    return best_strategy, confidence