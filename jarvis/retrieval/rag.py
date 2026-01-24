from jarvis.core.embeddings import embed
from jarvis.core.generation import generate_text
def rag_model(file_path, query):

    results = embed(file_path, query)
    if not results:
        return "Not found on the provided documents."

    top_score = results[0][0]
    if top_score < 0.15:
        return "I don't know based on the provided documents."
    
    contexts = []
    for score, chunk in results:
        print(f"[DEBUG] score={score:.3f} chunk_id={chunk['chunk_id']}")
        contexts.append(chunk["text"])

    context = "\n\n".join(contexts)
    prompt ="""Answer using ONLY the provided context.
            If the answer is not present, say you don’t know"""
    return generate_text(f"{prompt}\n\nContext: {context}\n\nQuestion: {query}")['answer']
    