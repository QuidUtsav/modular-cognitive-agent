from transformers import pipeline
from jarvis.prompts.templates import web_prompt
from jarvis.tools.web_search import web_search


generator = pipeline(
    task="text2text-generation",
    model = "google/flan-t5-base"
)

# Action for text-generation
def generate_text(prompt):
    prompt = prompt

    output = generator(
        prompt,
        max_new_tokens=100,
        do_sample=False
    )
    return output[0]["generated_text"]
    
    
def handle_web_search(query, memory_context):
    results = web_search(query)

    clean_snippets = [
            r["snippet"].strip()
            for r in results if len(r["snippet"].strip()) > 20
        ]

    context = "\n".join(clean_snippets)

    prompt = web_prompt(
            memory_context=memory_context,
            context=context,
            query=query
        )
    return generate_text(prompt)