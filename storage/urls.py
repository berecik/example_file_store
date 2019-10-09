from django.urls import path, include
from .views import upload_file, download_file

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('<str:file_hash>/', download_file, name='download')
]
