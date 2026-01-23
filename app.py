from jarvis.retrieval.rag import rag_model
from jarvis.core.reasoning import decide_strategy


print("Jarvis is ready. Type 'exit' to quit.\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    strategy = decide_strategy(query)
    print(f"[DEBUG] strategy={strategy}")

    if strategy == "needs_retrieval" or strategy == "needs_reasoning":
        response = rag_model("document.txt", query)
    else:
        response = "Not implemented yet"

    print("Jarvis:", response)