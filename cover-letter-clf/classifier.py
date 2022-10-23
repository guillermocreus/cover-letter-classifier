from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers_interpret import ZeroShotClassificationExplainer
import torch
import numpy as np
from utils import clean_text


class Classifier:
    def __init__(self, model_name: str = "facebook/bart-large-mnli") -> None:

        # models_to_choose = {"facebook/bart-large-mnli",
        #                     "typeform/distilbert-base-uncased-mnli"}

        self.nli_model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.nli_model = self.nli_model.to(self.device)

    def classification_scores(
        self, cover_letter: str, labels: list[str]
    ) -> list[(str, float)]:
        """
        Given cover letter text and a list of labels, return list of label
        and score pairs.
        """

        results_dict = {label: 0 for label in labels}
        clean_paragraphs = clean_text(cover_letter)

        for paragraph in clean_paragraphs:
            premise = [paragraph] * len(labels)
            hypothesis = [
                f"In this paragraph the applicant shows {label}." for label in labels
            ]

            x = self.tokenizer(
                premise, hypothesis, return_tensors="pt", truncation=True, padding=True
            )

            x = {key: value.to(self.device) for key, value in x.items()}

            with torch.no_grad():
                logits = self.nli_model(**x)["logits"]

            entail_contradiction_logits = logits[:, [0, 2]].cpu()
            probs = entail_contradiction_logits.softmax(dim=1).numpy()
            prob_label_is_true = probs[:, 1]

            for k, label in enumerate(labels):
                results_dict[label] = max(results_dict[label], prob_label_is_true[k])

        results = [(label, score) for label, score in results_dict.items()]

        return results

    def classification_interpret(
        self, cover_letter: str, label: str
    ) -> list[(str, float)]:
        """
        Given cover letter text and a label, return list of each cover
        letter token and score pairs.
        """

        clean_paragraphs = clean_text(cover_letter)
        zero_shot_explainer = ZeroShotClassificationExplainer(
            self.nli_model, self.tokenizer
        )

        results = []

        for paragraph in clean_paragraphs:
            word_attributions = zero_shot_explainer(
                paragraph,
                labels=[label],
            )

            results += word_attributions[label]

        return results
