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


def regionalData(allData,word,tlang):
    wordList=[]
    length = 0
    #print(type(allData))
    for i in allData:
        #print(type(i))
        if tlang != "11":
            synonuyms = i.synset.decode('UTF-8').split(', ')
        else:
            synonuyms = i.synset.split(',')
        #print(synonuyms)
        if word in synonuyms:
            #print("word:" + word)
            #print(synonuyms)
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
                #print("in catch")
            #print("after try")
            gloss = m.TblAllSynset.objects.filter(synset_id = str(i.synset_id))[0]
            l.append(gloss.gloss.decode('UTF-8').split(':')[0])
            
            #print(l)   
            wordList.append(l)
        #else:
            #print("word na malyo")
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
        # english_id =  m.EnglishHindiIdMapping.objects.using('region').filter(hindi_id = str(synset_id))
        # print(english_id)

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

def hyponymy(request):
    synset_id = request.GET.get('synset_id',None)
    langno = request.GET.get('langno')
    i=m.TblNounHyponymy.objects.filter(synset_id=synset_id).values()
    hy_id=[] #stores hyponymy id's
    data_list=[]
    
    #fetching hyponymmy id's
    for value in i:
        hy_id.append(value['hyponymy_id'])
    
    #fetching data
    data={}
    j=0
    #fetching data
    for k in hy_id:
        l=[]
        synset = searchSynsetDataById(k,langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        print(synset["gloss"])
        l.append(synset["gloss"])
        # l.append(synset["gloss"][1])
        l.append(synset["pos"])
        data[j]=l
        j = j+1

    data["length"]=j
    hypo_data_json = json.dumps(data,ensure_ascii=False)

    return JsonResponse(hypo_data_json,safe=False)
    # for j in hy_id:
    #     l=[]
    #     s=[]
    #     l.append(j)
    #     synonuyms = TblAllWords.objects.filter(synset_id = j)
    #     gloss = TblAllSynset.objects.filter(synset_id = j)[0]
    #     for k in synonuyms:
    #         s.append(str(k.word))
    #     l.append(s)
    #     data = gloss.gloss
    #     data = data.decode('UTF-8')
    #     data = data.split(':')
    #     l.append(data)
    #     data_list.append(l)
    # print(data_list)
    # hypo_data_json=json.dumps(data_list,ensure_ascii=False)

    return JsonResponse(hypo_data_json,safe=False)

def hypernymy(request):
    synset_id = request.GET.get('synset_id',None)
    langno = request.GET.get('langno')
    pos = request.GET.get('pos',None)
    #pos=TblAllSynset.objects.filter(synset_id=synset_id).values('category')[0]['category']
    # selecting hypernymy table based on pos
    if(pos=='noun'):
        i=m.TblNounHypernymy.objects.filter(synset_id=synset_id).values()
    else:
        i=m.TblVerbHypernymy.objects.filter(synset_id=synset_id).values()
    hyper_id=[] # stores hypernymy id's
    
    #fetching hypernym id's
    while(len(i)!=0):
        hyper_id.append(i[0]['hypernymy_id'])
        if(pos=='noun'):
            i=m.TblNounHypernymy.objects.filter(synset_id=i[0]['hypernymy_id']).values()
        else:
            i=m.TblVerbHypernymy.objects.filter(synset_id=i[0]['hypernymy_id']).values()
    print("id",hyper_id)
    
    data={}
    j=0
    #fetching data
    for k in hyper_id:
        l=[]
        synset = searchSynsetDataById(k,langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        # l.append(synset["gloss"][1])
        l.append(synset["pos"])
        data[j]=l
        j = j+1

    data["length"]=j
    hyper_data_json = json.dumps(data,ensure_ascii=False)

    return JsonResponse(hyper_data_json,safe=False)

        # l=[]
        # s=[]
        # l.append(j)
        # synonuyms = TblAllWords.objects.filter(synset_id = j)
        # gloss = TblAllSynset.objects.filter(synset_id = j)[0]
        # for k in synonuyms:
        #     s.append(str(k.word))
        # l.append(s)
        # data = gloss.gloss
        # data = data.decode('UTF-8')
        # data = data.split(':')
        # l.append(data)
        # data_list.append(l)
    # print("data_list",data_list)
    # hyper_data_json=json.dumps(data_list,ensure_ascii=False)

    # return JsonResponse(hyper_data_json,safe=False)

def derivedform(request):
    synset_id=request.GET.get('synset_id',None)
    pos=TblAllSynset.objects.filter(synset_id=synset_id).values('category')[0]['category']
    der_id=None

    # geting derived_from_id based on pos
    if(pos=='noun'):
        der_id=TblNounDerivedFrom.objects.filter(synset_id=synset_id).values('derived_from_id')[0]['derived_from_id']
    elif(pos=='adverb'):
        der_id=TblAdverbDerivedFrom.objects.filter(synset_id=synset_id).values('derived_from_id')[0]['derived_from_id']
    elif(pos=='verb'):
        der_id=TblVerbDerivedFrom.objects.filter(synset_id=synset_id).values('derived_from_id')[0]['derived_from_id']
    elif(pos=='adjective'):
        der_id=TblAdjectiveDerivedFrom.objects.filter(synset_id=synset_id).values('derived_from_id')[0]['derived_from_id']
    else:
        der_id=None
    
    #fetching data
    l=[]
    s=[]
    l.append(der_id)
    synonuyms = TblAllWords.objects.filter(synset_id = der_id)
    gloss = TblAllSynset.objects.filter(synset_id = der_id)[0]
    for k in synonuyms:
        s.append(str(k.word))
    l.append(s)
    data = gloss.gloss
    data = data.decode('UTF-8')
    data = data.split(':')
    l.append(data)

    print(l)
    derived_data_json=json.dumps(l,ensure_ascii=False)

    return JsonResponse(derived_data_json,safe=False)

def modifies(request):
    synset_id=request.GET.get('synset_id',None)
    pos=TblAllSynset.objects.filter(synset_id=synset_id).values('category')[0]['category']
    flag=None
    mod_id=[]
    data_list=[]

    print("hii")

    if(pos=='adjective'):
        id_i=TblAdjectiveModifiesNoun.objects.filter(synset_id=synset_id).values()
        flag="modifies_noun_id"
    elif(pos=='adverb'):
        id_i=TblAdverbModifiesVerb.objects.filter(synset_id=synset_id).values()
        flag="modifies_verb_id"
    else:
        id_i=[]
    
    if(len(id_i)>0):
        for i in id_i:
            mod_id.append(i[flag])
    
    for j in mod_id:
        l=[]
        s=[]
        l.append(j)
        l.append(flag[:-3])
        synonuyms = TblAllWords.objects.filter(synset_id = j)
        gloss = TblAllSynset.objects.filter(synset_id = j)[0]
        for k in synonuyms:
            s.append(str(k.word))
        l.append(s)
        data = gloss.gloss
        data = data.decode('UTF-8')
        data = data.split(':')
        l.append(data)
        data_list.append(l)
    print("data_list",data_list)
    modifies_data_json=json.dumps(data_list,ensure_ascii=False)

    return JsonResponse(modifies_data_json,safe=False)



def word(request):
    q = str(request.GET.get('q',None) ) 
    langno = int(request.GET.get('langno',None))
    
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
