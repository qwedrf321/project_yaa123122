from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'folder', 'is_public']
    
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['folder'].queryset = user.folders.all()
            self.fields['folder'].required = False
            self.fields['folder'].empty_label = "Без папки"

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User