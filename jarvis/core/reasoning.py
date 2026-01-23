"""This module decides how the system should handle a user query."""

""" 
Labels:
1. direct_answer: The system will be able to provide a direct answer to the user's query.
2. needs_reasoning: The system needs to perform reasoning to answer the user's query.
3. needs_retrieval: The system needs to retrieve additional information to answer the user's query.
4. chat: The system should engage in a conversational manner to address the user's query.
"""
labels = [
    "direct_answer",
    "needs_reasoning",
    "needs_retrieval",
    "chat"
]
looks_like_chat = ["how are you", "tell me a joke", "what's up", "let's chat"]
looks_like_needs_retrieval = ["find me", "search for", "look up", "retrieve information about","document","according to","compare"]
looks_like_needs_reasoning = ["why", "how", "explain", "analyze", "compare"]

"""Priority: chat → retrieval → reasoning → direct_answer
Retrieval is checked before reasoning because reasoning may depend on retrieved information."""

def decide_strategy(user_query: str):
    user_query = user_query.lower()
    if any(phrase in user_query for phrase in looks_like_chat):
        return "chat"
    elif any(phrase in user_query for phrase in looks_like_needs_retrieval):
        return "needs_retrieval"
    elif any(phrase in user_query for phrase in looks_like_needs_reasoning):
        return "needs_reasoning"
    else:
        return "direct_answer"
    
