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
from django.urls import path, include
from django.contrib import admin
from indoWordNet import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wordnet", views.wordnet, name="wordnet"),
    path("showonto", views.showOnto, name="showonto"),
    path("home", views.index, name="index"),
    path("home#contactUs", views.contactUs, name="contactUs"),
    path("home#feedBack", views.feedBack, name="feedBack"),
    path("feedBack", views.feedBack, name="feedBack"),
    path("fetch_synset", views.fetchSynset, name="fetchSynset"),
    path("fetch_nounRelations", views.fetchNounRelations, name="nounRelations"),
    path("fetch_verbRelations", views.fetchVerbRelations, name="verbRelations"),
    path("fetch_derivedFrom", views.fetchDerivedFrom, name="derivedFrom"),
    path("fetch_modifies", views.fetchModifies, name="modifies"),
    path("fetch_holonymy", views.fetchHolonymy, name="holonymy"),
    path("fetch_meronymy", views.fetchMeronymy, name="meronymy"),
    path("fetch_antonymy", views.fetchAntonymy, name="antonymy"),
    path("fetch_hypernymy", views.fetchHypernymy, name="hypernymy"),
    path("fetch_hyponymy", views.fetchHyponymy, name="hyponymy"),
    path("fetch_ontology", views.fetchOntonymy, name="ontology"),
    path("fetch_revOnto", views.fetchReverseOntonymy, name="reverseOntonymy"),
    path("word", views.word, name="word"),
]
