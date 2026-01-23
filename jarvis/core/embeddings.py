import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def load_document(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        return f.read()

def clean_document(text):
  
  text = re.sub(r'\[[^\]]*\]','',text)
  text = text.replace('\r\n','\n').replace('\r','\n')
  text = re.sub(r'\n{3,}','\n\n',text)  
                
  return text.strip()

def chunk_knowledge_base(text):
    paragraphs = re.split(r'\n\n',text)
    chunks = []
    for i, para in enumerate(paragraphs):
      para = para.strip()
      if len(para) < 50:
        continue
      chunks.append(
        {
          "chunk_id":i,
          "text":para,
          "length":len(para)
        }
      )
    return chunks
  
def embed_chunks(chunks):
    texts = [c["text"] for c in chunks]
    embeddings = embedding_model.encode(texts)

    for chunk, emb in zip(chunks, embeddings):
        chunk["embedding"] = emb

    return chunks

def normalize_query(query):
    return query.strip()

def embed_query(query):
    return embedding_model.encode([query])[0]

def retrieve_top_chunks_from_knowledge_base(chunks, query_embedding, top_k=3):
    scores = []

    for chunk in chunks:
        score = cosine_similarity(
            [query_embedding],
            [chunk["embedding"]]
        )[0][0]
        scores.append((score, chunk))

    scores.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in scores[:top_k]]
  
def retrieve_context_from_knowledge_base(query, chunks, top_k=1):
    query = normalize_query(query)
    query_embedding = embed_query(query)
    return retrieve_top_chunks_from_knowledge_base(chunks, query_embedding, top_k)
  
def prepare_chunks_for_knowledge_base(text):
    cleaned_text = clean_document(text)
    raw_chunks = chunk_knowledge_base(cleaned_text)
    embedded_chunks = embed_chunks(raw_chunks)
    return embedded_chunks

#Working with knowledge base
_knowledge_base_cache = {}

def embed(document_path, query):
    if document_path not in _knowledge_base_cache:
        text = load_document(document_path)
        chunks = prepare_chunks_for_knowledge_base(text)
        _knowledge_base_cache[document_path] = chunks

    chunks = _knowledge_base_cache[document_path]
    return retrieve_context_from_knowledge_base(query, chunks)

