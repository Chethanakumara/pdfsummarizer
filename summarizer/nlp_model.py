import fitz  # PyMuPDF
import torch
import re
from transformers import pipeline

# Load model ONCE
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=0 if torch.cuda.is_available() else -1
)

# ---------- CLEAN TEXT ----------
def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# ---------- SMART CHUNKING ----------
def chunk_text(text, chunk_size=600):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

# ---------- MAIN SUMMARIZER ----------
def summarize_pdf(pdf_file, max_pages=20):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    summaries = []

    for page_num in range(min(len(doc), max_pages)):
        page_text = clean_text(doc[page_num].get_text())

        if len(page_text) < 300:
            continue

        page_summary = []

        for chunk in chunk_text(page_text):
            result = summarizer(
                chunk,
                max_length=300,
                min_length=150,
                do_sample=False
            )
            page_summary.append(result[0]["summary_text"])

        summaries.append(f"\n📄 Page {page_num + 1} Summary:\n" + " ".join(page_summary))

    if not summaries:
        return "No readable text found in PDF."

    return "\n".join(summaries)
