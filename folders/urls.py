# folders/urls.py
from django.urls import path
from .views import FolderListView, FolderCreateView, FolderNotesView

app_name = 'folders'

urlpatterns = [
    path('', FolderListView.as_view(), name='list'),
    path('create/', FolderCreateView.as_view(), name='create'),
    path('<int:folder_id>/notes/', FolderNotesView.as_view(), name='folder_notes'),
]