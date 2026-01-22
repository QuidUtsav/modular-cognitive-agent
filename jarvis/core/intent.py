import random
from transformers import pipeline


model = pipeline(
    task="zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)
ner = pipeline(
    task="ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

label =["social conversation","factual information lookup"]
chat_content = ["hi","hello","thanks","thank you"]
search_content = ["who", "what", "when", "where", "how does","tell me about"]
SOCIAL_ACT_PATTERNS = {
  "GREETING": ["hi", "hello", "hey"],
  "GRATITUDE": ["thank", "thanks"],
  "PERMISSION_REQUEST": ["can i ask", "may i ask"],
  "WELLBEING_QUERY": ["how are you", "how do you feel"],
}
SOCIAL_ACT_RESPONSES = {
  "GREETING": [
      "Hey 🙂 What can I help you with?",
      "Hi there! How can I assist?"
  ],
  "GRATITUDE": [
      "You're welcome!",
      "Glad I could help 🙂"
  ],
  "PERMISSION_REQUEST": [
      "Of course. Go ahead.",
      "Sure, what do you want to ask?"
  ],
  "WELLBEING_QUERY": [
      "I'm doing well — how can I help you today?",
      "I'm just here to help you 🙂"
  ]
}
INFO_VERBS = ["explain", "tell", "describe", "define"]

def looks_like_info_request(text):
    return any(v in text for v in INFO_VERBS)

def route_intent(text):
  result=model(text,label)

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

  return final_decision

def handle_social_conversation(text):
  for key,value in SOCIAL_ACT_PATTERNS.items():
    if any(x in text for x in value):
      return key
  return None

def handle_factual_information_lookup(text):
  print("Let me look that up for you.")
  return "(Search results will appear here)"


def extract_entities(text):
  entities = ner(text)
  values={}

  for entity in entities:
    label = entity["entity_group"]
    word = entity["word"]

    values.setdefault(label, []).append(word)
  return values

def debug_decision(raw_text, intent, entities, response=None):
    return {
        "input": raw_text,
        "intent": intent,
        "response": response,
        "entities": entities
    }

# Action for Chatbot

while True:
    raw_text = input("what do you have in mind today? ")
    normalized_text = raw_text.lower()
    if looks_like_info_request(normalized_text):
        intent = "factual information lookup"
    else:
        intent = route_intent(normalized_text)

    print(intent)

    if intent == "social conversation":
        social_act = handle_social_conversation(normalized_text)
        if social_act:
            response = random.choice(SOCIAL_ACT_RESPONSES[social_act])
        else:
            response = random.choice(SOCIAL_ACT_RESPONSES["GREETING"])
    else:
        response = handle_factual_information_lookup(raw_text)
    entities = extract_entities(raw_text)
    debug = debug_decision(raw_text, intent, entities, response)
    print(debug)
    print("press 1 to exit")
    if input() == "1":
        break

