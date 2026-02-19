from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('list/', views.NotesListView.as_view(), name='notes_list'),
    path('create/', views.NoteCreateView.as_view(), name='create'),
    path("note/<int:pk>/", views.NoteDetailView.as_view(), name="detail"),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete_note'),
]
