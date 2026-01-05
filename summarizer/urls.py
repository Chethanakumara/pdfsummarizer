from django.urls import path
from .views import pdf_upload

urlpatterns = [
    path("", pdf_upload, name="pdf_upload"),
]
