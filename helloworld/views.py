from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from gui.models import Textmessage
 
def hello(request):
    return HttpResponse("Hello world ! ")
def index(request):
	t1 = Textmessage.objects.create(talker='Jack',message='Hello1')
	t2 = Textmessage.objects.create(talker='JackS',message='Hello2')
	t3 = Textmessage.objects.create(talker='JackA',message='Hello3')
	msgs = Textmessage.objects.all()
	ClassList=map (str , range(100))
	return render(request, 'jackproj.html',locals())
