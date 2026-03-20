from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Note
from .forms import NoteForm, UserRegistrationForm

class IndexView(TemplateView):
    template_name = 'index.html'

class NotesListView(ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    paginate_by = 6
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Note.objects.filter(
                Q(is_public=True) | Q(owner=user)
            ).order_by('-created_at')

        return Note.objects.filter(is_public=True).order_by('-created_at')

class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'
    login_url = '/login/'

    def test_func(self):
        note = self.get_object()
        return note.is_public or note.owner == self.request.user

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/notes_create.html'
    success_url = reverse_lazy('notes:notes_list')
    login_url = '/login/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user 
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:notes_list')
    login_url = '/login/'

    def test_func(self):
        return self.get_object().owner == self.request.user

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('notes:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Вы успешно зарегистрировались!")
        return redirect(self.success_url)