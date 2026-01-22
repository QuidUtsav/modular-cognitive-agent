import re
from transformers import pipeline

generator = pipeline(
    task="text2text-generation",
    model = "google/flan-t5-base"
)

# Action for text-generation
jarvis_prompt = """

Question: A shopkeeper buys a pen for 10 rupees and sells it for 15 rupees. 
If he sells 20 pens, what is his total profit?

Let's think step by step.

"""

output = generator(
    jarvis_prompt,
    max_new_tokens=100,
    do_sample=False
)
print(output[0]['generated_text'])