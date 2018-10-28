from django.shortcuts import render,redirect,render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from gui.models import Textmessage
from django.contrib.auth.forms import UserCreationForm

def delete(request):
    Textmessage.objects.all().delete()
    return HttpResponseRedirect('/index/')
def index(request):
    msgs = Textmessage.objects.all()
    if not request.user.is_authenticated: 
        return HttpResponseRedirect('/hello/')

    elif 'ok' in request.POST:
        user = request.user.username
        content = request.POST['content']
        #email = request.POST['email']
        date_time = datetime.now()     # 擷取現在時間
        Textmessage.objects.create(talker = user, message=content,talktime=date_time) 
        msgs = Textmessage.objects.all()
        ClassList=map (str , range(100))
    return render(request,'jackproj.html',locals())

def  home(request):
	return render(request,'home.html',locals())

def hello(request):
    return render_to_response('hello.html',locals())

def login(request):
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/hello/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if  user is not None and user.is_active:
        auth.login(request, user) #maintain the state of login
        return HttpResponseRedirect('/hello/')
    else:
        return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/hello/')

def admin_message(request):
    user = request.user.username
    msgs_f = Textmessage.objects.filter(talker=user)
    ClassList=map (str , range(100))
    if 'edit_h' in request.POST:
        msg_e = request.POST['content']
        data_time = request.POST['time']
        edit_msg = Textmessage.objects.filter(talktime=data_time,talker=user).update(message=msg_e,talktime=data_time)    
        return HttpResponseRedirect('/admin_message/')
    elif 'delete_h' in request.POST:
        msg_d = request.POST['content']
        data_time = request.POST['time']
        delete_msg = Textmessage.objects.filter(talktime=data_time,talker=user,message=msg_d)
        delete_msg.delete()  
        return HttpResponseRedirect('/admin_message/')

    return render(request,'admin_message.html',locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',locals())


