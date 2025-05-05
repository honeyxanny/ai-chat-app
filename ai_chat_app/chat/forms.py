from django import forms
from . import models


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'] = forms.CharField(
            label='',
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control shadow-none border-0 bg-transparent p-0 overflow-auto',
                    'placeholder': 'Введите текст...',
                    'style': 'resize: none;',
                    'rows': 3
                }
            )
        )
