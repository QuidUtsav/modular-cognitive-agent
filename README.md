🧠 Intent Router & Entity Extractor (Week 1 Complete)

This repository contains the cognitive core of a Jarvis-style personal assistant.

It is an intelligent routing layer that processes user input, decides what the user wants (Intent), identifies key subjects (Entities), and selects the appropriate response strategy.

    Status: ✅ Week 1 Complete The system now classifies intents, extracts named entities (People, Locations, Orgs), and handles basic social interactions with randomized responses.

✨ Week 1 Milestones

Moving beyond simple classification, the system now includes:

    Hybrid Intent Detection: Combines keyword heuristics (rules) with a Zero-Shot Transformer model.

    Named Entity Recognition (NER): Automatically extracts important details (e.g., "Nepal", "Python") using BERT.

    Social Sub-Intents: granular handling of Greetings, Gratitude, Wellbeing, and Permissions.

    Confidence Thresholding: A safety mechanism that defaults to "Search" if the AI isn't confident in its classification (<0.55).

    Debug Mode: Outputs a structured JSON object visualizing the AI's decision process.

🧩 The Logic Flow

The system doesn't just guess; it follows a specific decision tree to ensure reliability.

    Normalization: Input is lowercased for consistency.

    Heuristic Check:

        Does it contain specific "info verbs" (explain, define)? -> Force Search.

        Does it match social keywords? -> Force Social.

    Zero-Shot Classification: If no rules match, the Transformer model analyzes the semantic meaning.

    Confidence Check: If the model's confidence is low (below 55%), the system safely assumes it's a factual lookup.

    Entity Extraction: Parallel process to pull out names and places.

    Response Generation:

        Social: Selects a random natural response from a pre-defined template.

        Info: Prepares a placeholder for the future search engine.

🤖 Models Used

The brain consists of two distinct Hugging Face pipelines:

Function	Model	Purpose
Intent Classification	typeform/distilbert-base-uncased-mnli	Determines if input is "Social" or "Factual".
Entity Extraction	dslim/bert-base-NER	Identifies Real-world objects (PER, ORG, LOC, MISC).
💻 Usage & Example Output

When running the script, the assistant analyzes the input and returns a debug object containing the raw decision data.
Scenario A: Information Lookup

User Input: "Who invented Python?"
JSON

{
  "input": "who invented python?",
  "intent": "factual information lookup",
  "social_act": null,
  "entities": {
      "MISC": ["Python"]
  }
}

System Action: triggers handle_factual_information_lookup
Scenario B: Social Interaction

User Input: "Thanks for your help"
JSON

{
  "input": "thanks for your help",
  "intent": "social conversation",
  "social_act": "GRATITUDE",
  "entities": {}
}

System Action: Responds "Glad I could help 🙂"
🏗️ Code Structure (Week 1)

    route_intent(text): The core logic gate.

    extract_entities(text): The NER pipeline.

    handle_social_conversation(text): Matches specific social cues to templates.

    SOCIAL_ACT_RESPONSES: A dictionary of randomized persona-based replies.

🚧 Current Limitations

    Search is Mocked: The system identifies when to search, but doesn't actually query the web yet.

    NER Sensitivity: The bert-base-NER model is case-sensitive (normalization logic needs fine-tuning for entities).

    Context: No multi-turn memory yet (each query is treated as new).

🛣️ Roadmap: Week 2

    🔌 Connect Real Search: Replace the mock print statement with a Wikipedia API or Google Search integration.

    🧠 Command Intent: Add a third intent class for "Actions" (e.g., "Open YouTube", "Set a timer").

    🧹 Code Refactoring: Move dictionaries and config to a separate file for cleaner logic.

🧑‍💻 About the Project

This is a personal journey into Applied AI Systems. The goal is not just to use an LLM API, but to understand the architecture required to build a controllable, deterministic assistant system.

Feedback and contributions are welcome!
