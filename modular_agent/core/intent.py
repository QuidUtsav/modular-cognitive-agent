# FILE: jarvis/core/intent.py
"""
The 'Reflex' System.
Handles instant social responses (Hi, Thanks, Bye) without touching the LLM.
Efficient and lightweight (No heavy models).
"""

SOCIAL_ACT_PATTERNS = {
  "GREETING": ["hi", "hello", "hey", "good morning", "good evening"],
  "GRATITUDE": ["thank", "thanks", "thx", "appreciate it"],
  "PERMISSION_REQUEST": ["can i ask", "may i ask", "quick question"],
  "WELLBEING_QUERY": ["how are you", "how do you feel", "what's up"],
}

SOCIAL_ACT_RESPONSES = {
  "GREETING": [
      "Hey there! What's on your mind?",
      "Hello! Ready to help.",
      "Hi! I'm listening."
  ],
  "GRATITUDE": [
      "You're welcome!",
      "Anytime.",
      "Glad I could help."
  ],
  "PERMISSION_REQUEST": [
      "Go ahead, I'm listening.",
      "Shoot. What do you need?"
  ],
  "WELLBEING_QUERY": [
      "System green. All logic circuits functioning.",
      "I'm just code, but I'm feeling productive."
  ]
}

def handle_social_conversation(text: str):
    """
    Checks if the text matches a hardcoded social pattern.
    Returns the key (e.g., 'GREETING') or None.
    """
    text = text.lower().strip()
    for key, patterns in SOCIAL_ACT_PATTERNS.items():
        if any(p in text for p in patterns):
            return key
    return None