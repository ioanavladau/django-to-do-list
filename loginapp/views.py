from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from django.urls import reverse

def login(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(request, 
                    username=request.POST['user'],
                    password=request.POST['password']
                )
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('todoapp:index'))
        else:
            context = {'error':'Username or password is wrong.'}

    return render(request, 'loginapp/login.html', context)


def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('loginapp:login'))


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request)
            return redirect("loginapp/login.html")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "loginapp/signup.html",
                          context={"form":form})
    form = UserCreationForm
    return render(request = request,
                  template_name = "loginapp/signup.html",
                  context={"form":form})
    # if request.method == 'POST':
    #     user = User.objects.create_user
    #     user = aUser.objects.create_user() 
    #     user.last_name=request.POST['user']
    #     user.password=request.POST['password']
    #     user.save()
    #     dj_login(request, user)
    #     return HttpResponseRedirect(reverse('todoapp:index'))
    # else:
    #     return HttpResponseBadRequest()


def password_reset(request):
    pass
    