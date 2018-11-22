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
