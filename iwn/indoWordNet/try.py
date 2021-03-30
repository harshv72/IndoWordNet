s = "ability verb"
pos = "noun"
tbl_name = "Tbl" + pos.title().replace(" ","") + s.title().replace(" ","")
print(tbl_name)

d = {
  "0": [
    101,
    "गुणसूचक (Qualitative)",
    "QUAL   उदाहरण :- बुद्धिमान, अच्छा, मूर्ख इत्यादि",
    "1"
  ],
  "1": [
    96,
    "विवरणात्मक (Descriptive)",
    "DES  उदाहरण :- लाल, पाँच, सुंदर इत्यादि",
    101
  ],
  "2": [
    91,
    "विशेषण (Adjective)",
    "ADJ  उदाहरण:- सुंदर,लिखित,अमर इत्यादि",
    96
  ]
}

keys = list(d.keys())
for k in keys:
    if d[k][0] > 96:
        d.pop(k)

ini_list = list(range(0,len(d)))
d = dict(zip(ini_list, list(d.values())))

print(d)

if(data["error"][0] != '0')
        response = JsonResponse({"error": "No Data Found For Given Synset In " + displayLanguages[int(langno)]})
        response.status_code = 202 # To announce that the user isn't allowed to publish
        return response

response = JsonResponse({"error": "there was an error because of category"})
response.status_code = 202 # To announce that the user isn't allowed to publish
return response

def fetchVerbRelations(request):
    synset_id=request.GET.get('synset_id',None)
    langno = request.GET.get('langno',None)
    
    
    verbRelationsList = []
    print(synset_id)
    if pos != "verb":
        print("Not verb")
        return None
        ## return failure
    
    for suffix in verbRelationsVector:
        tbl_name = "Tbl" + pos.title().replace(" ","") + suffix.title().replace(" ","")
        print("Looking in:", tbl_name)

        ans1 = 0
        ans2 = None
        col_name = suffix.replace(" ","_") + "_id"

        IDs = None
        m = apps.get_model(appName, tbl_name)
        IDs = m.objects.filter(synset_id=synset_id).values()

        if(len(IDs)>0):
            for i in IDs:
                temp=[]
                temp.append(i[col_name])
                temp.append('Relation '+ suffix.title())
                verbRelationsList.append(temp)
    
    ## Removing duplicate ids from Antonymy IDs
    temp_id = []
    temp = []
    for k in verbRelationsList:
        if k[0] not in temp_id:
            temp_id.append(k[0])
            temp.append(k)
    verbRelationsList = temp

    data={}
    j=0
    #fetching data
    for k in verbRelationsList:
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

    # data["length"]=j
    verbRelations_data_json = json.dumps(data,ensure_ascii=False)
            
    return JsonResponse(verbRelations_data_json,safe=False) 
