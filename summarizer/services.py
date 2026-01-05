import fitz
import torch
import re
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from itertools import islice

# Load models ONCE
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=0 if torch.cuda.is_available() else -1
)

# ---------- CLEAN ----------
def clean_text(text):
    text = re.sub(r"\s+", " ", text.replace("\n", " "))
    text = re.sub(r"http\S+", "", text)
    return text.strip()

# ---------- BATCH CHUNKS ----------
def batch_chunks(iterable, batch_size=4):
    iterator = iter(iterable)
    while batch := list(islice(iterator, batch_size)):
        yield batch

def chunk_text(text, size=600):
    words = text.split()
    for i in range(0, len(words), size):
        yield " ".join(words[i:i + size])

# ---------- KEYWORDS ----------
def extract_keywords(text, top_n=10):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform([text])
    scores = zip(tfidf.get_feature_names_out(), tfidf_matrix.toarray()[0])
    keywords = sorted(scores, key=lambda x: x[1], reverse=True)
    return [word for word, score in keywords[:top_n]]

# ---------- MAIN ----------
def summarize_pdf(pdf_file, max_pages=20, detail_level="medium"):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    length_map = {
        "short": (120, 60),
        "medium": (220, 120),
        "long": (350, 200),
    }
    max_len, min_len = length_map[detail_level]

    page_summaries = []
    full_text = ""

    for i in range(min(len(doc), max_pages)):
        page_text = clean_text(doc[i].get_text())
        full_text += page_text + " "

        if len(page_text) < 300:
            continue

        summaries = []
        chunks = list(chunk_text(page_text))

        for batch in batch_chunks(chunks):
            results = summarizer(
                batch,
                max_length=max_len,
                min_length=min_len,
                do_sample=False
            )
            summaries.extend(r["summary_text"] for r in results)

        page_summaries.append({
            "page": i + 1,
            "summary": " ".join(summaries)
        })

    keywords = extract_keywords(full_text)

    return page_summaries, keywords
