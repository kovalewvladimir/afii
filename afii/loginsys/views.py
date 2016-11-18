from django.shortcuts import render

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth


@csrf_protect
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '').lower()
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            next_page = request.COOKIES.get('auth_next_page', '/')
            return redirect(next_page)
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request, 'loginsys/login.html', args)
    else:
        next_page = request.GET.get('next', '/')
        response = render(request, 'loginsys/login.html', args)
        response.set_cookie('auth_next_page', next_page)
        return response


def logout(request):
    auth.logout(request)
    return redirect('/')
