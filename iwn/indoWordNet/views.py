from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    return render(request,'index.html',context=None)

def wordnet(request):
    return render(request,'wordnet.html', context=None)

def feedBack(request):
    return render(request,'index.html#feedBack',context=None)

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)

