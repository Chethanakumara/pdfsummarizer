📄 PDF Summarizer using NLP (Django + Transformers)
🔍 Project Overview

The PDF Summarizer is a web-based application that automatically generates concise and accurate summaries from PDF documents using Natural Language Processing (NLP).
It is built with Django on the backend and leverages Hugging Face Transformer models (BART) for abstractive text summarization.

This project is especially useful for summarizing long research papers, reports, books, and documentation in seconds.

🚀 Features

📤 Upload PDF documents

📄 Extract text from multiple PDF pages

🧠 Abstractive summarization using facebook/bart-large-cnn

📏 Adjustable summary length (Short / Medium / Detailed)

✂️ Text cleaning and chunk-based summarization for large PDFs

📥 Export summary as PDF or DOCX

🌐 Simple and clean web interface (Bootstrap)

🐳 Dockerized for easy deployment

🛠️ Tech Stack

Backend: Django (Python)

NLP Model: Hugging Face Transformers (BART)

PDF Processing: PyMuPDF (fitz)

ML / NLP: PyTorch

Export: ReportLab (PDF), python-docx (DOCX)

Frontend: HTML, Bootstrap

Containerization: Docker

🧠 How It Works

User uploads a PDF file

Text is extracted from selected pages

Text is cleaned and split into manageable chunks

Each chunk is summarized using a Transformer model

Final summaries are merged into a detailed output

User can view or export the summary


⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/chethankiruvaase/pdfsummarizer.git
cd pdfsummarizer

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Server
python manage.py migrate
python manage.py runserver


Open browser:

http://127.0.0.1:8000/

🐳 Docker Usage
docker build -t pdfsummarizer .
docker run -p 8000:8000 pdfsummarizer

📌 Use Cases

Research paper summarization

Academic notes generation

Legal and medical document review

Business reports analysis

Quick document understanding

View
<img width="1914" height="1025" alt="Screenshot 2026-01-05 181025" src="https://github.com/user-attachments/assets/bc31ff62-f0c6-4a49-bbfd-073762cc3e8e" />

<img width="1913" height="1032" alt="Screenshot 2026-01-05 180922" src="https://github.com/user-attachments/assets/7d7ea3f4-2c41-4a13-ad6a-0ce93c1d3fa5" />

<img width="1917" height="1018" alt="Screenshot 2026-01-05 181010" src="https://github.com/user-attachments/assets/f4677072-f9e9-424f-a2c9-6e7106888d4c" />




