from django.shortcuts import redirect, render, get_object_or_404
from . import models


mock_user = models.User.objects.get(pk=1)


def chat(request, chat_uuid):
    chat = get_object_or_404(models.Chat, pk=chat_uuid)
    return render(request, 'chat/chat.html', {'chat': chat})


def start_new_chat(request):
    chat = models.Chat.objects.create(user=mock_user)
    return redirect(f'/chat/{chat.id}')
