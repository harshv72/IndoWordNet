from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
from indoWordNet.models import TblAllWords,TblAllSynset,EnglishHindiIdMapping,EnglishSynsetData,TblOntoMap,TblOntoNodes,TblOntoData
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
        
        #Adding ontology data for synset
        #onto_data = ontology(str(i.synset_id))
        #l.append(onto_data)
        
        wordList.append(l)
    #print(wordList)
    return render(request,'wordnet.html', {'query':word,'length':length,'wordList':wordList})

def onto(request):
    synset_id = request.GET.get('synset_id',None)
    #Fetching node id
    i = TblOntoNodes.objects.filter(synset_id= synset_id)[0].onto_nodes_id
    
    #Fetching Parent Ids
    onto_ids=[]
    while(i != 1):
        onto_ids.append(i)
        i = TblOntoMap.objects.filter(child_id = str(i))[0].parent_id
    #print(onto_ids)

    #Fetching description and data
    data = {}
    j=0
    for i in onto_ids:
        l = []
        onto_data = TblOntoData.objects.filter(onto_id= str(i))[0]
        l.append(onto_data.onto_id)
        l.append(onto_data.onto_data)
        l.append(onto_data.onto_desc)
        data[j]=l
        j=j+1
    data["length"]=j
    onto_data_json = json.dumps(data,ensure_ascii=False)
    

    return JsonResponse(onto_data_json,safe=False)


def feedBack(request):
    return render(request,'index.html#feedBack',context=None)

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)
