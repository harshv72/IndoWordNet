from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
from django.db.models import Q
# from indoWordNet.models import TblAllWords,TblAllSynset,EnglishHindiIdMapping,EnglishSynsetData,TblOntoMap,TblOntoNodes,TblOntoData,EnglishSynsetData1
# from indoWordNet.models import TblAllAssameseSynsetData,TblAllBengaliSynsetData,TblAllBodoSynsetData,TblAllGujaratiSynsetData,TblAllHindiSynsetData
import indoWordNet.models as m
import base64
# Create your views here.

def index(request):
    return render(request,'index.html',context=None)


def regionalData(allData,word,lang):
    wordList=[]
    length = 0
    for i in allData:
        if lang == '11':
            li = i.synset.split(',')
        else:
            li = i.synset.decode('UTF-8').split(', ')

        if word in li:
            length = length + 1
            l=[]
            l.append(str(i.synset_id))
            l.append(str(i.category))
            
            synonuyms = li
            l.append(synonuyms)
            if lang in ['11','17','18']:
                l.append(i.gloss.decode('UTF-8').split(':'))
            else:
                l.append(i.gloss.decode('UTF-8').split(';'))

            try:
                enId = m.EnglishHindiIdMapping.objects.using('region').get(hindi_id = str(i.synset_id))
                glossEN = m.EnglishSynsetData.objects.using('region').filter(synset_id = str(enId.english_id))[0]
                l.append(str(glossEN.gloss))
            except m.EnglishHindiIdMapping.DoesNotExist:
                l.append('English Linkage Not Available')
            gloss = m.TblAllSynset.objects.filter(synset_id = str(i.synset_id))[0]
            l.append(gloss.gloss.decode('UTF-8').split(':')[0])
               
            wordList.append(l)
    return wordList,length
    


def wordnet(request):
    word = str(request.GET.get('query'))
    lang = str(request.GET.get('langno'))
    length = 0
    wordList=[]
  
    if lang == '0':
        synset = m.TblAllWords.objects.filter(word = word)
        length = len(synset)
        for i in synset:
            l=[]
            s=[]
            l.append(str(i.synset_id))
            l.append(str(i.pos))
            synonuyms = m.TblAllWords.objects.filter(synset_id = str(i.synset_id))
            gloss = m.TblAllSynset.objects.filter(synset_id = str(i.synset_id))[0]
            for j in synonuyms:
                s.append(str(j.word))
            l.append(s)
            l.append(gloss.gloss.decode('UTF-8').split(':'))
            try:
                enId = m.EnglishHindiIdMapping.objects.using('region').get(hindi_id = str(i.synset_id))
                glossEN = m.EnglishSynsetData.objects.using('region').filter(synset_id = str(enId.english_id))[0]
                l.append(str(glossEN.gloss))
            except m.EnglishHindiIdMapping.DoesNotExist:
                l.append('English Linkage Not Available')
            wordList.append(l)

    elif lang == '1':
        data = m.EnglishSynsetData.objects.using('region').all()
        for i in data:
            if word in i.synset_words.split(', '):
                print(str(i.synset_id))
                hindiId = m.EnglishHindiIdMapping.objects.using('region').filter(english_id = str(i.synset_id))
                for j in hindiId:
                    length = length + 1
                    l=[]
                    l.append(str(j.hindi_id))
                    l.append(str(j.hindi_category))
                    synonuyms = i.synset_words.split(', ')
                    l.append(synonuyms)
                    l.append(i.gloss.split(';'))
                    l.append(str(i.gloss))
                    l.append(m.TblAllHindiSynsetData.objects.using('region').filter(synset_id = str(j.hindi_id))[0].gloss.decode('UTF-8').split(':')[0])
                    print(*l,sep = "\n")
                    wordList.append(l)
    
    elif lang == '2':
        data = m.TblAllAssameseSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
        
    elif lang == '3':
        data = m.TblAllBengaliSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
        
    elif lang == '4':
        data = m.TblAllBodoSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '5':
        data = m.TblAllGujaratiSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)

    elif lang == '6':
        data = m.TblAllKannadaSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
        
    elif lang == '7':
        data = m.TblAllKashmiriSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '8':
        data = m.TblAllKonkaniSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '9':
        data = m.TblAllMalayalamSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '10':
        data = m.TblAllManipuriSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '11':
        data = m.TblAllMarathiSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '12':
        data = m.TblAllNepaliSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '13':
        data = m.TblAllSanskritSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '14':
        data = m.TblAllTamilSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '15':
        data = m.TblAllTeluguSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '16':
        data = m.TblAllPunjabiSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '17':
        data = m.TblAllUrduSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)
    
    elif lang == '18':
        data = m.TblAllOriyaSynsetData.objects.using('region').all()
        wordList,length = regionalData(data,word,lang)

    return render(request,'wordnet.html', {'query':word,'langno':lang,'length':length,'wordList':wordList})

def onto(request):
    synset_id = request.GET.get('synset_id',None)
    #Fetching node id
    i = m.TblOntoNodes.objects.filter(synset_id= synset_id)[0].onto_nodes_id
    
    #Fetching Parent Ids
    onto_ids=[]
    while(i != 1):
        onto_ids.append(i)
        i = m.TblOntoMap.objects.filter(child_id = str(i))[0].parent_id
    #print(onto_ids)

    #Fetching description and data
    data = {}
    j=0
    for i in onto_ids:
        l = []
        onto_data = m.TblOntoData.objects.filter(onto_id= str(i))[0]
        l.append(onto_data.onto_id)
        l.append(onto_data.onto_data)
        l.append(onto_data.onto_desc)
        data[j]=l
        j=j+1
    data["length"]=j
    onto_data_json = json.dumps(data,ensure_ascii=False)
    

    return JsonResponse(onto_data_json,safe=False)

# def recomendation(langn):
    


def word(request):
    q = str(request.GET.get('q',None) ) 
    langno = int(request.GET.get('langno',None))
    pri
    if langno == 0:
        wordData = list(m.TblAllWords.objects.values_list('word', flat=True).filter(word__startswith = q))[0:10]
    elif langno == 5:
        wordData = list(m.EnglishSynsetData1.objects.using('region').values_list('synset_words', flat=True).filter(synset_words__istartswith = q))[0:10]
    print(wordData)
    wordList = json.dumps(wordData,ensure_ascii=False)
    
    return JsonResponse(wordList,safe=False)

def feedBack(request):
    return render(request,'index.html#feedBack',context=None)

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)
