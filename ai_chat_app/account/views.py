from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def user_login(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/chat')
                else:
                    error_message = 'Disabled account'
            else:
                error_message = 'Invalid login'
    else:
        form = LoginForm()

    return render(request,
                  'account/login.html',
                  {'form': form, 'error': error_message})
