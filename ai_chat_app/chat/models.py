import uuid
from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Новый чат")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name="messages"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
