from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from notes.models import Note
from .models import Folder

@login_required
def create_folder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('name', '')
        if folder_name.strip():
            Folder.objects.create(name=folder_name, owner=request.user)
        return redirect('folders:list')
    return render(request, 'folders/folder_create.html')


@login_required
def folder_list(request):
    folders = request.user.folders.all()
    return render(request, 'folders/folder_list.html', {'folders': folders})

# folders/views.py
def folder_notes(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    # Фильтруем заметки, у которых поле folder совпадает с текущей папкой
    notes = Note.objects.filter(folder=folder) 
    return render(request, 'folders/folder_notes.html', {'folder': folder, 'notes': notes})