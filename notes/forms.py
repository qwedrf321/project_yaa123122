from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'folder', 'is_public']
    
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            # Показываем только папки текущего пользователя
            self.fields['folder'].queryset = user.folders.all()
            self.fields['folder'].required = False
            self.fields['folder'].empty_label = "Без папки"
