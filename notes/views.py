from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Note
from .forms import NoteForm

class IndexView(TemplateView):
    template_name = 'index.html'

class NotesListView(ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    paginate_by = 3
    ordering = ['-created_at']

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/notes_create.html'
    success_url = reverse_lazy('notes:notes_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:notes_list')

    def test_func(self):
        note = self.get_object()
        return note.owner == self.request.user