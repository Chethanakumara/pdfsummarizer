from django.db import models
from django.utils import timezone

class PdfSummary(models.Model):
    pdf = models.FileField(upload_to="pdfs/")
    summary = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pdf.name
