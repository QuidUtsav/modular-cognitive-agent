from transformers import pipeline
model = pipeline(
    task="zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)
label =["social conversation","factual information lookup"]
chat_content = ["hi","hello","thanks","thank you"]
search_content = ["who", "what", "when", "where", "how does","tell me about"]
while(True):
  text=input("what do you have in mind today? ")
  result=model(text.lower(),label)
  top_labels,top_scores=result["labels"],result["scores"]

  if(any(x in text for x in chat_content)):
    final_decision = "social conversation"
  elif(any(x in text for x in search_content)):
    final_decision = "factual information lookup"
  else:
    if(top_scores[0]<=.55):
      final_decision = "factual information lookup"
    else:
      final_decision = top_labels[0]
  print(f"{final_decision}")
  print("press 1 to exit")
  if(input()=="1"):
    break
