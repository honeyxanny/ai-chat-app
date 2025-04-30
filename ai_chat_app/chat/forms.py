from django import forms


class CreateMessageForm(forms.Form):
    text = forms.CharField(
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
