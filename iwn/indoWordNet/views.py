from django.shortcuts import render
from django.views.generic import TemplateView
from indoWordNet.models import TblAllWords,TblAllSynset,EnglishHindiIdMapping,EnglishSynsetData
import base64
# Create your views here.

def index(request):
    return render(request,'index.html',context=None)

def wordnet(request):
    word = str(request.GET.get('query'))
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
        data = gloss.gloss
        data = data.decode('UTF-8')
        data = data.split(':')
        l.append(data)
        try:
            enId = EnglishHindiIdMapping.objects.using('region').get(hindi_id = str(i.synset_id))
            glossEN = EnglishSynsetData.objects.using('region').filter(synset_id = str(enId.english_id))[0]
            l.append(str(glossEN.gloss))
        except EnglishHindiIdMapping.DoesNotExist:
            l.append('English Linkage Not Available')
        
        wordList.append(l)
    return render(request,'wordnet.html', {'query':word,'length':length,'wordList':wordList})

def feedBack(request):
    return render(request,'index.html#feedBack',context=None)

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)


