from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='home'),
    path('list/', views.notes_list, name='notes_list'),
    path('create/', views.note_create, name='create'),
]