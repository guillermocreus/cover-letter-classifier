from transformers import BartForSequenceClassification, BartTokenizer
import torch
import numpy as np
import json
import sys

nli_model = BartForSequenceClassification.from_pretrained('facebook/bart-large-mnli')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-mnli')
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
nli_model = nli_model.to(device)

if __name__=="__main__":
    path = sys.argv[1]
    input_data = json.load(open(path))

    text = input_data["text"]
    labels = input_data["labels"]

    premise = [text] * len(labels)
    hypothesis = [f'This example is {label}.' for label in labels]

    x = tokenizer(premise, hypothesis, return_tensors='pt', truncation=True, padding=True)

    for key in x:
        x[key] = x[key].to(device)

    with torch.no_grad():
        logits = nli_model(**x)["logits"]

    entail_contradiction_logits = logits[:, [0, 2]]
    probs = entail_contradiction_logits.softmax(dim=1).numpy()
    prob_label_is_true = probs[:, 1]

    ordered_labels = np.argsort(-prob_label_is_true)

    print("Given the text:", text)
    print("The labels predicted are:")
    print("-" * 30)

    for label, p in zip(np.array(labels)[ordered_labels], prob_label_is_true[ordered_labels]):
        print(f'Label {label}: p =', round(p, 3))

