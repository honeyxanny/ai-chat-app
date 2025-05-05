from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user
from . import models
from . import forms


def chat(request, chat_uuid):
    chat = get_object_or_404(models.Chat, pk=chat_uuid)
    user = get_user(request)

    if request.method == 'POST':
        form = forms.MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.user = user
            message.chat = chat
            message.save()

    context = {
        'title': chat.title,
        'messages': chat.messages.all(),
        'chats': user.chats.all(),
        'current_chat_id': chat.id,
        'form': forms.MessageForm(initial={
            'user': user,
            'chat': chat.id,
        })
    }

    return render(request, 'chat/conversation.html', context)


def start_new_chat(request):
    mock_user = models.User.objects.get(pk=1)
    chat = models.Chat.objects.create(user=mock_user)
    return redirect(f'/chat/{chat.id}')


def start_page(request):
    user = get_user(request)

    context = {
        'chats': user.chats.all(),
        'form': forms.MessageForm()
    }

    return render(request, 'chat/start.html', context)
