import uuid
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        abstract = True


class Chat(BaseModel):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='chats'
    )
    title = models.CharField(max_length=100, default="Новый чат")
    modified_at = models.DateTimeField(auto_now=True)


class Message(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name="messages"
    )
    text = models.TextField()
