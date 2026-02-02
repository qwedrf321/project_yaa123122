from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
