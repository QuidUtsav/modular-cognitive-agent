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

labels = [
    "direct_answer",
    "needs_reasoning",
    "needs_retrieval",
    "chat",
    "needs_web"
]
CHAT_PHRASES = [
    "hi",
    "hello",
    "thanks",
    "thank you",
    "how are you",
    "tell me a joke",
    "what's up",
    "let's chat",
    "who are you",
    "your name",
    "who created you",
    "how do you feel",
    "who are you",
    "what can you do"
]
WEB_PHRASES = [
    "latest",
    "current",
    "today",
    "news",
    "price",
    "recent",
    "now"
]

RETRIEVAL_PHRASES = [
    "find",
    "search",
    "look up",
    "retrieve",
    "according to",
    "from the document",
    "based on the document",
    "in the text",
    "who is",
    "what is"
]

REASONING_PHRASES = [
    "why",
    "how",
    "explain",
    "analyze",
    "compare",
    "difference between",
    "pros and cons"
]

"""Priority: chat → retrieval → reasoning → direct_answer
Retrieval is checked before reasoning because reasoning may depend on retrieved information."""

def decide_strategy(user_query: str):
    query = normalize(user_query)

    if any(p in query for p in CHAT_PHRASES):
        return "chat"
    
    if any(p in query for p in WEB_PHRASES):
        return "needs_web"
    
    if any(p in query for p in RETRIEVAL_PHRASES):
        return "needs_retrieval"

    if any(p in query for p in REASONING_PHRASES):
        return "needs_reasoning"

    return "direct_answer"

