from django.shortcuts import render,redirect,render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from gui.models import Textmessage,Resultcounter
from django.contrib.auth.forms import UserCreationForm


def index(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username)
    if(R_counter.count()== 0):
        Resultcounter.objects.create(user = request.user.username, counter = 0)
    return render(request,'jackproj.html',locals())
def fire(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username,D_fire = False)
    if(R_counter.count() != 0):
        r = Resultcounter.objects.get(user = request.user.username)
        R_counter.update(counter =r.counter+1 , D_fire = True)
    return render(request,'fire.html',locals())
def fight(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username,D_fight= False)
    if(R_counter.count() != 0):
        r = Resultcounter.objects.get(user = request.user.username)
        R_counter.update(counter = r.counter+1 , D_fight = True)
    return render(request,'fight.html',locals())
def stone(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username,D_stone = False)
    if(R_counter.count() != 0):
        r = Resultcounter.objects.get(user = request.user.username)
        R_counter.update(counter = r.counter+1 , D_stone = True)
    return render(request,'stone.html',locals())
def money(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username,D_moneyless = False)
    if(R_counter.count() != 0):
        r = Resultcounter.objects.get(user = request.user.username)
        R_counter.update(counter = r.counter+1 , D_moneyless = True)
    return render(request,'money.html',locals())
def bamboo(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username,D_blue = False)
    if(R_counter.count() != 0):
        r = Resultcounter.objects.get(user = request.user.username)
        R_counter.update(counter = r.counter+1 , D_blue = True)
    return render(request,'bamboo.html',locals())
def germ(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username,D_germ = False)
    if(R_counter.count() != 0):
        r = Resultcounter.objects.get(user = request.user.username)
        R_counter.update(counter = r.counter+1 , D_germ = True)
    return render(request,'germ.html',locals())
def sun(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username,D_sunburn = False)
    if(R_counter.count() != 0):
        r = Resultcounter.objects.get(user = request.user.username)
        R_counter.update(counter = r.counter+1 , D_sunburn = True)
    return render(request,'sun.html',locals())
def sword(request):
    R_counter = Resultcounter.objects.filter(user = request.user.username,D_sword = False)
    if(R_counter.count() != 0):
        r = Resultcounter.objects.get(user = request.user.username)
        R_counter.update(counter = r.counter+1 , D_sword = True)
    return render(request,'sword.html',locals())
def home(request):
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
def restart(request):
    r = Resultcounter.objects.filter(user = request.user.username)
    r.update(counter = 0,D_fight=False,D_sword=False,D_sunburn=False,D_germ=False,D_blue=False,D_moneyless=False,D_stone=False,D_fire=False)
    return HttpResponseRedirect('/index/')