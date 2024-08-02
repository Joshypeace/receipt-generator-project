from django.urls import path
from .views import create_receipt, download_receipt_pdf

urlpatterns = [
    path('create/', create_receipt, name='create_receipt'),
    path('download/<int:pk>/', download_receipt_pdf, name='download_receipt_pdf'),
]
