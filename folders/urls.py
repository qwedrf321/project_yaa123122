# folders/urls.py
from django.urls import path
from . import views

app_name = 'folders'  

urlpatterns = [
    path('', views.folder_list, name='list'),
    path('create/', views.create_folder, name='create'),
    path('<int:folder_id>/notes/', views.folder_notes, name='folder_notes'),
]