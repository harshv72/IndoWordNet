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

def getReginalAllData(lang):
    if lang == '0':
        data = m.TblAllHindiSynsetData.objects.using('region').all()
        
    elif lang == '1':
        data = m.EnglishSynsetData.objects.using('region').all()
        
    elif lang == '2':
        data = m.TblAllAssameseSynsetData.objects.using('region').all()
        
    elif lang == '3':
        data = m.TblAllBengaliSynsetData.objects.using('region').all()
        
    elif lang == '4':
        data = m.TblAllBodoSynsetData.objects.using('region').all()
        
    elif lang == '5':
        data = m.TblAllGujaratiSynsetData.objects.using('region').all()
        
    elif lang == '6':
        data = m.TblAllKannadaSynsetData.objects.using('region').all()
        
    elif lang == '7':
        data = m.TblAllKashmiriSynsetData.objects.using('region').all()
        
    elif lang == '8':
        data = m.TblAllKonkaniSynsetData.objects.using('region').all()
        
    elif lang == '9':
        data = m.TblAllMalayalamSynsetData.objects.using('region').all()
        
    elif lang == '10':
        data = m.TblAllManipuriSynsetData.objects.using('region').all()
        
    elif lang == '11':
        data = m.TblAllMarathiSynsetData.objects.using('region').all()
        
    elif lang == '12':
        data = m.TblAllNepaliSynsetData.objects.using('region').all()
        
    elif lang == '13':
        data = m.TblAllSanskritSynsetData.objects.using('region').all()
        
    elif lang == '14':
        data = m.TblAllTamilSynsetData.objects.using('region').all()
        
    elif lang == '15':
        data = m.TblAllTeluguSynsetData.objects.using('region').all()
        
    elif lang == '16':
        data = m.TblAllPunjabiSynsetData.objects.using('region').all()
        
    elif lang == '17':
        data = m.TblAllUrduSynsetData.objects.using('region').all()
        
    elif lang == '18':
        data = m.TblAllOriyaSynsetData.objects.using('region').all()
       
    return data
    

def regionalData(allData,word,tlang):
    wordList=[]
    length = 0
    for i in allData:
        if tlang != "11":
            synonuyms = i.synset.decode('UTF-8').split(', ')
        else:
            synonuyms = i.synset.split(',')
        if word in synonuyms:
            length = length + 1
            l=[]
            l.append(str(i.synset_id))
            l.append(str(i.category))
            l.append(synonuyms)

            if tlang in ['11','17','18']:
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

def fetch_synset(request):
    synset_id = request.GET.get('synset_id',None)
    langno = request.GET.get('langno')

    data = searchSynsetDataById(synset_id,langno)
    
    synset_data_json = json.dumps(data,ensure_ascii=False)
    

    return JsonResponse(synset_data_json,safe=False)

def searchSynsetDataById(synset_id,lang):
    
    if lang == '0':
        data={}
        data["synset_id"]= str(synset_id)

        s=[]
        synonuyms = m.TblAllWords.objects.filter(synset_id = synset_id)
        data["pos"] = str(synonuyms[0].pos)
        for j in synonuyms:
            s.append(str(j.word))
        data["synonyms"] = s

        gloss = m.TblAllSynset.objects.filter(synset_id = str(synset_id))[0]
        data["gloss"] = gloss.gloss.decode('UTF-8').split(':')
        
        return data

    elif lang == '1':
        d = {}
        d["synset_id"] = synset_id

        english_id =  m.EnglishHindiIdMapping.objects.using('region').filter(hindi_id = str(synset_id))[0].english_id
        if english_id is None:
            return None
        data = m.EnglishSynsetData.objects.using('region').filter(synset_id= str(english_id))[0]
        #print(english_id)
        d["pos"]=str(data.category)
        synonuyms = data.synset_words.split(', ')
        d["synonyms"]= synonuyms
        d["gloss"]=data.gloss.split(';')
        
        return d
    
    elif lang == '2':
        data = m.TblAllAssameseSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)

    elif lang == '3':
        data = m.TblAllBengaliSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
        
    elif lang == '4':
        data = m.TblAllBodoSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '5':
        data = m.TblAllGujaratiSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)

    elif lang == '6':
        data = m.TblAllKannadaSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
        
    elif lang == '7':
        data = m.TblAllKashmiriSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '8':
        data = m.TblAllKonkaniSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '9':
        data = m.TblAllMalayalamSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '10':
        data = m.TblAllManipuriSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '11':
        data = m.TblAllMarathiSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '12':
        data = m.TblAllNepaliSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '13':
        data = m.TblAllSanskritSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '14':
        data = m.TblAllTamilSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '15':
        data = m.TblAllTeluguSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '16':
        data = m.TblAllPunjabiSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '17':
        data = m.TblAllUrduSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)
    
    elif lang == '18':
        data = m.TblAllOriyaSynsetData.objects.using('region').filter(synset_id= synset_id)[0]
        return fetch_regional_data(data,synset_id,lang)

def fetch_regional_data(data,synset_id,tlang):
    d={}
    d["synset_id"]=synset_id
    d["pos"]=data.category
    if tlang == "11":
        d["synonyms"] = data.synset.split(', ')
    else:
        d["synonyms"] = data.synset.decode('UTF-8').split(', ')
    if tlang in ['11','17','18']:
        d["gloss"]= data.gloss.decode('UTF-8').split(':')
    else:
        d["gloss"]= data.gloss.decode('UTF-8').split(';')
    
    return d

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

def recomendation(q,lang):
    wordList = []
    j = 0
    data = getReginalAllData(lang)
    for i in data:
        if lang == '0':
            words = i.synset.decode('UTF-8').split(',')
        elif lang == '11':
            words = i.synset.split(',')
        elif lang == '1':
            words = i.synset_words.split(', ')
        else:
            words = i.synset.decode('UTF-8').split(', ')
        for k in words:
            if k.startswith(q):    
                wordList.append(k)
                j = j+1
                if j == 10:
                    break
        if j == 10:
            break
    return wordList    

def word(request):
    q = str(request.GET.get('q',None) ) 
    lang = str(request.GET.get('langno',None))
   
    wordList = recomendation(q,lang)
    wordList = json.dumps(wordList,ensure_ascii=False)
    
    return JsonResponse(wordList,safe=False)

def feedBack(request):
    return render(request,'index.html#feedBack',context=None)

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)
