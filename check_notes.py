import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_yaa123122.settings')
import django
django.setup()
from notes.models import Note

notes = Note.objects.all()
print('Total notes:', notes.count())
for n in notes:
    print(f'ID: {n.id}, Title: {n.title}, Content len: {len(n._content)}')
    if n._content:
        print(f'  Decrypted: {repr(n.content)}')