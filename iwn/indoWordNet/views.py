from django.shortcuts import render
from django.views.generic import TemplateView
from indoWordNet.models import TblAllWords,TblAllSynset
# Create your views here.

def index(request):
    return render(request,'index.html',context=None)

def wordnet(request):
    word = str(request.GET.get('query'))
    print(word)
    synset = TblAllWords.objects.filter(word = word)
    length = len(synset)
    wordList=[]
    
    for i in synset:
        l=[]
        s=[]
        l.append(str(i.synset_id))
        l.append(str(i.pos))
        synonuyms = TblAllWords.objects.filter(synset_id = str(i.synset_id))
        gloss = TblAllSynset.objects.filter(synset_id = str(i.synset_id))[0]
        for j in synonuyms:
            s.append(str(j.word))
        l.append(s)
        l.append(str(gloss.gloss))
        wordList.append(l)
    return render(request,'wordnet.html', {'query':word,'length':length,'wordList':wordList})

def feedBack(request):
    return render(request,'index.html#feedBack',context=None)

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)


