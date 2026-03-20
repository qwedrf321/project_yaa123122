from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from folders.models import Folder


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, required=False)  

    class Meta:
        model = Note
        fields = ['title', 'folder', 'is_public', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['content'].initial = self.instance.content

    def save(self, commit=True):
        note = super().save(commit=commit)
        if commit:
            note.content = self.cleaned_data.get('content', '')
            note.save()
        return note

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['folder'].queryset = user.folders.all()
        else:
            self.fields['folder'].queryset = Folder.objects.none()

        self.fields['folder'].required = False
        self.fields['folder'].empty_label = "Без папки"


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User