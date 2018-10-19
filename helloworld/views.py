from django.shortcuts import render,redirect,render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from gui.models import Textmessage
 
def menu(request):
    food1 = { 'name':'番茄炒蛋', 'price':60, 'comment':'好吃', 'is_spicy':False }
    food2 = { 'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True }
    foods = [food1,food2]
    return render_to_response('menu.html',locals())
def hello(request):
    return HttpResponse("Hello world ! ")
def index(request):
    if 'ok' in request.POST:
        user = request.POST['user']
        content = request.POST['content']
        #email = request.POST['email']
        #date_time = datetime.datetime.now()     # 擷取現在時間
        Textmessage.objects.create(talker = user, message=content) 
        msgs = Textmessage.objects.all()
        ClassList=map (str , range(100))
    return render(request,'jackproj.html',locals())
def  home(request):
	return render(request,'home.html',locals())
def login(request):
	return render(request,'login.html',locals())