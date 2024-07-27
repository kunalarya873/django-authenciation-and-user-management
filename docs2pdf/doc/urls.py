from django.urls import path
from .views import index, check_status, download_file

urlpatterns = [
    path('', index, name='index'),
    path('status/<str:task_id>/', check_status, name='check_status'),
    path('download/<str:file_path>/', download_file, name='download_file'),
]
