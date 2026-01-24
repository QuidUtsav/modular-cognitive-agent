def chat_prompt(memory_context, query):
    return f"""
Conversation so far:
{memory_context}

User:
{query}

Respond naturally and helpfully.
"""


def retrieval_prompt(memory_context, context, query):
    return f"""
Conversation so far:
{memory_context}

Use ONLY the information below to answer.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""


def web_prompt(memory_context, context, query):
    return f"""
Conversation so far:
{memory_context}

You are answering a factual question using web search results.

Extract the correct answer from the information below.
Be concise and factual.
If the answer is not clearly stated, say "I don't know".

Web information:
{context}

Question:
{query}

Answer:
"""


def reasoning_prompt(memory_context, query):
    return f"""
Conversation so far:
{memory_context}

Think step by step and answer the question clearly.

Question:
{query}

Answer:
"""
