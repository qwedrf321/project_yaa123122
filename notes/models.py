from django.db import models
from django.contrib.auth.models import User
from folders.models import Folder

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
