from django.urls import path
from .views import *

urlpatterns = [
    path('pdf/', GeneratePdf.as_view()),
    path('excel/', ExportImportExcel.as_view())
]
