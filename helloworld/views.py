from django.shortcuts import render,redirect,render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from gui.models import Textmessage
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request,'jackproj.html',locals())

def  home(request):
    return render(request,'home.html',locals())
def login(request):
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if  user is not None and user.is_active:
        auth.login(request, user) #maintain the state of login
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',locals())