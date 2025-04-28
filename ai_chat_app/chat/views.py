from django.shortcuts import redirect, render, get_object_or_404
from . import models


def chat(request, chat_uuid):
    chat = get_object_or_404(models.Chat, pk=chat_uuid)
    context = {
        'title': chat_uuid,
        'messages': chat.messages.all()
    }

    return render(request, 'chat/chat.html', context)


def start_new_chat(request):
    mock_user = models.User.objects.get(pk=1)
    chat = models.Chat.objects.create(user=mock_user)
    return redirect(f'/chat/{chat.id}')
