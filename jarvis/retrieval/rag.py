from jarvis.core.embeddings import embed
from jarvis.core.generation import generate_text
def rag_model(file_path, query):

    result = embed(file_path, query)
    
    context = result[0]['text']
    prompt ="""Answer using ONLY the provided context.
            If the answer is not present, say you don’t know"""
    return generate_text(f"{prompt}\n\nContext: {context}\n\nQuestion: {query}")['answer']
    