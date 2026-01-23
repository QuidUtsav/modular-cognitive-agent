from transformers import pipeline

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
    print(f"[DEBUG] generated_text={output[0]['generated_text']}")
    return {
    "answer": output[0]["generated_text"],
    "model": "flan-t5-base"
    }