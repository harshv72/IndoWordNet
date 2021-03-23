from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
from indoWordNet.models import TblAllWords,TblAllSynset,EnglishHindiIdMapping,EnglishSynsetData,TblOntoMap,TblOntoNodes,TblOntoData,TblNounHyponymy,TblVerbHypernymy,TblNounHypernymy,TblVerbDerivedFrom,TblAdjectiveDerivedFrom,TblNounDerivedFrom,TblAdverbDerivedFrom,TblNounMeroComponentObject,TblAdjectiveModifiesNoun,TblAdverbModifiesVerb
import base64
# Create your views here.

def index(request):
    return render(request,'index.html',context=None)

def wordnet(request):
    word = str(request.GET.get('query'))
    synset = TblAllWords.objects.filter(word = word)
    length = len(synset)
    wordList=[]
    print('-'*100)
    id_i=TblAdjectiveModifiesNoun.objects.filter(synset_id=118).values()
    print(id_i)
    print('-'*100)

#------------------------------------------------------
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
        #hyponymy()

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

def hyponymy(request):
    synset_id = request.GET.get('synset_id',None)
    i=TblNounHyponymy.objects.filter(synset_id=synset_id).values()
    hy_id=[] #stores hyponymy id's
    data_list=[]
    
    #fetching hyponymmy id's
    for value in i:
        hy_id.append(value['hyponymy_id'])
    
    #fetching data
    for j in hy_id:
        l=[]
        s=[]
        l.append(j)
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
    print(data_list)
    hypo_data_json=json.dumps(data_list,ensure_ascii=False)

    return JsonResponse(hypo_data_json,safe=False)

def hypernymy(request):
    synset_id = request.GET.get('synset_id',None)
    pos=TblAllSynset.objects.filter(synset_id=synset_id).values('category')[0]['category']
    
    # selecting hypernymy table based on pos
    if(pos=='noun'):
        i=TblNounHypernymy.objects.filter(synset_id=synset_id).values()
    else:
        i=TblVerbHypernymy.objects.filter(synset_id=synset_id).values()
    hyper_id=[] # stores hypernymy id's
    data_list=[]
    
    #fetching hypernym id's
    while(len(i)!=0):
        hyper_id.append(i[0]['hypernymy_id'])
        if(pos=='noun'):
            i=TblNounHypernymy.objects.filter(synset_id=i[0]['hypernymy_id']).values()
        else:
            i=TblVerbHypernymy.objects.filter(synset_id=i[0]['hypernymy_id']).values()
    print("id",hyper_id)
    
    #fetching data
    for j in hyper_id:
        l=[]
        s=[]
        l.append(j)
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
    hyper_data_json=json.dumps(data_list,ensure_ascii=False)

    return JsonResponse(hyper_data_json,safe=False)

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

#def holonymy(request):
    synset_id=request.GET.get('synset_id',None)




def feedBack(request):
    return render(request,'index.html#feedBack',context=None)

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)
