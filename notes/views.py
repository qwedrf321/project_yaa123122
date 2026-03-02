from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Note
from .forms import NoteForm
from django.db.models import Q

class IndexView(TemplateView):
    template_name = 'index.html'

class NotesListView(ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    paginate_by = 6
    ordering = ['-created_at']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(
                Q(is_public=True) | Q(owner=self.request.user)
            ).order_by('-created_at')
        else:
            return Note.objects.filter(is_public=True).order_by('-created_at')

class NoteDetailView(UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

    def test_func(self):
        note = self.get_object()
        if note.is_public:
            return True
        return note.owner == self.request.user

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