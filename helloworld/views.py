from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User

 
def index(request):
	ClassList=map (str , range(100))
	return render(request, 'jackproj.html',{'ClassList':ClassList})