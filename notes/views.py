from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm


def index(request):
    return render(request, 'index.html')


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': notes})


@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.user, request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('notes:notes_list')
    else:
        form = NoteForm(user=request.user)
    return render(request, 'notes/notes_create.html', {'form': form})