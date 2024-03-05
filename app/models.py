from django.db import models
import uuid
from django.contrib.auth.models import User
from django_bleach.models import BleachField

class Workspace(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='workspaces')
    def __str__(self):
        return self.name

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    content = BleachField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True)
    trashed = models.BooleanField(default=False)

    def __str__(self):
        return self.title