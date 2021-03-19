"""iwn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib import admin
from indoWordNet import views
urlpatterns = [
    path('',views.index,name='index'),
    path('wordnet',views.wordnet,name='wordnet'),
    path('home',views.index,name='index'),
    path('home#contactUs',views.contactUs,name='contactUs'),
    path('home#feedBack',views.feedBack,name='feedBack'),
    path('fetch_onto',views.onto,name='onto'),
    path('word',views.word,name='word')
]
