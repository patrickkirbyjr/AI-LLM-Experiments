from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

res = generator(
    "I would describe a Hobbit as a creature with",
    max_length=5,
    num_return_sequences=1
)

print(res)