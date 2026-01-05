from django.shortcuts import render
from .services import summarize_pdf
from .utils import export_pdf, export_docx

def pdf_upload(request):
    if request.method == "POST":
        pdf = request.FILES["pdf"]
        detail = request.POST.get("detail", "medium")

        summaries, keywords = summarize_pdf(pdf, detail_level=detail)

        request.session["summary_data"] = summaries

        return render(request, "result.html", {
            "summaries": summaries,
            "keywords": keywords
        })

    return render(request, "upload.html")
