from django.http import HttpResponse
from django.shortcuts import render
from app_users.forms import AuthForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Вы успешно вошли в систему")
                else:
                    auth_form.add_error('__all__', "Ошибка! Учетная запись пользователя не активна!")
            else:
                auth_form.add_error('__all__', "Ошибка! Проверьте правильность написания логина и пароля!")
    else:
        auth_form = AuthForm
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)
