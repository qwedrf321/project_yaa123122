from django.db import models
from django.contrib.auth.models import User
from folders.models import Folder
from cryptography.fernet import Fernet # type: ignore
from django.conf import settings

fernet = Fernet(settings.SECRET_NOTE_KEY)


class Note(models.Model):
    title = models.CharField(max_length=200)
    _content = models.BinaryField(db_column='content', default=b'')  
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        related_name='notes',
        blank=True,
        null=True
    )
    file = models.FileField(upload_to='notes_files/', blank=True, null=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def content(self):
        if self._content:
            try:
                return fernet.decrypt(self._content).decode()
            except:
                # Если не удается расшифровать, предполагаем старый незашифрованный текст
                return self._content.decode('utf-8')
        return ""

    @content.setter
    def content(self, value):
        if value:
            self._content = fernet.encrypt(value.encode())
        else:
            self._content = b''

    def __str__(self):
        return self.title