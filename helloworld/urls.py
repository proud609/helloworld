"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [ 
    path('', views.home),
    path('home/', views.home),
    path('index/',views.index),
    path('logout/',views.logout),
    path('login/',views.login),
    path('register/',views.register),
    path('video_f/',views.fire),
    path('video_fight/',views.fight),
    path('video_s/',views.stone),
    path('video_m/',views.money),
    path('video_b/',views.bamboo),
    path('video_g/',views.germ),
    path('video_sun/',views.sun),
    path('video_sword/',views.sword),
    path('restart/',views.restart),
]
