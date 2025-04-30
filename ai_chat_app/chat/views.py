from django.shortcuts import redirect, render, get_object_or_404
from . import models
from . import forms


def chat(request, chat_uuid):
    chat = get_object_or_404(models.Chat, pk=chat_uuid)
    mock_user = models.User.objects.get(pk=1)

    if request.method == 'POST':
        form = forms.CreateMessageForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            message = models.Message(chat=chat, user=mock_user, text=text)
            message.save()

    context = {
        'title': chat.title,
        'messages': chat.messages.all(),
        'chats': mock_user.chats.all(),
        'current_chat_id': chat.id,
        'form': forms.CreateMessageForm()
    }

    return render(request, 'chat/chat.html', context)


def start_new_chat(request):
    mock_user = models.User.objects.get(pk=1)
    chat = models.Chat.objects.create(user=mock_user)
    return redirect(f'/chat/{chat.id}')
