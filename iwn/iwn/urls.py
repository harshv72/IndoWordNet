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
    path('fetch_synset',views.fetchSynset,name='fetchSynset'),
    path('fetch_derivedFrom',views.derivedFrom,name='derivedFrom'),
    path('fetch_modifies',views.modifies,name='modifies'),
    path('fetch_holonymy',views.holonymy,name='holonymy'),
    path('fetch_meronymy',views.meronymy,name='meronymy'),
    path('fetch_antonymy',views.antonymy,name='antonymy'),
    path('fetch_hypernymy',views.hypernymy,name='hypernymy'),
    path('fetch_hyponymy',views.hyponymy,name='hyponymy'),
    path('fetch_ontology',views.ontonymy,name='ontology'),
    path('word',views.word,name='word')
]

