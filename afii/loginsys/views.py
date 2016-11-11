from django.shortcuts import render


from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth


@csrf_protect
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request, 'loginsys/login.html', args)
    else:
        return render(request, 'loginsys/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')
