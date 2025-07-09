from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier(
    "The wizard just got his first wand!",
    candidate_labels=["fantasy", "self-help", "romance"],
)

print(res)