from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
from django.db.models import Q
from django.apps import apps
# from indoWordNet.models import TblAllWords,TblAllSynset,EnglishHindiIdMapping,EnglishSynsetData,TblOntoMap,TblOntoNodes,TblOntoData,EnglishSynsetData1
# from indoWordNet.models import TblAllAssameseSynsetData,TblAllBengaliSynsetData,TblAllBodoSynsetData,TblAllGujaratiSynsetData,TblAllHindiSynsetData
import indoWordNet.models as m
import base64
import os


# Create your views here.

# Declaring GLobal Variables
appName = 'indoWordNet'
langName = ['Hindi','English','Assamese','Bengali','Bodo','Gujarati','Kannada','Kashmiri','Konkani','Malayalam','Manipuri','Marathi','Nepali','Sanskrit','Tamil','Telugu','Punjabi','Urdu','Oriya']
def index(request):
    # wordList = {}
    
    # for lang in range(19):
    #     word = []
    #     if lang == 1:
    #         tblName = "EnglishSynsetData"
    #     else:
    #         tblName = "TblAll"+langName[int(lang)]+"SynsetData"
            
    #     try:
    #         model = apps.get_model(appName,tblName)
    #     except Exception as e:
    #         print(e)
        
    #     data = model.objects.using('region').all()
    #     for i in data:
    #         if lang == 0:
    #             words = i.synset.decode('UTF-8').split(',')
    #         elif lang == 11:
    #             words = i.synset.split(',')
    #         elif lang == 1:
    #             words = i.synset_words.split(', ')
    #         else:
    #             words = i.synset.decode('UTF-8').split(', ')
    #         for k in words:
    #             word.append(k)
    #     wordList[str(lang)] = word

    # with open('words.json','w') as outfile:
    #     json.dump(wordList,outfile) 
    #     print(os.path.abspath(outfile.name))

    return render(request,'index.html',{'found':True,'suggFound': False})

    
def getCloseMatch(word,lang):
    wordList = []
    

    if lang == '1':
        tblName = "EnglishSynsetData"
        idList = []
    else:
        tblName = "TblAll"+langName[int(lang)]+"SynsetData"
        
    try:
        model = apps.get_model(appName,tblName)
    except Exception as e:
        print(e)
    
    data = model.objects.using('region').all()
    
    for i in data:
        try:
            if lang == '0':
                words = i.synset.decode('UTF-8').split(',')
            elif lang == '11':
                words = i.synset.split(',')
            elif lang == '1':
                words = i.synset_words.split(', ')
                sID = str(i.synset_id)
            else:
                words = i.synset.decode('UTF-8').split(', ')
        except Exception as e:
            print(e)


        for k in words:
            if word in k:   
                wordList.append(k)
                if lang == '1':
                    idList.append(sID)

    if len(wordList) > 10:
        l = 0
        newWordList = []
        length = len(word)
        for (i,w) in enumerate(wordList):
            length1 = len(w)
            ratio = length/length1
            # limit = ((length-1)*10+30)/100
            limit = 0
            print(w)
            try:
                if(ratio > limit):
                    if lang == '1':
                        try:
                            if m.EnglishHindiIdMapping.objects.using('region').filter(english_id = idList[i]):
                                l = l+1
                                newWordList.append(w)
                                if l == 10:
                                    return newWordList,l

                        except Exception as e:
                            print(e)
                    
                    else:
                        l = l+1
                        newWordList.append(w)
                        if l == 10:
                            return newWordList,l
            except Exception as e:
                print(e)
        return wordList,l
    else:
        
        if lang == '1':
            l=0
            newWordList = []
            for (i,w) in enumerate(wordList):
                try:
                    if m.EnglishHindiIdMapping.objects.using('region').filter(english_id = idList[i]):
                        newWordList.append(w)
                        l=l+1                       
                except Exception as e:
                    print(e)
            return newWordList,l   
        l =len(wordList)
        return wordList,l
    



def getSynsetByWord(word,lang):
    wordList=[]
    length = 0

    if lang == '1':
        try:
            data = m.EnglishSynsetData.objects.using('region').all()
        except Exception as e:
            print(e)

        for i in data:
            try:
                synonuyms = i.synset_words.split(', ')
            except Exception as e:
                print(e)
            
            if word in synonuyms:
                try:
                    hindiId = m.EnglishHindiIdMapping.objects.using('region').filter(english_id = str(i.synset_id))
                except Exception as e:
                    print(e)
                    
                
                for j in hindiId:
                    length = length + 1
                    l=[]
                    l.append(str(j.hindi_id))
                    l.append(str(j.hindi_category))
                    l.append(synonuyms)
                    
                    try:
                        gloss = i.gloss.split(';')
                        if len(gloss) == 1:
                            gloss.append("Example statement not available")
                            l.append(gloss)
                        else:
                            l.append(gloss)
                    except Exception as e:
                        l.append(str(i.gloss))
                    
                    l.append(str(i.gloss))
                    
                    try:
                        l.append(m.TblAllHindiSynsetData.objects.using('region').filter(synset_id = str(j.hindi_id))[0].gloss.decode('UTF-8').split(':')[0])
                    except Exception as e:
                        print(e)
                    
                    wordList.append(l)


    else:
        if lang == '0':
            tblName = "TblAllWords"
        else:
            tblName = "TblAll"+langName[int(lang)]+"SynsetData"
        
        try:
            model = apps.get_model(appName,tblName)
        except Exception as e:
            print(e)

        try:
            if lang == '0':
                data = model.objects.filter(word = word).order_by('sense_num')
            else:
                data = model.objects.using('region').all()
        except Exception as e:
            print(e)


        for i in data:
            try:
                if lang == '0':
                    i = m.TblAllSynset.objects.get(synset_id = str(i.synset_id))
               
                if lang == "11":
                    synonuyms = i.synset.split(',')
                else:
                    synonuyms = i.synset.decode('UTF-8').replace(', ',',').split(',')
            except Exception as e:
                print(e)

            if word in synonuyms:
                length = length + 1
                l=[]
                l.append(str(i.synset_id))
                l.append(str(i.category))
                l.append(synonuyms)
                
                try:
                    gloss = i.gloss.decode('UTF-8').replace(':',';')
                    gloss = gloss.split(';')
                    if len(gloss) == 1:
                        gloss.append("Example statement not available")
                    l.append(gloss)
                except Exception as e:
                    print(e)
                    l.append(i.gloss.decode('UTF-8'))
                
                try:
                    enId = m.EnglishHindiIdMapping.objects.using('region').get(hindi_id = str(i.synset_id))
                    glossEN = m.EnglishSynsetData.objects.using('region').filter(synset_id = str(enId.english_id))
                    l.append(str(glossEN[0].gloss))
                except m.EnglishHindiIdMapping.DoesNotExist:
                    l.append('English Linkage Not Available')

                try:                
                    gloss = m.TblAllSynset.objects.filter(synset_id = str(i.synset_id))[0]
                    l.append(gloss.gloss.decode('UTF-8').split(':')[0])
                except Exception as e:
                    print(e)
                wordList.append(l)
            
    return wordList,length
    

def getSynsetByID(sID,lang):
    data={}
    data['synset_id']= str(sID)

    if lang == '1':
        tblName = "EnglishSynsetData"
    else:
        tblName = "TblAll"+langName[int(lang)]+"SynsetData"
        
    try:
        model = apps.get_model(appName,tblName)
    except Exception as e:
        print(e)

    try:
        if lang == '0':
            i = m.TblAllSynset.objects.get(synset_id = str(sID))
        elif lang == '1':
            englishId = m.EnglishHindiIdMapping.objects.using('region').get(hindi_id = str(sID))
            i = model.objects.using('region').get(synset_id = str(englishId.english_id))
        else:
            i = model.objects.using('region').get(synset_id = str(sID))

        if lang == '1':    
            synonuyms = i.synset_words.split(',')
        elif lang == "11":
            synonuyms = i.synset.split(',')
        else:
            synonuyms = i.synset.decode('UTF-8').replace(', ',',').split(',')
            
    except Exception as e:
        print(e)
        data['pos']=''
        data['synonyms'] = []
        data['gloss'] = ['','']
        return

    data['pos'] = str(i.category)

    data["synonyms"] = synonuyms

    try:
        if lang == '1':
            gloss = i.gloss.replace(':',';')  
        else:  
            gloss = i.gloss.decode('UTF-8').replace(':',';')  
        
        
        
        data['gloss'] = gloss.split(';')
    except Exception as e:
        print(e)
        gloss = i.gloss.decode('UTF-8')
        
    gloss = gloss.split(';')
    if len(gloss) == 1:
        gloss.append("Example statement not available")
        data['gloss'] = gloss
    else:
        data['gloss'] = gloss

    return data

def wordnet(request):
    word = str(request.GET.get('query'))
    lang = str(request.GET.get('langno'))
    length = 0
    wordList=[]
    wordList,length = getSynsetByWord(word,lang)
   
    if length == 0:
        suggWord,l= getCloseMatch(word,lang)
        if(l != 0):
            return render(request,'index.html',{'query':word,'found':False,'suggWord':suggWord,'suggFound' : True,'langno':lang})
        else:
            return render(request,'index.html',{'query':word,'found':False,'suggWord':suggWord,'suggFound' : False,'langno':lang})
    return render(request,'wordnet.html', {'query':word,'langno':lang,'length':length,'wordList':wordList})

def fetchSynset(request):
    synset_id = request.GET.get('synset_id',None)
    langno = request.GET.get('langno')

    data = getSynsetByID(synset_id,langno)
    # data = searchSynsetDataById(synset_id,langno)
    
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

def ontonymy(request):
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


def derivedFrom(request):
    synset_id=request.GET.get('synset_id',None)
    langno = request.GET.get('langno',None)
    pos = request.GET.get('pos',None)
    #pos=m.TblAllSynset.objects.filter(synset_id=synset_id).values('category')[0]['category']
    der_id=None

    # geting derived_from_id based on pos
    if(pos=='noun'):
        der_id=m.TblNounDerivedFrom.objects.filter(synset_id=synset_id).values('derived_from_id')
        # [0]['derived_from_id']
    elif(pos=='adverb'):
        der_id=m.TblAdverbDerivedFrom.objects.filter(synset_id=synset_id).values('derived_from_id')
    elif(pos=='verb'):
        print("in verb")
        der_id=m.TblVerbDerivedFrom.objects.filter(synset_id=synset_id).values('derived_from_id')
    elif(pos=='adjective'):
        der_id=m.TblAdjectiveDerivedFrom.objects.filter(synset_id=synset_id).values('derived_from_id')
    else:
        der_id=None
    print(der_id, langno)
    data={}
    j=0
    #fetching data
    for k in der_id:
        l=[]
        synset = searchSynsetDataById(k["derived_from_id"],langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        print(synset["gloss"])
        l.append(synset["gloss"])
        # l.append(synset["gloss"][1])
        l.append(synset["pos"])
        data[j]=l
        j = j+1

    data["length"]=j
    derived_data_json = json.dumps(data,ensure_ascii=False)

    #fetching data
    # l=[]
    # s=[]
    # l.append(der_id)
    # synonuyms = m.TblAllWords.objects.filter(synset_id = der_id)
    # gloss = m.TblAllSynset.objects.filter(synset_id = der_id)[0]
    # for k in synonuyms:
    #     s.append(str(k.word))
    # l.append(s)
    # data = gloss.gloss
    # data = data.decode('UTF-8')
    # data = data.split(':')
    # l.append(data)

    # print(l)
    # derived_data_json=json.dumps(l,ensure_ascii=False)

    return JsonResponse(derived_data_json,safe=False)

def modifies(request):
    synset_id=request.GET.get('synset_id',None)
    langno = request.GET.get('langno',None)
    pos = request.GET.get('pos',None)
    
    # pos=m.TblAllSynset.objects.filter(synset_id=synset_id).values('category')[0]['category']
    flag=None
    mod_id=[]
    data_list=[]

    # print("hii")
    text=""
    if(pos=='adjective'):
        id_i=m.TblAdjectiveModifiesNoun.objects.filter(synset_id=synset_id).values()
        flag="modifies_noun_id"
        text = "Modifies noun"
    elif(pos=="adverb"):
        id_i=m.TblAdverbModifiesVerb.objects.filter(synset_id=synset_id).values()
        flag="modifies_verb_id"
        text = "Modifies verb"
    else:
        id_i=[]
    
    if(len(id_i)>0):
        for i in id_i:
            mod_id.append(i[flag])
    #print(mod_id)
    data={}
    j=0
    #fetching data
    for k in mod_id:
        l=[]
        synset = searchSynsetDataById(k,langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        print(synset["gloss"])
        l.append(synset["gloss"])
        # l.append(synset["gloss"][1])
        l.append(synset["pos"])
        l.append(text)
        data[j]=l
        j = j+1

    data["length"]=j
    modifies_data_json = json.dumps(data,ensure_ascii=False)
    # for j in mod_id:
    #     l=[]
    #     s=[]
    #     l.append(j)
    #     l.append(flag[:-3])
    #     synonuyms = m.TblAllWords.objects.filter(synset_id = j)
    #     gloss = m.TblAllSynset.objects.filter(synset_id = j)[0]
    #     for k in synonuyms:
    #         s.append(str(k.word))
    #     l.append(s)
    #     data = gloss.gloss
    #     data = data.decode('UTF-8')
    #     data = data.split(':')
    #     l.append(data)
    #     data_list.append(l)
    # print("data_list",data_list)
    # modifies_data_json=json.dumps(data_list,ensure_ascii=False)

    return JsonResponse(modifies_data_json,safe=False)

def holonymy(request):
    synset_id=request.GET.get('synset_id',None)
    langno = request.GET.get('langno',None)
    holo_lis=[]
    data_lis=[]
    com_id=m.TblNounHoloComponentObject.objects.filter(synset_id=synset_id).values()
    feat_id=m.TblNounHoloFeatureActivity.objects.filter(synset_id=synset_id).values()
    mem_col=m.TblNounHoloMemberCollection.objects.filter(synset_id=synset_id).values()
    ph_state=m.TblNounHoloPhaseState.objects.filter(synset_id=synset_id).values()
    pl_ar=m.TblNounHoloPlaceArea.objects.filter(synset_id=synset_id).values()
    por_mas=m.TblNounHoloPortionMass.objects.filter(synset_id=synset_id).values()
    pos_area=m.TblNounHoloPositionArea.objects.filter(synset_id=synset_id).values()
    res_pro=m.TblNounHoloResourceProcess.objects.filter(synset_id=synset_id).values()
    st_ob=m.TblNounHoloStuffObject.objects.filter(synset_id=synset_id).values()

    if(len(com_id)>0):
        for i in com_id:
            temp=[]
            temp.append(i['holo_component_object_id'])
            temp.append('holonymy component_object')
            holo_lis.append(temp)
    
    if(len(feat_id)>0):
        for i in feat_id:
            temp=[]
            temp.append(i['holo_feature_activity_id'])
            temp.append('holonymy feature_activity')
            holo_lis.append(temp)
    
    if(len(mem_col)>0):
        for i in mem_col:
            temp=[]
            temp.append(i['holo_member_collection_id'])
            temp.append('holonymy member_collection')
            holo_lis.append(temp)
    
    if(len(ph_state)>0):
        for i in ph_state:
            temp=[]
            temp.append(i['holo_phase_state_id'])
            temp.append('holonymy phase_state')
            holo_lis.append(temp)
    
    if(len(pl_ar)>0):
        for i in pl_ar:
            temp=[]
            temp.append(i['holo_place_area_id'])
            temp.append('holonymy place_area')
            holo_lis.append(temp)
    
    if(len(por_mas)>0):
        for i in por_mas:
            temp=[]
            temp.append(i['holo_portion_mass_id'])
            temp.append('holonymy portion_mass')
            holo_lis.append(temp)
    
    if(len(pos_area)>0):
        for i in pos_area:
            temp=[]
            temp.append(i['holo_position_area_id'])
            temp.append('holonymy position_area')
            holo_lis.append(temp)

    if(len(res_pro)>0):
        for i in res_pro:
            temp=[]
            temp.append(i['holo_resource_process_id'])
            temp.append('holonymy resource_process')
            holo_lis.append(temp)
    
    if(len(st_ob)>0):
        for i in st_ob:
            temp=[]
            temp.append(i['holo_stuff_object_id'])
            temp.append('holonymy stuff_object')
            holo_lis.append(temp)
    
    data={}
    j=0
    #fetching data
    for k in holo_lis:
        l=[]
        synset = searchSynsetDataById(k[0],langno)
        l.append(k[1])
        l.append(synset["synonyms"])
        print(synset["gloss"])
        l.append(synset["gloss"])
        # l.append(synset["gloss"][1])
        l.append(synset["synset_id"])
        l.append(synset["pos"])
        data[j]=l
        j = j+1

    data["length"]=j
    holonymy_data_json = json.dumps(data,ensure_ascii=False)
    # for j in holo_lis:
    #     l=[]
    #     s=[]
    #     l.append(j[0])
    #     l.append(j[1])
    #     synonuyms = m.TblAllWords.objects.filter(synset_id = j[0])
    #     gloss = m.TblAllSynset.objects.filter(synset_id = j[0])[0]
    #     for k in synonuyms:
    #         s.append(str(k.word))
    #     l.append(s)
    #     data = gloss.gloss
    #     data = data.decode('UTF-8')
    #     data = data.split(':')
    #     l.append(data)
    #     data_lis.append(l)
    # print("data_list",data_lis)
    # holonymy_data_json=json.dumps(data_lis,ensure_ascii=False)

    return JsonResponse(holonymy_data_json,safe=False)

def meronymy(request):
    synset_id=request.GET.get('synset_id',None)
    langno = request.GET.get('langno',None)
    mero_lis=[]
    data_lis=[]
    com_id=m.TblNounMeroComponentObject.objects.filter(synset_id=synset_id).values()
    feat_id=m.TblNounMeroFeatureActivity.objects.filter(synset_id=synset_id).values()
    mem_col=m.TblNounMeroMemberCollection.objects.filter(synset_id=synset_id).values()
    ph_state=m.TblNounMeroPhaseState.objects.filter(synset_id=synset_id).values()
    pl_ar=m.TblNounMeroPlaceArea.objects.filter(synset_id=synset_id).values()
    por_mas=m.TblNounMeroPortionMass.objects.filter(synset_id=synset_id).values()
    pos_area=m.TblNounMeroPositionArea.objects.filter(synset_id=synset_id).values()
    res_pro=m.TblNounMeroResourceProcess.objects.filter(synset_id=synset_id).values()
    st_ob=m.TblNounMeroStuffObject.objects.filter(synset_id=synset_id).values()

    if(len(com_id)>0):
        for i in com_id:
            temp=[]
            temp.append(i['mero_component_object_id'])
            temp.append('meronymy component_object')
            mero_lis.append(temp)
    
    if(len(feat_id)>0):
        for i in feat_id:
            temp=[]
            temp.append(i['mero_feature_activity_id'])
            temp.append('meronymy feature_activity')
            mero_lis.append(temp)
    
    if(len(mem_col)>0):
        for i in mem_col:
            temp=[]
            temp.append(i['mero_member_collection_id'])
            temp.append('meronymy member_collection')
            mero_lis.append(temp)
    
    if(len(ph_state)>0):
        for i in ph_state:
            temp=[]
            temp.append(i['mero_phase_state_id'])
            temp.append('meronymy phase_state')
            mero_lis.append(temp)
    
    if(len(pl_ar)>0):
        for i in pl_ar:
            temp=[]
            temp.append(i['mero_place_area_id'])
            temp.append('meronymy place_area')
            mero_lis.append(temp)
    
    if(len(por_mas)>0):
        for i in por_mas:
            temp=[]
            temp.append(i['mero_portion_mass_id'])
            temp.append('meronymy portion_mass')
            mero_lis.append(temp)
    
    if(len(pos_area)>0):
        for i in pos_area:
            temp=[]
            temp.append(i['mero_position_area_id'])
            temp.append('meronymy position_area')
            mero_lis.append(temp)

    if(len(res_pro)>0):
        for i in res_pro:
            temp=[]
            temp.append(i['mero_resource_process_id'])
            temp.append('meronymy resource_process')
            mero_lis.append(temp)
    
    if(len(st_ob)>0):
        for i in st_ob:
            temp=[]
            temp.append(i['mero_stuff_object_id'])
            temp.append('meronymy stuff_object')
            mero_lis.append(temp)
    
    data={}
    j=0
    #fetching data
    for k in mero_lis:
        l=[]
        synset = searchSynsetDataById(k[0],langno)
        l.append(k[1])
        l.append(synset["synonyms"])
        print(synset["gloss"])
        l.append(synset["gloss"])
        # l.append(synset["gloss"][1])
        l.append(synset["synset_id"])
        l.append(synset["pos"])
        data[j]=l
        j = j+1

    data["length"]=j
    meronymy_data_json = json.dumps(data,ensure_ascii=False)
    # for j in mero_lis:
    #     l=[]
    #     s=[]
    #     l.append(j[0])
    #     l.append(j[1])
    #     synonuyms = m.TblAllWords.objects.filter(synset_id = j[0])
    #     gloss = m.TblAllSynset.objects.filter(synset_id = j[0])[0]
    #     for k in synonuyms:
    #         s.append(str(k.word))
    #     l.append(s)
    #     data = gloss.gloss
    #     data = data.decode('UTF-8')
    #     data = data.split(':')
    #     l.append(data)
    #     data_lis.append(l)
    # print("data_list",data_lis)
    # meronymy_data_json=json.dumps(data_lis,ensure_ascii=False)

    return JsonResponse(meronymy_data_json,safe=False)

def antonymy(request):
    synset_id=request.GET.get('synset_id',None)
    langno = request.GET.get('langno',None)
    pos = request.GET.get('pos',None)
    antonymy_ids=[]
    action_id = amount_id = colour_id = direction_id = gender_id = manner_id = personality_id = place_id = quality_id = size_id = state_id = time_id = []
    if(pos == "noun"):
        action_id=m.TblNounAntoAction.objects.filter(synset_id=synset_id).values()
        amount_id=m.TblNounAntoAmount.objects.filter(synset_id=synset_id).values()
        colour_id=m.TblNounAntoColour.objects.filter(synset_id=synset_id).values()
        direction_id=m.TblNounAntoDirection.objects.filter(synset_id=synset_id).values()
        gender_id=m.TblNounAntoGender.objects.filter(synset_id=synset_id).values()
        manner_id=m.TblNounAntoManner.objects.filter(synset_id=synset_id).values()
        personality_id=m.TblNounAntoPersonality.objects.filter(synset_id=synset_id).values()
        place_id=m.TblNounAntoPlace.objects.filter(synset_id=synset_id).values()
        quality_id=m.TblNounAntoQuality.objects.filter(synset_id=synset_id).values()
        size_id=m.TblNounAntoSize.objects.filter(synset_id=synset_id).values()
        state_id=m.TblNounAntoState.objects.filter(synset_id=synset_id).values()
        time_id=m.TblNounAntoTime.objects.filter(synset_id=synset_id).values()
    elif(pos == "adjective"):
        action_id=m.TblAdjectiveAntoAction.objects.filter(synset_id=synset_id).values()
        amount_id=m.TblAdjectiveAntoAmount.objects.filter(synset_id=synset_id).values()
        colour_id=m.TblAdjectiveAntoColour.objects.filter(synset_id=synset_id).values()
        direction_id=m.TblAdjectiveAntoDirection.objects.filter(synset_id=synset_id).values()
        gender_id=m.TblAdjectiveAntoGender.objects.filter(synset_id=synset_id).values()
        manner_id=m.TblAdjectiveAntoManner.objects.filter(synset_id=synset_id).values()
        personality_id=m.TblAdjectiveAntoPersonality.objects.filter(synset_id=synset_id).values()
        place_id=m.TblAdjectiveAntoPlace.objects.filter(synset_id=synset_id).values()
        quality_id=m.TblAdjectiveAntoQuality.objects.filter(synset_id=synset_id).values()
        size_id=m.TblAdjectiveAntoSize.objects.filter(synset_id=synset_id).values()
        state_id=m.TblAdjectiveAntoState.objects.filter(synset_id=synset_id).values()
        time_id=m.TblAdjectiveAntoTime.objects.filter(synset_id=synset_id).values()
    elif(pos == "adverb"):
        action_id=m.TblAdverbAntoAction.objects.filter(synset_id=synset_id).values()
        amount_id=m.TblAdverbAntoAmount.objects.filter(synset_id=synset_id).values()
        colour_id=m.TblAdverbAntoColour.objects.filter(synset_id=synset_id).values()
        direction_id=m.TblAdverbAntoDirection.objects.filter(synset_id=synset_id).values()
        gender_id=m.TblAdverbAntoGender.objects.filter(synset_id=synset_id).values()
        manner_id=m.TblAdverbAntoManner.objects.filter(synset_id=synset_id).values()
        personality_id=m.TblAdverbAntoPersonality.objects.filter(synset_id=synset_id).values()
        place_id=m.TblAdverbAntoPlace.objects.filter(synset_id=synset_id).values()
        quality_id=m.TblAdverbAntoQuality.objects.filter(synset_id=synset_id).values()
        size_id=m.TblAdverbAntoSize.objects.filter(synset_id=synset_id).values()
        state_id=m.TblAdverbAntoState.objects.filter(synset_id=synset_id).values()
        time_id=m.TblAdverbAntoTime.objects.filter(synset_id=synset_id).values()
    elif(pos == "verb"):
        action_id=m.TblVerbAntoAction.objects.filter(synset_id=synset_id).values()
        amount_id=m.TblVerbAntoAmount.objects.filter(synset_id=synset_id).values()
        colour_id=m.TblVerbAntoColour.objects.filter(synset_id=synset_id).values()
        direction_id=m.TblVerbAntoDirection.objects.filter(synset_id=synset_id).values()
        gender_id=m.TblVerbAntoGender.objects.filter(synset_id=synset_id).values()
        manner_id=m.TblVerbAntoManner.objects.filter(synset_id=synset_id).values()
        personality_id=m.TblVerbAntoPersonality.objects.filter(synset_id=synset_id).values()
        place_id=m.TblVerbAntoPlace.objects.filter(synset_id=synset_id).values()
        quality_id=m.TblVerbAntoQuality.objects.filter(synset_id=synset_id).values()
        size_id=m.TblVerbAntoSize.objects.filter(synset_id=synset_id).values()
        state_id=m.TblVerbAntoState.objects.filter(synset_id=synset_id).values()
        time_id=m.TblVerbAntoTime.objects.filter(synset_id=synset_id).values()
    
    if(len(action_id)>0):
        for i in action_id:
            temp=[]
            temp.append(i['anto_action_id'])
            temp.append('Antonymy - Action')
            antonymy_ids.append(temp)
    
    if(len(amount_id)>0):
        for i in amount_id:
            temp=[]
            temp.append(i['anto_amount_id'])
            temp.append('Antonymy - Amount')
            antonymy_ids.append(temp)
    
    if(len(colour_id)>0):
        for i in colour_id:
            temp=[]
            temp.append(i['anto_colour_id'])
            temp.append('Antonymy - Colour')
            antonymy_ids.append(temp)
    
    if(len(direction_id)>0):
        for i in direction_id:
            temp=[]
            temp.append(i['anto_direction_id'])
            temp.append('Antonymy - Direction')
            antonymy_ids.append(temp)
    
    if(len(gender_id)>0):
        for i in gender_id:
            temp=[]
            temp.append(i['anto_gender_id'])
            temp.append('Antonymy - Gender')
            antonymy_ids.append(temp)
    
    if(len(manner_id)>0):
        for i in manner_id:
            temp=[]
            temp.append(i['anto_manner_id'])
            temp.append('Antonymy - Manner')
            mero_lis.append(temp)

    if(len(personality_id)>0):
        for i in personality_id:
            temp=[]
            temp.append(i['anto_personality_id'])
            temp.append('Antonymy - Personality')
            antonymy_ids.append(temp)
    
    if(len(place_id)>0):
        for i in place_id:
            temp=[]
            temp.append(i['anto_place_id'])
            temp.append('Antonymy - Place')
            antonymy_ids.append(temp)
    
    if(len(quality_id)>0):
        for i in quality_id:
            temp=[]
            temp.append(i['anto_quality_id'])
            temp.append('Antonymy - Quality')
            antonymy_ids.append(temp)
    
    if(len(size_id)>0):
        for i in size_id:
            temp=[]
            temp.append(i['anto_size_id'])
            temp.append('Antonymy - Size')
            antonymy_ids.append(temp)

    if(len(state_id)>0):
        for i in state_id:
            temp=[]
            temp.append(i['anto_state_id'])
            temp.append('Antonymy - State')
            antonymy_ids.append(temp)

    if(len(time_id)>0):
        for i in time_id:
            temp=[]
            temp.append(i['anto_time_id'])
            temp.append('Antonymy - Time')
            antonymy_ids.append(temp)
    
    ## Removing duplicate ids from Antonymy IDs
    temp_id = []
    temp = []
    for k in antonymy_ids:
        if k[0] not in temp_id:
            temp_id.append(k[0])
            temp.append(k)

    antonymy_ids = temp

    data={}
    j=0
    #fetching data
    for k in antonymy_ids:
        l=[]
        synset = searchSynsetDataById(k[0],langno)
        l.append(k[1])
        l.append(synset["synonyms"])
        print(synset["gloss"])
        l.append(synset["gloss"])
        # l.append(synset["gloss"][1])
        l.append(synset["synset_id"])
        l.append(synset["pos"])
        data[j]=l
        j = j+1

    data["length"]=j
    antonymy_data_json = json.dumps(data,ensure_ascii=False)

    return JsonResponse(antonymy_data_json,safe=False)


def recomendation(q,lang):
    wordList = []
    j = 0

    if lang == '1':
        tblName = "EnglishSynsetData"
    else:
        tblName = "TblAll"+langName[int(lang)]+"SynsetData"
        
    try:
        model = apps.get_model(appName,tblName)
    except Exception as e:
        print(e)
    
    data = model.objects.using('region').all()
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





    
   
def feedBack(request):
    return render(request,'index.html#feedBack',context=None)

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)
