from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Folder
from django.views.generic import ListView
from django.views.generic import DetailView
from notes.models import Note


class FolderCreateView(LoginRequiredMixin, CreateView):
    model = Folder
    fields = ['name']
    template_name = 'folders/folder_create.html'
    success_url = reverse_lazy('folders:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FolderListView(LoginRequiredMixin, ListView):
    model = Folder
    template_name = 'folders/folder_list.html'
    context_object_name = 'folders'

    def get_queryset(self):
        return self.request.user.folders.all()

class FolderNotesView(LoginRequiredMixin, DetailView):
    model = Folder
    template_name = 'folders/folder_notes.html'
    context_object_name = 'folder'
    pk_url_kwarg = 'folder_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(folder=self.object)
        return context