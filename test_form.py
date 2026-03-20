import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_yaa123122.settings')
import django
django.setup()
from notes.forms import NoteForm
from django.contrib.auth.models import User

u = User.objects.first()
data = {'title': 'Test Note', 'content': 'This is test content', 'is_public': True}
form = NoteForm(data=data, user=u)
print('Form valid:', form.is_valid())
if not form.is_valid():
    print('Errors:', form.errors)
else:
    form.instance.owner = u
    note = form.save()
    print('Saved, content:', repr(note.content))