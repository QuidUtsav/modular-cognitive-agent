from jarvis.retrieval.rag import rag_model
from jarvis.core.reasoning import decide_strategy
query = "Compare BERT and GPT"
strategy = decide_strategy(query)
print(f"Decided strategy: {strategy}")
if strategy == "needs_retrieval":
    response = rag_model("document.txt", query)
else:
    response = "Strategy not supported in this example."
    
print(response)