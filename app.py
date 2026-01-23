from jarvis.retrieval.rag import rag_model
from jarvis.core.reasoning import decide_strategy
query = "Compare BERT and GPT"
strategy = decide_strategy(query)
if strategy == "needs_retrieval":
    response = rag_model("document.txt", query)
else:
    response = "Strategy not supported in this example."
    
print(response)