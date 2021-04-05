from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
from django.db.models import Q,Count
from django.apps import apps
import indoWordNet.models as m
import base64
import time
import os

# Declaring GLobal Variables
appName = "indoWordNet"
languageName = ["Hindi","English","Assamese","Bengali","Bodo","Gujarati","Kannada","Kashmiri","Konkani","Malayalam","Manipuri","Marathi","Nepali","Sanskrit","Tamil","Telugu","Punjabi","Urdu","Oriya"]
displayLanguages = ["हिन्दी (hindi)","English","অসমীয়া (Assamese)","বাংলা (Bengali)","बोडो (bodo)","ગુજરાતી (Gujarati)"," ಕನ್ನಡ (Kannada) ","کًش (Kashmiri)","कोंकणी (konkani)","മലയാളം (Malayalam)","মনিপুরি (Manipuri)","मराठी (Marathi)"," नेपाली (Nepali)","संस्कृतम् (Sanskrit)"," தமிழ் (Tamil)","తెలుగు} (Telugu)","ਪੰਜਾਬੀ (punjabi)","اردو (urdu)","ଓରିୟା (odiya)"]
meronymyVector = ["component object","feature activity","member collection","phase state","place area","portion mass","position area","resource process","stuff object"]
holonymyVector = ["component object","feature activity","member collection","phase state","place area","portion mass","position area","resource process","stuff object"]
antonymyVector = ["action","amount","colour","direction","gender","manner","personality","place","quality","size","state","time"]
nounRelationsVector = ["ability verb","attributes","capability verb","compound","function verb"]
verbRelationsVector = ["causative","compounding","conjunction","derived from","entailment","troponymy"]
modifiesVector = {"adjective": "modifies noun", "adverb": "modifies verb"}
stat = []
## App Functions

## Index Function - For Home Page
def index(request):
    feedbackSuccess = None
    if('feedbackSuccess' in request.GET):
        feedbackSuccess = request.GET.get('feedbackSuccess',None)
        return render(request,'index.html',{'found':True,'suggFound': False,'feedbackSuccess': feedbackSuccess})
    
    feedbackError = None
    if('feedbackError' in request.GET):
        feedbackError = request.GET.get('feedbackError',None)
        return render(request,'index.html',{'found':True,'suggFound': False,'feedbackError': feedbackError})
    
    return render(request,'index.html',{'found':True,'suggFound': False})



## Wordnet Function  - For Main Page Rendering
## It searches for synset by word, if found: returns list of synsets and redirects to wordnet.html
## If not found: returns list of closes matching words and redirects to index.html
def wordnet(request):
    word = str(request.GET.get("query"))
    langno = str(request.GET.get("langno"))
    length = 0
    wordList = []
    wordList, length = getSynsetByWord(word, langno)

    if length == 0:
        suggWord, l = getCloseMatch(word, langno)
        if l != 0:
            return render(request,"index.html",{"query": word,"found": False,"suggWord": suggWord,"suggFound": True,"langno": langno})
        else:
            return render(request,"index.html",{"query": word,"found": False,"suggWord": suggWord,"suggFound": False,"langno": langno})
    return render(request,"wordnet.html",{"query": word, "langno": langno, "length": length, "wordList": wordList})


## getSynsetByWord : return list of synsets for given word
def getSynsetByWord(word, lang):
    wordList = []
    length = 0

    if lang == "1":
        try:
            data = m.EnglishSynsetData.objects.using("region").all()
        except Exception as e:
            print(e)

        for i in data:
            try:
                synonyms = i.synset_words.split(", ")
            except Exception as e:
                print(e)

            if word in synonyms:
                try:
                    hindiId = m.EnglishHindiIdMapping.objects.using("region").filter(
                        english_id=str(i.synset_id)
                    )
                except Exception as e:
                    print(e)

                for j in hindiId:
                    length = length + 1
                    l = []
                    l.append(str(j.hindi_id))
                    l.append(str(j.hindi_category))
                    l.append(synonyms)

                    try:
                        gloss = i.gloss.split(";")
                        if len(gloss) == 1:
                            gloss.append("Example statement not available")
                            l.append(gloss)
                        else:
                            l.append(gloss)
                    except Exception as e:
                        l.append(str(i.gloss))

                    l.append(str(i.gloss))

                    try:
                        l.append(
                            m.TblAllHindiSynsetData.objects.using("region")
                            .filter(synset_id=str(j.hindi_id))[0]
                            .gloss.decode("UTF-8")
                            .split(":")[0]
                        )
                    except Exception as e:
                        print(e)

                    wordList.append(l)

    else:
        if lang == "0":
            tblName = "TblAllWords"
        else:
            tblName = "TblAll" + languageName[int(lang)] + "SynsetData"

        try:
            model = apps.get_model(appName, tblName)
        except Exception as e:
            print(e)

        try:
            if lang == "0":
                data = model.objects.filter(word=word).order_by("sense_num")
            else:
                data = model.objects.using("region").all()
        except Exception as e:
            print(e)

        for i in data:
            try:
                if lang == "0":
                    i = m.TblAllSynset.objects.get(synset_id=str(i.synset_id))

                if lang == "0":
                    synonyms = []
                    words = m.TblAllWords.objects.filter(synset_id=str(i.synset_id))
                    for j in words:
                        synonyms.append(j.word)

                elif lang == "11":
                    synonyms = i.synset.split(",")
                else:
                    synonyms = i.synset.decode("UTF-8").replace(", ", ",").split(",")
            except Exception as e:
                print(e)

            if word in synonyms:
                length = length + 1
                l = []
                l.append(str(i.synset_id))
                l.append(str(i.category))
                l.append(synonyms)

                ## Appending Gloss is particular language
                try:
                    gloss = i.gloss.decode("UTF-8").replace(":", ";")
                    gloss = gloss.split(";")
                    if len(gloss) == 1:
                        gloss.append("Example statement not available")
                    l.append(gloss)
                except Exception as e:
                    print(e)
                    l.append(i.gloss.decode("UTF-8"))

                ## Appending Gloss in English language
                try:
                    enId = m.EnglishHindiIdMapping.objects.using("region").get(hindi_id=str(i.synset_id))
                    glossEN = m.EnglishSynsetData.objects.using("region").filter(synset_id=str(enId.english_id))
                    l.append(str(glossEN[0].gloss))
                except m.EnglishHindiIdMapping.DoesNotExist:
                    l.append("English Linkage Not Available")

                ## Appending Gloss in Hindi Language
                try:
                    gloss = m.TblAllSynset.objects.filter(synset_id=str(i.synset_id))[0]
                    l.append(gloss.gloss.decode("UTF-8").split(":")[0])
                except Exception as e:
                    print(e)
                wordList.append(l)

    return wordList, length


## getCloseMatch - returns list of closest matching words in case of search word not found failure
def getCloseMatch(word, lang):
    wordList = []

    if lang == "1":
        tblName = "EnglishSynsetData"
        idList = []
    else:
        tblName = "TblAll" + languageName[int(lang)] + "SynsetData"

    try:
        model = apps.get_model(appName, tblName)
    except Exception as e:
        print(e)

    data = model.objects.using("region").all()

    for i in data:
        try:
            if lang == "0":
                words = i.synset.decode("UTF-8").split(",")
            elif lang == "11":
                words = i.synset.split(",")
            elif lang == "1":
                words = i.synset_words.split(", ")
                sID = str(i.synset_id)
            else:
                words = i.synset.decode("UTF-8").split(", ")
        except Exception as e:
            print(e)

        for k in words:
            if word in k:
                wordList.append(k)
                if lang == "1":
                    idList.append(sID)

    if len(wordList) > 10:
        l = 0
        newWordList = []
        length = len(word)
        for (i, w) in enumerate(wordList):
            length1 = len(w)
            ratio = length / length1
            limit = 0
           
            try:
                if ratio > limit:
                    if lang == "1":
                        try:
                            if m.EnglishHindiIdMapping.objects.using("region").filter(english_id=idList[i]):
                                l = l + 1
                                newWordList.append(w)
                                if l == 10:
                                    return newWordList, l

                        except Exception as e:
                            print(e)

                    else:
                        l = l + 1
                        newWordList.append(w)
                        if l == 10:
                            return newWordList, l
            except Exception as e:
                print(e)
        return wordList, l
    else:

        if lang == "1":
            l = 0
            newWordList = []
            for (i, w) in enumerate(wordList):
                try:
                    if m.EnglishHindiIdMapping.objects.using("region").filter(english_id=idList[i]):
                        newWordList.append(w)
                        l = l + 1
                except Exception as e:
                    print(e)
            return newWordList, l
        l = len(wordList)
        return wordList, l


## getSynsetByID : returns a single synset for given synset sID and lang no.
## Used internally by other functions to get data of a particular synset.
def getSynsetByID(sID, lang):
    data = {}
    # data['error'] = ['0','Success']
    data["synset_id"] = str(sID)

    if lang == "1":
        tblName = "EnglishSynsetData"
    else:
        tblName = "TblAll" + languageName[int(lang)] + "SynsetData"

    try:
        model = apps.get_model(appName, tblName)
    except Exception as e:
        print(e)

    try:
        if lang == "0":
            i = m.TblAllSynset.objects.get(synset_id=str(sID))
        elif lang == "1":
            englishId = m.EnglishHindiIdMapping.objects.using("region").get(hindi_id=str(sID))
            i = model.objects.using("region").get(synset_id=str(englishId.english_id))
        else:
            i = model.objects.using("region").get(synset_id=str(sID))
    except Exception as e:
        print(e)
        data["pos"] = ""
        data["synonyms"] = []
        data["gloss"] = ["", ""]
        data["error"] = ["1", "No Data found for given Synset"]
        return data

    data["pos"] = str(i.category)

    try:
        if lang == "0":
            synonyms = []
            words = m.TblAllWords.objects.filter(synset_id=str(i.synset_id))
            for j in words:
                synonyms.append(j.word)
        elif lang == "1":
            synonyms = i.synset_words.split(",")
        elif lang == "11":
            synonyms = i.synset.split(",")
        else:
            synonyms = i.synset.decode("UTF-8").replace(", ", ",").split(",")
    except Exception as e:
        print(e)
        data["synonyms"] = []
        data["gloss"] = ["", ""]
        data["error"] = ["2", "No Synonyms found for given Synset"]
        return data

    data["synonyms"] = synonyms

    try:
        if lang == "1":
            gloss = i.gloss.replace(":", ";")
        else:
            gloss = i.gloss.decode("UTF-8").replace(":", ";")

        data["gloss"] = gloss.split(";")
    except Exception as e:
        print(e)
        gloss = i.gloss.decode("UTF-8")

    gloss = gloss.split(";")

    if len(gloss) == 1:
        gloss.append("Example statement not available")
        data["gloss"] = gloss
    else:
        data["gloss"] = gloss

    return data


## fetchSynset - return synset of given synset ID in target language responding to langno
def fetchSynset(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno")

    data = getSynsetByID(synset_id, langno)
    
    if "error" in data:
        response = JsonResponse({"error": ["1","No Data Found For Given Synset In " + displayLanguages[int(langno)]], "cause": data["error"][1]})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    synset_data_json = json.dumps(data, ensure_ascii=False)
    return JsonResponse(synset_data_json, safe=False)




def fetchHypernymy(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno")
    pos = request.GET.get("pos", None)
   
    if pos != "noun" and pos != "verb":
        response = JsonResponse({"error": ["1", "No Hypernymy Data Found."],"cause": "Invalid Part Of Speech: " + pos })
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    tbl_name = "Tbl" + pos.title().replace(" ", "") + "Hypernymy"
    try:
        m = apps.get_model(appName, tbl_name)
    except Exception as e:
        print(e)
        response = JsonResponse({"error": ["1", "No Hypernymy Data Found."],"cause": "Internal Server Error"})
        response.status_code = 500  # To announce that the user isn't allowed to publish
        return response

    i = m.objects.filter(synset_id=synset_id).values()
    if len(i) == 0:
        response = JsonResponse({"error": ["1", "No Hypernymy Data Found"], "cause": "No Data available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
    hyper_ids = []  # stores hypernymy id's

    # fetching hypernym id's
    while len(i) != 0:
        hyper_ids.append(i[0]["hypernymy_id"])
        i = m.objects.filter(synset_id=i[0]["hypernymy_id"]).values()
       
    errorStatus = ["0", "Found In Current Language"]
    data = {}
    j = 0
    # fetching data
    for k in hyper_ids:
        l = []
        synset = getSynsetByID(k, langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["pos"])
        data[j] = l
        j = j + 1

    hyper_data_json = json.dumps(data, ensure_ascii=False)

    return JsonResponse(hyper_data_json, safe=False)

   

def fetchHyponymy(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno")
    pos = request.GET.get("pos", None)
   
    if pos != "noun":
        response = JsonResponse({"error": ["1", "No Hyponymy Data Found."],"cause": "Invalid Part Of Speech: " + pos})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    tbl_name = "Tbl" + pos.title().replace(" ", "") + "Hyponymy"
    try:
        m = apps.get_model(appName, tbl_name)
    except Exception as e:
        print(e)
        response = JsonResponse({    "error": ["1", "No Hyponymy Data Found."],
                "cause": "Internal Server Error",
            }
        )
        response.status_code = 500  # To announce that the user isn't allowed to publish
        return response

    i = m.objects.filter(synset_id=synset_id).values()
    if len(i) == 0:
        response = JsonResponse({"error": ["1", "No Hyponymy Data Found"], "cause": "No Data available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    hy_id = []  # stores hyponymy id's

    for value in i:
        hy_id.append(value["hyponymy_id"])

    # fetching data
    data = {}
    j = 0
    for k in hy_id:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k, langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["pos"])
        data[j] = l
        j = j + 1

    hypo_data_json = json.dumps(data, ensure_ascii=False)

    return JsonResponse(hypo_data_json, safe=False)
   
    return JsonResponse(hypo_data_json, safe=False)


def fetchOntonymy(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    
    # Fetching node id
    i = m.TblOntoNodes.objects.filter(synset_id=synset_id)[0].onto_nodes_id
    data = getOntoAllAncestors(synset_id, langno)
    onto_data_json = json.dumps(data, ensure_ascii=False)

    return JsonResponse(onto_data_json, safe=False)


def showOnto(request):
    synset_id = request.GET.get("synset_id", None)
    oid = request.GET.get("oid", None)
    langno = request.GET.get("langno", None)
    wordList = getOntoAllAncestors(synset_id, langno)

    keys = list(wordList.keys())
    for k in keys:
        if wordList[k][0] > int(oid):
            wordList.pop(k)

    ini_list = list(range(0, len(wordList)))
    wordList = dict(zip(ini_list, list(wordList.values())))

    return render(request, "ontotree.html", {"oid": oid, "langno": langno, "wordList": wordList})


def getOntoAllAncestors(synset_id, langno):

    try:
        # Fetching node id
        m = apps.get_model(appName, "TblOntoNodes")
    except Exception as e:
        print(e)
        response = JsonResponse({"error": ["1", "No Ontonymy Data Found."],"cause": "Internal Server Error"})
        response.status_code = 500  # To announce that the user isn't allowed to publish
        return response

    i = m.objects.filter(synset_id=synset_id)[0].onto_nodes_id
    
    onto_ids = []
    try:
        # Fetching Parent Ids
        m = apps.get_model(appName, "TblOntoMap")
    except Exception as e:
        print(e)
        response = JsonResponse({"error": ["1", "No Ontonymy Data Found."],"cause": "Internal Server Error"})
        response.status_code = 500  # To announce that the user isn't allowed to publish
        return response

    while i != 1:
        onto_ids.append(i)
        i = m.objects.filter(child_id=str(i))[0].parent_id
    
    if len(onto_ids) == 0:
        response = JsonResponse({"error": ["1", "No Ontonymy Data Found."], "cause": "No Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
    try:
        m = apps.get_model(appName, "TblOntoData")
    except Exception as e:
        print(e)
        response = JsonResponse({"error": ["1", "No Ontonymy Data Found."],"cause": "Internal Server Error"})
        response.status_code = 500  # To announce that the user isn't allowed to publish
        return response

    data = {}
    parent_id = synset_id
    j = 0
    for i in onto_ids:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        onto_data = m.objects.filter(onto_id=str(i))[0]
        if onto_data != []:
            l.append(onto_data.onto_id)
            l.append(onto_data.onto_data)
            l.append(onto_data.onto_desc)
            l.append(errorStatus)
            l.append(parent_id)
            parent_id = onto_data.onto_id
        else:
            l.append("")
            l.append("")
            l.append("")
            l.append(errorStatus)
            l.append(parent_id)
            parent_id = str(i)
        data[j] = l
        j = j + 1
    return data


def fetchReverseOntonymy(request):
    oid = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    pos = request.GET.get("pos", None)  ##pos is not needed for this function. Still saved it for future purpose
    start = int(request.GET.get("start", None))
    tbl_name = "TblOntoNodes"
    if start < 0:
        start = 0
    try:
        m = apps.get_model(appName, tbl_name)
    except Exception as e:
        print(e)
        response = JsonResponse({"error": ["1", "No Synset Data Found."], "cause": "Internal Server Error"})
        response.status_code = 500  # To announce that the user isn't allowed to publish
        return response

    synset_ids = m.objects.filter(onto_nodes_id=oid).order_by("synset_id").values()
    
    if len(synset_ids) == 0:
        response = JsonResponse({"error": ["1", "No Synset Data Found."], "cause": "Data Not Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
    

    end = len(synset_ids)

    if start >= end:
        response = JsonResponse({"error": ["2", "No More Synset Data Found."],"cause": "No More Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    if start + 25 < len(synset_ids):
        end = start + 25
    ## try in slicing
    synset_ids = synset_ids[start:end]
    currentLength = len(synset_ids)

    
    data = {}
    j = 0
    # fetching data
    for k in synset_ids:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k["synset_id"], langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["pos"])
        data[j] = l
        j = j + 1
    reverseOnto_data_json = json.dumps(data, ensure_ascii=False)
    return JsonResponse(reverseOnto_data_json, safe=False)


def fetchNounRelations(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    pos = request.GET.get("pos", None)
    nounRelationsList = []
    print(synset_id)
    if pos != "noun":
        response = JsonResponse({"error": ["1", "No Noun Relations Data Found."],"cause": "Invalid Part Of Speech: " + pos})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
    
    for suffix in nounRelationsVector:
        tbl_name = ("Tbl" + pos.title().replace(" ", "") + suffix.title().replace(" ", ""))
       
        ans1 = 0
        ans2 = None
        col_name = suffix.replace(" ", "_") + "_id"

        IDs = None
        try:
            m = apps.get_model(appName, tbl_name)
        except Exception as e:
            print(e)
            response = JsonResponse({"error": ["1", "No Noun Relations Data Found."],"cause": "Internal Server Error"})
            response.status_code = 500  # To announce that the user isn't allowed to publish
            return response

        IDs = m.objects.filter(synset_id=synset_id).values()

        if len(IDs) > 0:
            for i in IDs:
                temp = []
                temp.append(i[col_name])
                temp.append("Relation " + suffix.title())
                nounRelationsList.append(temp)

    if len(nounRelationsList) == 0:
        response = JsonResponse({"error": ["1", "No Noun Relations Data Found."],"cause": "No Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish        
        return response
    ## Removing duplicate ids from Antonymy IDs
    temp_id = []
    temp = []
    for k in nounRelationsList:
        if k[0] not in temp_id:
            temp_id.append(k[0])
            temp.append(k)
    nounRelationsList = temp

    data = {}
    j = 0
    # fetching data
    for k in nounRelationsList:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k[0], langno)
        l.append(k[1])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["synset_id"])
        l.append(synset["pos"])
        data[j] = l
        j = j + 1

    nounRelations_data_json = json.dumps(data, ensure_ascii=False)

    return JsonResponse(nounRelations_data_json, safe=False)


def fetchVerbRelations(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    pos = request.GET.get("pos", None)
    verbRelationsList = []
 
    if pos != "verb":
        response = JsonResponse({"error": ["1", "No Verb Relations Data Found."],"cause": "Invalid Part Of Speech: " + pos})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    for suffix in verbRelationsVector:
        tbl_name = ("Tbl" + pos.title().replace(" ", "") + suffix.title().replace(" ", ""))
      

        ans1 = 0
        ans2 = None
        col_name = suffix.replace(" ", "_") + "_id"

        IDs = None
        try:
            m = apps.get_model(appName, tbl_name)
        except Exception as e:
            print(e)
            response = JsonResponse({"error": ["1", "No Verb Relations Data Found."], "cause": "Internal Server Error"})
            response.status_code = (500)  # To announce that the user isn't allowed to publish
            
            return response
        IDs = m.objects.filter(synset_id=synset_id).values()

        if len(IDs) > 0:
            for i in IDs:
                temp = []
                temp.append(i[col_name])
                temp.append("Relation " + suffix.title())
                verbRelationsList.append(temp)

    if len(verbRelationsList) == 0:
        response = JsonResponse({"error": ["1", "No Verb Relations Data Found."],"cause": "No Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    ## Removing duplicate ids from Antonymy IDs
    temp_id = []
    temp = []
    for k in verbRelationsList:
        if k[0] not in temp_id:
            temp_id.append(k[0])
            temp.append(k)
    verbRelationsList = temp

    data = {}
    j = 0
    # fetching data
    for k in verbRelationsList:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k[0], langno)
        l.append(k[1])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["synset_id"])
        l.append(synset["pos"])
        data[j] = l
        j = j + 1

    verbRelations_data_json = json.dumps(data, ensure_ascii=False)

    return JsonResponse(verbRelations_data_json, safe=False)


def fetchDerivedFrom(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    pos = request.GET.get("pos", None)
    der_id = []

    if pos != "noun" and pos != "adjective" and pos != "verb" and pos != "adverb":
        response = JsonResponse({ "error": ["1", "No Derived From Data Found."],"cause": "Invalid Part Of Speech: " + pos})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    tbl_name = "Tbl" + pos.title().replace(" ", "") + "DerivedFrom"
   

    try:
        m = apps.get_model(appName, tbl_name)
    except Exception as e:
        print(e)
        response = JsonResponse({"error": ["1", "No Derived From Data Found."],"cause": "Internal Server Error"})
        response.status_code = 500  # To announce that the user isn't allowed to publish
        return response

    der_id = m.objects.filter(synset_id=synset_id).values("derived_from_id")
    
    if len(der_id) == 0:
        response = JsonResponse({"error": ["1", "No Derived From Data Found."],"cause": "No Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
   
    data = {}
    j = 0
    # fetching data
    for k in der_id:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k["derived_from_id"], langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["pos"])
        data[j] = l
        j = j + 1

    derived_data_json = json.dumps(data, ensure_ascii=False)

    
    return JsonResponse(derived_data_json, safe=False)


def fetchModifies(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    pos = request.GET.get("pos", None)
    mod_id = []

    if pos != "adjective" and pos != "adverb":
        response = JsonResponse({"error": ["1", "No Modifies Data Found."],"cause": "Invalid Part Of Speech: " + pos})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
    tbl_name = ("Tbl" + pos.title().replace(" ", "")+ modifiesVector[pos].title().replace(" ", ""))
   

    try:
        m = apps.get_model(appName, tbl_name)
    except Exception as e:
        print(e)
        response = JsonResponse({"error": ["1", "No Modifies Data Found."],"cause": "Internal Server Error"})
        response.status_code = 500  # To announce that the user isn't allowed to publish
        return response

    id_i = m.objects.filter(synset_id=synset_id).values()
    col_name = modifiesVector[pos].replace(" ", "_") + "_id"
    if len(id_i) > 0:
        for i in id_i:
            mod_id.append(i[col_name])

    if len(mod_id) == 0:
        response = JsonResponse({"error": ["1", "No Modifies Data Found."], "cause": "No Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
   
    data = {}
    j = 0
    # fetching data
    for k in mod_id:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k, langno)
        l.append(synset["synset_id"])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["pos"])
        l.append(modifiesVector[pos])
        data[j] = l
        j = j + 1

  
    modifies_data_json = json.dumps(data, ensure_ascii=False)
    
    return JsonResponse(modifies_data_json, safe=False)


def fetchHolonymy(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    pos = request.GET.get("pos", None)
    holo_lis = []

    if pos != "noun":
        response = JsonResponse({"error": ["1", "No Holonymy Data Found."],"cause": "Invalid Part Of Speech: " + pos})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    for suffix in holonymyVector:
        tbl_name = ("Tbl"+ pos.title().replace(" ", "") + "Holo" + suffix.title().replace(" ", ""))
       
        ans1 = 0
        ans2 = None
        col_name = "holo_" + suffix.replace(" ", "_") + "_id"

        IDs = None

        try:
            m = apps.get_model(appName, tbl_name)
        except Exception as e:
            print(e)
            response = JsonResponse({"error": ["1", "No Holonymy Data Found."],"cause": "Internal Server Error"})
            response.status_code = 500 # To announce that the user isn't allowed to publish
            return response

        IDs = m.objects.filter(synset_id=synset_id).values()
        if len(IDs) > 0:
            for i in IDs:
                temp = []
                temp.append(i[col_name])
                temp.append("Holonymy " + suffix.title())
                holo_lis.append(temp)

    if len(holo_lis) == 0:
        response = JsonResponse({"error": ["1", "No Holonymy Data Found."], "cause": "No Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
    
    ## Removing duplicate ids from Antonymy IDs
    temp_id = []
    temp = []
    for k in holo_lis:
        if k[0] not in temp_id:
            temp_id.append(k[0])
            temp.append(k)

    holo_lis = temp

    data = {}

    j = 0
    # fetching data
    for k in holo_lis:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k[0], langno)
        l.append(k[1])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["synset_id"])
        l.append(synset["pos"])
        data[j] = l
        j = j + 1

    holonymy_data_json = json.dumps(data, ensure_ascii=False)
    
    return JsonResponse(holonymy_data_json, safe=False)


def fetchMeronymy(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    pos = request.GET.get("pos", None)
    mero_lis = []

    if pos != "noun":
        response = JsonResponse({"error": ["1", "No Meronymy Data Found."],"cause": "Invalid Part Of Speech: " + pos})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    for suffix in holonymyVector:
        tbl_name = ("Tbl" + pos.title().replace(" ", "") + "Mero" + suffix.title().replace(" ", ""))
       

        ans1 = 0
        ans2 = None
        col_name = "mero_" + suffix.replace(" ", "_") + "_id"

        IDs = None

        try:
            m = apps.get_model(appName, tbl_name)
        except Exception as e:
            print(e)
            response = JsonResponse({"error": ["1", "No Meronymy Data Found."],"cause": "Internal Server Error"})
            response.status_code = 500 # To announce that the user isn't allowed to publish
            return response

        IDs = m.objects.filter(synset_id=synset_id).values()
        if len(IDs) > 0:
            for i in IDs:
                temp = []
                temp.append(i[col_name])
                temp.append("Meronymy " + suffix.title())
                mero_lis.append(temp)

    if len(mero_lis) == 0:
        response = JsonResponse({"error": ["1", "No Meronymy Data Found."], "cause": "No Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    ## Removing duplicate ids from Antonymy IDs
    temp_id = []
    temp = []
    for k in mero_lis:
        if k[0] not in temp_id:
            temp_id.append(k[0])
            temp.append(k)

    mero_lis = temp

    data = {}

    j = 0
    # fetching data
    for k in mero_lis:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k[0], langno)
        l.append(k[1])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["synset_id"])
        l.append(synset["pos"])
        data[j] = l
        j = j + 1

    holonymy_data_json = json.dumps(data, ensure_ascii=False)

    return JsonResponse(holonymy_data_json, safe=False)
    

def fetchAntonymy(request):
    synset_id = request.GET.get("synset_id", None)
    langno = request.GET.get("langno", None)
    pos = request.GET.get("pos", None)
    antonymy_ids = []

    if pos != "noun" and pos != "adjective" and pos != "verb" and pos != "adverb":
        response = JsonResponse({"error": ["1", "No Antonymy Data Found."],"cause": "Invalid Part Of Speech: " + pos})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response

    for suffix in antonymyVector:
        tbl_name = ("Tbl"+ pos.title().replace(" ", "")+ "Anto"+ suffix.title().replace(" ", ""))
     
        ans1 = 0
        ans2 = None
        col_name = "anto_" + suffix.replace(" ", "_") + "_id"

        IDs = None

        try:
            m = apps.get_model(appName, tbl_name)
        except Exception as e:
            print(e)
            response = JsonResponse({"error": ["1", "No Antonymy Data Found."],"cause": "Internal Server Error"})
            response.status_code = 500  # To announce that the user isn't allowed to publish
            return response

        IDs = m.objects.filter(synset_id=synset_id).values()
        if len(IDs) > 0:
            for i in IDs:
                temp = []
                temp.append(i[col_name])
                temp.append("Antonymy " + suffix.title())
                antonymy_ids.append(temp)

    if len(antonymy_ids) == 0:
        response = JsonResponse({"error": ["1", "No Antonymy Data Found."], "cause": "No Data Available"})
        response.status_code = 202  # To announce that the user isn't allowed to publish
        return response
    temp_id = []
    temp = []
    for k in antonymy_ids:
        if k[0] not in temp_id:
            temp_id.append(k[0])
            temp.append(k)

    antonymy_ids = temp

    data = {}
    j = 0
    # fetching data
    for k in antonymy_ids:
        l = []
        errorStatus = ["0", "Found In Current Language"]
        synset = getSynsetByID(k[0], langno)
        l.append(k[1])
        l.append(synset["synonyms"])
        l.append(synset["gloss"])
        if "error" in synset:
            errorStatus[0] = "1"
            errorStatus[1] = "Not Found In Current Language"
        l.append(errorStatus)
        l.append(synset["synset_id"])
        l.append(synset["pos"])
        data[j] = l
        j = j + 1

    antonymy_data_json = json.dumps(data, ensure_ascii=False)

    return JsonResponse(antonymy_data_json, safe=False)


def recomendation(q, lang):
    wordList = []
    j = 0

    if lang == "1":
        tblName = "EnglishSynsetData"
    else:
        tblName = "TblAll" + languageName[int(lang)] + "SynsetData"

    try:
        model = apps.get_model(appName, tblName)
    except Exception as e:
        print(e)

    data = model.objects.using("region").all()
    for i in data:
        if lang == "0":
            words = i.synset.decode("UTF-8").split(",")
        elif lang == "11":
            words = i.synset.split(",")
        elif lang == "1":
            words = i.synset_words.split(", ")
        else:
            words = i.synset.decode("UTF-8").split(", ")
        for k in words:
            if k.startswith(q):
                wordList.append(k)
                j = j + 1
                if j == 10:
                    break
        if j == 10:
            break
    return wordList


def word(request):
    q = str(request.GET.get("q", None))
    lang = str(request.GET.get("langno", None))

    wordList = recomendation(q, lang)
    wordList = json.dumps(wordList, ensure_ascii=False)
    return JsonResponse(wordList, safe=False)



def getStatestics(request):
    
    langno = int(request.GET.get("langno",None))
    l = [ "","" ,"" ,"" ,"" ,""]
    l[0] = displayLanguages[langno]
    if languageName[langno] == "English":
        tblName = "EnglishSynsetData"
    else:
        tblName = "TblAll" + languageName[langno] + "SynsetData"
    
    try:
        model = apps.get_model(appName, tblName)
    except Exception as e:
        print(e)

     
    data = model.objects.using("region").values('category').order_by('category').annotate(count = Count('category'))
    totel = 0
    for c in data:
        totel = totel + c["count"]
        if str(c["category"]).lower() == "noun":
            l[1] = c["count"]
        elif str(c["category"]).lower() == "verb":
            l[2] = c["count"]
        elif str(c["category"]).lower() == "adjective":
            l[3] = c["count"]
        elif str(c["category"]).lower() == "adverb":
            l[4] = c["count"]
              
    l[5] = totel
    
    statistics = json.dumps(l, ensure_ascii=False)
    return JsonResponse(statistics, safe=False)

def feedback(request):
    if(request.method == "GET"):
        return render(request,'index.html#feedBack',context=None)
    elif(request.is_ajax and request.method == "POST"):
        name = request.POST.get('name',None)
        emailId = request.POST.get('email',None)
        comments = request.POST.get('comments',None)

        try:
            record = m.UserFeedback(name=name,emailid=emailId,comments=comments)
            record.save(using='iwn_utilities')
            if(record.pk):
                return redirect('/?feedbackSuccess=True')
            else:
                return redirect('/?feedbackError=True')
        except Exception as e:
            print(e)
            return redirect('/?feedbackError=True')

def contactUs(request):
    return render(request,'index.html#contactUs',context=None)
