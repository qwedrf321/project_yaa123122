from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Note
from .forms import NoteForm

def index(request):
    return render(request, 'index.html')

def notes_list(request):
    notes_all = Note.objects.all().order_by('-created_at')
    paginator = Paginator(notes_all, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'notes/notes_list.html', {'page_obj': page_obj})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})

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

@login_required 
def delete_note(request, pk):
    note = get_object_or_404(Note, id=pk)
    if note.owner == request.user:
        note.delete()
    return redirect('notes:notes_list')