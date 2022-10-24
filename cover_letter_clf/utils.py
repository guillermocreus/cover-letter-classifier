import re


def clean_text(text: str):
    paragraphs = re.split("[\n]+[\s]*[\n]+", text)
    clean_paragraphs = []

    for k in range(len(paragraphs)):
        paragraphs[k] = re.sub("\n", " ", paragraphs[k]).strip()
        if len(paragraphs[k]) >= 90:
            clean_paragraphs.append(paragraphs[k])

    return clean_paragraphs
