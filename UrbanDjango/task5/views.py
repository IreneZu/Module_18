from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        users = ['abdulay1', 'regine12', 'maxim123']
        info['error'] = ''

        name = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif name in users:
            info['error'] = 'Пользователь уже существует'
        else:
            resp = f'<h1>Приветствуем, {name} !</h1>'
            return HttpResponse(resp, content_type="text/html; charset=utf-8")

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django (request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            users = ['abdulay1', 'regine12', 'maxim123']
            info = {
                'error' : '',
                'form' : form
            }
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif name in users:
            info['error'] = 'Пользователь уже существует'
        else:
            resp = f'<h1>Приветствуем, {name} !</h1>'
            return HttpResponse(resp, content_type="text/html")
    else:

        form = UserRegister()

    info['form'] = form

    return render(request, 'fifth_task/registration_page.html', info)

