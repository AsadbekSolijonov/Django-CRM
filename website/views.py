from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from website.forms import RegistrationModelForm


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('index')
        else:
            messages.error(request, "Wrong username or password!")
            return redirect('index')
    else:
        return render(request, 'website/index.html', {})


def logout_user(request):
    logout(request)
    messages.warning(request, 'You are now logged out!')
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegistrationModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            pass

    else:
        form = RegistrationModelForm()
    context = {
        "form": form
    }
    return render(request, 'website/register.html',  context)

