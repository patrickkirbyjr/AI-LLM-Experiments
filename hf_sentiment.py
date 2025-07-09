from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertTokenizer, BertModel
import torch
import torch.nn.functional as F

# classifier = pipeline("sentiment-analysis")
# res = classifier("I hate EVERYTHING.")
# print(res)

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# res = classifier("I hate EVERYTHING.")
# print(res)

# multiple sentiments
X_train = [
    "I hate EVERYTHING.",
    "Life is just great!",
    "What a glooomy, depressing day."
]

# output
res = classifier(X_train)
print(res)

batch = tokenizer(X_train, padding=True, truncation=True, max_length=512, return_tensors="pt")
print(batch)

# step by step with pytorch
with torch.no_grad():
    outputs = model(**batch)
    print(outputs)
    predictions = F.softmax(outputs.logits, dim=1)
    print(predictions)
    labels = torch.argmax(predictions, dim=1)
    print(labels)

# step by step
# sequence = "I enjoy calm walks on the beach."
# res = tokenizer(sequence)
# print(res)
# tokens = tokenizer.tokenize(sequence)
# print(tokens)
# ids = tokenizer.convert_tokens_to_ids(tokens)
# print(ids)
# decoded_string = tokenizer.decode(ids)
# print(decoded_string)

# saving tokenizer and model
save_directory = "saved_tokenizer_model"
tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)

# loading tokenizer and model
tok = AutoTokenizer.from_pretrained(save_directory)
mod = AutoModelForSequenceClassification.from_pretrained(save_directory)