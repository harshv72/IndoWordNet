function expand(thistag){
    //alert();
    var s = document.getElementById("lang");
       try{
           for(i=0;i<=s.length;i++){
               //alert(i);
               m = document.getElementById("map"+i).style;
               m.display = 'none';
           }
       }catch(er){}
    //alert(s.value);
    m = document.getElementById("map"+s.value).style;
    m.display = 'block';

   styleObj=document.getElementById(thistag).style;
   styleObj.display='';
   
}

function close1(thistag){
   styleObj=document.getElementById(thistag).style;
   styleObj.display='none';

}

function toggle(thistag){
   styleObj=document.getElementById(thistag).style;
   if (styleObj.display=='none')
        {expand(thistag);}
   else
       {close1(thistag);}

    $(document).on("keypress", '#Search_Form', function (e) {  // Disabling the enter keypress submission, required for the 
        var code = e.keyCode || e.which;					   // function to check word if its empty, the function is 
        console.log(code);									   // called on 'click', hence disabling enter submission is necessary. - Diptesh 20/08/2014
        if (code == 13) {
            console.log('Inside');
            e.preventDefault();
            return false;
        }
    });
}

// function autocomplete(inp, arr) {
//     var currentFocus;
//     inp.addEventListener("input", function(e) {
//         var a, b, i, val = this.value;
//         closeAllLists();
//         if (!val) { return false;}
//         currentFocus = -1;
//         a = document.createElement("DIV");
//         a.setAttribute("id", this.id + "autocomplete-list");
//         a.setAttribute("class", "autocomplete-items");
//         this.parentNode.appendChild(a);
//         k = 0;
//         for (i = 0; ; i++) {
//             if (arr[i].substr(0, val.length)== val) {
//                 k = k+1;
//                 b = document.createElement("DIV");
//                 b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
//                 b.innerHTML += arr[i].substr(val.length);
//                 b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
//                 b.addEventListener("click", function(e) {
//                     inp.value = this.getElementsByTagName("input")[0].value;
//                     closeAllLists();
//                 });
//                 a.appendChild(b);
//                 if(k==10){
//                     break;
//                 }
//             }
//         }
//         if (k == 0){
//             b = document.createElement("DIV");
//                 b.innerHTML = "<strong> Not Found </strong>";
//                 b.addEventListener("click", function(e) {
//                     inp.value = this.getElementsByTagName("input")[0].value;
//                     closeAllLists();
//                 });
//                 a.appendChild(b);
                
//         }
//     });
//     inp.addEventListener("keydown", function(e) {
//         var x = document.getElementById(this.id + "autocomplete-list");
//         if (x) x = x.getElementsByTagName("div");
//         if (e.keyCode == 40) {
//             currentFocus++;
//             addActive(x);
//         } 
//         else if (e.keyCode == 38) { //up
//             currentFocus--;
//             addActive(x);
//         }
//         else if (e.keyCode == 13) {
//             e.preventDefault();
//             if (currentFocus > -1) {
//                 if (x) x[currentFocus].click();
//             }
//         }
//     });
//     function addActive(x) {
//         if (!x) return false;
//         removeActive(x);
//         if (currentFocus >= x.length) currentFocus = 0;
//         if (currentFocus < 0) currentFocus = (x.length - 1);
//         x[currentFocus].classList.add("autocomplete-active");
//     }
//     function removeActive(x) {
//         for (var i = 0; i < x.length; i++) {
//             x[i].classList.remove("autocomplete-active");
//         }
//     }
//     function closeAllLists(elmnt) {
//         var x = document.getElementsByClassName("autocomplete-items");
//         for (var i = 0; i < x.length; i++) {
//             if (elmnt != x[i] && elmnt != inp) {
//             x[i].parentNode.removeChild(x[i]);
//             }
//         }
//     }
//     document.addEventListener("click", function (e) {
//         closeAllLists(e.target);
//     });
//   }
  
  
function autocomplete(inp, arr) {
    var currentFocus;
    // console.log("1")
    // inp.addEventListener("input", function(e) {
        var a, b, i, val = inp.value;
        currentFocus = -1;
        a = document.createElement("DIV");
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            x[i].parentNode.removeChild(x[i]);
        }
        a.setAttribute("id", "autocomplete-list");
        a.setAttribute("class", "autocomplete-items ");
        inp.parentNode.appendChild(a);
        if(arr.length == 0){
            b = document.createElement("DIV");
            b.innerHTML = "<strong> Not Found </strong>";
            b.addEventListener("click", function(e) {
                inp.value = this.getElementsByTagName("input")[0].value;
                closeAllLists();
            });
            a.appendChild(b);
        }
        else{
            for (i = 0; i < arr.length; i++) {
                b = document.createElement("DIV");
                b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
                b.innerHTML += arr[i].substr(val.length);
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                b.addEventListener("click", function(e) {
                    inp.value = this.getElementsByTagName("input")[0].value;
                    closeAllLists();
                });
                a.appendChild(b);
            }
            
        }
        inp.focus()
    // });

  

}
    


function closeAllLists(elmnt) {
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i]) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
}
    
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});




function funct(w){
    //alert(w);
    queryword = document.getElementById("queryword");
    search_button = document.getElementById("search_button");

    queryword.value = queryword.value + w;
    // search()
    // var word = $("#queryword").val();
    // var lang = $("#lang").val();
    // alert('value changed');
    fetchRecomendationData();
    search_button.focus();
}

synset = 1
function next(l,wl,ln)
{
    document.getElementById('prev').style.display = null;
    if(l==(synset+1)){
        document.getElementById('next').style.display = "none"; 
    }
    num = document.getElementById('num').innerHTML = synset+1;
    synset_id = document.getElementById('s_id').innerHTML = wl[synset][0];

    pos = document.getElementById('pos').innerHTML = wl[synset][1];
    synonyms = document.getElementById('synonyms');
    synonyms.innerHTML = "";
    var i;
    for (i=0; i <wl[synset][2].length;i++){   
        var tag = document.createElement('a')
        text = "wordnet?langno="+ ln +"&query="+wl[synset][2][i];
        tag.setAttribute("href",text)
        var textnode = document.createTextNode(wl[synset][2][i]+", ")
        tag.appendChild(textnode);
        synonyms.appendChild(tag);
    }
   
    
    gloss = document.getElementById('gloss').innerHTML = wl[synset][3][0];
    ex = document.getElementById('ex').innerHTML = wl[synset][3][1];
    enGloss = document.getElementById('enGloss').innerHTML = wl[synset][4];
    
    if(ln != '0'){
        hindiGloss = document.getElementById('hindiGloss').innerHTML = wl[synset][5];
    
    }
    
    var tlangno = document.getElementById("tlang").value;
    //var ele = document.getElementsByName('button');
    var ele = document.getElementById("aBtnGroup").children;
    pos = document.getElementById("pos").innerHTML.toLowerCase();
    //console.log(ele);
    for(i = 0; i < ele.length; i++) { 
        //console.log(ele[i].className)
        if(ele[i].className.includes("btn-info")){
            //console.log(ele[i].value)
            fetchTblData(synset_id,tlangno,pos,ele[i].value);
            
            break; 
        }
    } 
    //createOntoTbl(wl[synset][0],0);

    synset = synset+1;
}


function prev(l,wl,ln){
    
    document.getElementById('next').style.display = null;
    if((synset-2)==0){
        document.getElementById('prev').style.display = "none"; 
    }
    synset = synset-1;
    num = document.getElementById('num').innerHTML = synset;
    synset_id = document.getElementById('s_id').innerHTML = wl[synset-1][0];
    pos = document.getElementById('pos').innerHTML = wl[synset-1][1];
   
    synonyms = document.getElementById('synonyms');
    synonyms.innerHTML = "";
    var i;
    for (i=0; i <wl[synset-1][2].length;i++){   
        var tag = document.createElement('a')
        text = "wordnet?langno="+ ln +"&query="+wl[synset-1][2][i];
        tag.setAttribute("href",text)
        var textnode = document.createTextNode(wl[synset-1][2][i]+", ")
        tag.appendChild(textnode);
        synonyms.appendChild(tag);
    }
   
    gloss = document.getElementById('gloss').innerHTML = wl[synset-1][3][0];
    ex = document.getElementById('ex').innerHTML = wl[synset-1][3][1];
    enGloss = document.getElementById('enGloss').innerHTML = wl[synset-1][4];
    if(ln != '0'){
        hindiGloss = document.getElementById('hindiGloss').innerHTML = wl[synset-1][5];
    
    }
    
    var tlangno = document.getElementById("tlang").value;
    //var ele = document.getElementsByName('button');
    var ele = document.getElementById("aBtnGroup").children;
    var pos = document.getElementById("pos").innerHTML.toLowerCase();
    //console.log(ele);
    for(i = 0; i < ele.length; i++) { 
        //console.log(ele[i].className)
        if(ele[i].className.includes("btn-info")){
            //console.log(ele[i].value)
            fetchTblData(synset_id,tlangno,pos,ele[i].value);
            
            break; 
        }
    }
    
}

function fetchTblData(synset_id,langno,pos,btnValue){
    console.log("Synset ID:" + synset_id);
    console.log("Target langNo:" + langno);
    console.log("POS:"+ pos);
    console.log("Button Value:" + btnValue);

    var tblParams = {
        headerList: ["Id","Synonyms","Gloss","Example"],
        colCount: 4
    };
    switch(btnValue){
        case "0":
            getSynsetData(synset_id,langno,pos); 
            break;
            // tblParams.headerList[0] = "Synset ID";
            // urlLink = "fetch_synset";
            // tblTitle = fetchTableSynsetTitle(langno);
            // createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams);
            // console.log("Synset Table Created Successfully");
            // break;
        case "1":
            tblParams.headerList[0] = "Hypernymy ID";
            urlLink = "fetch_hypernymy";
            tblTitle = "Showing Hypernymy";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25); // last parameter doesnt matter unless btnValue=11
            console.log("Hypernymy Table Created Successfully");
            break;
        case "2":
            tblParams.headerList[0] = "Hyponymy ID";
            urlLink = "fetch_hyponymy";
            tblTitle = "Showing Hyponymy";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Hyponymy Table Created Successfully");
            break;
        case "3":
            tblParams.headerList[0] = "Holonymy Type";
            urlLink = "fetch_holonymy";
            tblTitle = "Showing Holonymy";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Holonymy Table Created Successfully");
            break;
        case "4":
            tblParams.headerList[0] = "Meronymy Type";
            urlLink = "fetch_meronymy";
            tblTitle = "Showing Meronymy";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Meronymy Table Created Successfully");
            break;
        case "5":
            tblParams.headerList[0] = "Antonymy ID";
            urlLink = "fetch_antonymy";
            tblTitle = "Showing Antonymy";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Antonymy Table Created Successfully");
            break;
        case "6":
            tblParams.headerList = ["Ontology ID","Ontology Label","Ontology Description"];
            tblParams.colCount = 3;
            urlLink = "fetch_ontology";
            tblTitle = "Showing Ontology";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Ontology Table Created Successfully");
            break;
        case "7":
            tblParams.headerList[0] = "Noun Relation Type";
            urlLink = "fetch_nounRelations";
            tblTitle = "Showing Noun Relations";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Noun Relation Table Created Successfully");
            break;
        case "8":
            tblParams.headerList[0] = "Verb Relation Type";
            urlLink = "fetch_verbRelations";
            tblTitle = "Showing Verb Relations";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Verb Relation Table Created Successfully");
            break;
        case "9":
            tblParams.headerList[0] = "Derived From ID";
            urlLink = "fetch_derivedFrom";
            tblTitle = "Showing Derived From";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Derived From Table Created Successfully");
            break;
        case "10":
            var modifiesVector = {adjective: "Noun", adverb: "Verb"}
            tblParams.headerList[0] = "Modifies " + modifiesVector[pos] +" ID";
            urlLink = "fetch_modifies";
            tblTitle = "Showing Modifies";
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,-25);
            console.log("Modifies Table Created Successfully");
            break;
        case "11":
            tblParams.headerList[0] = "Synset ID";
            urlLink = "fetch_revOnto";
            tblTitle = "Showing Synset List"; // proper title needed for table

            var start = parseInt(document.getElementById("start").value)
            createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,start);
            console.log("Reverse Ontology Table Created Successfully");
            break;
        default:
            console.log("default case in fetch_tbl_data");
            break;
    }
}

function getSynsetData(synset_id,tlangno,pos){

    var langText = fetchTableSynsetTitle(tlangno);
    document.getElementById("tblTitle").innerHTML = langText;
    //var synset_id = document.getElementById("s_id").innerHTML;
    $.ajax({
        url: 'fetch_synset',
        data: {
          'synset_id': synset_id,
          'langno': tlangno,
          'pos': pos
        },
        dataType: 'json',
        success: function (data) {
            if(data.hasOwnProperty("error")){
                console.log("Error:" + data["error"][1]);
                console.log("Cause:" + data["cause"]);
                showErrorMessage(data["error"][1]);
            }
            else {
            
            // removing Error Section visibility
            errMsg = document.getElementById('errMsg');
            errMsg.style.display = "None";

            // Applying table visibility
            tbldivHTML = document.getElementById('tbldivHTML');
            tbldivHTML.style.display = "block";

            var data = JSON.parse(data);
            console.log(data);
            
            syndata = document.getElementById('tblHTML');
            syndata.innerHTML = "";

            var row1 = document.createElement('tr');
            row1.className = "border-bottom";
            var cell1 = document.createElement('td');
            var cell2 = document.createElement('td');
            var cell3 = document.createElement('td');
            var cell4 = document.createElement('td');
            var cell5 = document.createElement('td');
            var cell6 = document.createElement('td');

            cell1.className = "a";
            var text1 = document.createTextNode("Synset ID");
            cell1.appendChild(text1);
            
            cell2.className = "b";
            var text2 = document.createTextNode(":");
            cell2.appendChild(text2);
            
            cell3.className = "c";
            var text3 = document.createTextNode(data["synset_id"]);
            cell3.appendChild(text3);

            cell4.className = "a";
            var text4 = document.createTextNode("POS");
            cell4.appendChild(text4);
            
            cell5.className = "b";
            cell5.style.width = "14px";
            var text5 = document.createTextNode(":");
            cell5.appendChild(text5);
            
            cell6.className = "c";
            var text6 = document.createTextNode(data["pos"]);
            cell6.appendChild(text6);
            
            row1.appendChild(cell1);
            row1.appendChild(cell2);
            row1.appendChild(cell3);
            row1.appendChild(cell4);
            row1.appendChild(cell5);
            row1.appendChild(cell6);
            syndata.appendChild(row1);

            /////////////////////////////

            var row2 = document.createElement('tr');
            row2.className = "border-bottom";
            cell1 = document.createElement('td');
            cell2 = document.createElement('td');
            cell3 = document.createElement('td');

            cell1.className = "a";
            text1 = document.createTextNode("Synonyms");
            cell1.appendChild(text1);
            
            cell2.className = "b";
            text2 = document.createTextNode(":");
            cell2.appendChild(text2);
            
            cell3.className = "c";
            cell3.colSpan = "4";
            if(data["synonyms"].length == 0){
                cell3.style.color = "blue";
                text3 = document.createTextNode("No Synonyms Available");
                cell3.appendChild(text3);
            }
            else{
                for(i=0;i<data["synonyms"].length;i++)
                {
                    var a = document.createElement("a");
                    a.textContent = " " + data["synonyms"][i] + ",";
                    a.href = "wordnet?langno="+ tlang +"&query=" + data["synonyms"][i];
                    // a.appendChild(linkText);
                    cell3.appendChild(a);
                }
            }
            
            
            row2.appendChild(cell1);
            row2.appendChild(cell2);
            row2.appendChild(cell3);
            syndata.appendChild(row2);

            ////////////////////////

            var row3 = document.createElement('tr');
            row3.className = "border-bottom";
            cell1 = document.createElement('td');
            cell2 = document.createElement('td');
            cell3 = document.createElement('td');

            cell1.className = "a";
            text1 = document.createTextNode("Gloss");
            cell1.appendChild(text1);
            
            cell2.className = "b";
            text2 = document.createTextNode(":");
            cell2.appendChild(text2);
            
            cell3.className = "c";
            cell3.colSpan = "4";
            cell3.style.color = "red";
            if(data["gloss"][0] == ''){
                text3 = document.createTextNode("No Gloss Available");
            }
            else{
                text3 = document.createTextNode(data["gloss"][0]);
            }
            cell3.appendChild(text3);
            
            row3.appendChild(cell1);
            row3.appendChild(cell2);
            row3.appendChild(cell3);
            syndata.appendChild(row3);

            ///////////////////

            var row4 = document.createElement('tr');
            row4.className = "border-bottom";
            cell1 = document.createElement('td');
            cell2 = document.createElement('td');
            cell3 = document.createElement('td');

            cell1.className = "a";
            text1 = document.createTextNode("Example Statement");
            cell1.appendChild(text1);
            
            cell2.className = "b";
            text2 = document.createTextNode(":");
            cell2.appendChild(text2);
            
            cell3.className = "c";
            cell3.colSpan = "4";
            cell3.style.color = "green";
            if(data["gloss"][1] == ''){
                text3 = document.createTextNode("No Example Statement Available");
            }
            else{
                text3 = document.createTextNode(data["gloss"][1]);
            }
            cell3.appendChild(text3);
            
            row4.appendChild(cell1);
            row4.appendChild(cell2);
            row4.appendChild(cell3);
            syndata.appendChild(row4);

          }
          
        },
        error: function(response){
            console.log(response["status"]);
            if(response["status"] == 404){
                showErrorMessage("Page Not Found");
            }
            else if(response["status"] == 500){
                showErrorMessage("Internal Server Error");
            }
        }
      });
}

function createTbl(synset_id,langno,pos,urlLink,tblTitle,tblParams,btnValue,start)
{
    // removing Error Section visibility
    errMsg = document.getElementById('errMsg');
    errMsg.style.display = "None";

    // Applying table visibility
    tbldivHTML = document.getElementById('tbldivHTML');
    tbldivHTML.style.display = "block";

    // settting table title
    tblTitleHTML = document.getElementById("tblTitle").innerHTML = tblTitle;
    
    //generating Table
    tblHTML = document.getElementById('tblHTML');
    tblHTML.innerHTML = "";
    //var pos = document.getElementById("pos").innerHTML.toLowerCase();
    $.ajax({
        url: urlLink,
        data: {
            'synset_id': synset_id,
            'langno': langno,
            'pos': pos,
            'start': start
        },
        dataType: 'json',
        beforeSend: function(){
            // Show image container
            console.log("Loading...");
            //$("#loader").show();
           },
        success: function (data) {
            if(data.hasOwnProperty("error")){
                if(btnValue == "11"){
                    if(data["error"][0] == "2"){
                        $("#start").trigger("change");
                        document.getElementById("start").value = (start + 25).toString();
                        document.getElementById("nextOnto").style.display = "none";
                        document.getElementById("currentLength").value = "25";
                    }
                    else if(data["error"][0] == "1"){
                        document.getElementById("start").value = 0;
                        document.getElementById("currentLength").value = "25";
                        document.getElementById("nextOnto").style.display = "none";
                        document.getElementById("prevOnto").style.display = "none";
                    }
                }
                console.log("Error:" + data["error"][1]);
                console.log("Cause:" + data["cause"]);
                showErrorMessage(data["error"][1]);
            }
            else{
                var data = JSON.parse(data);
                console.log(data);
                var i,j,k;

                //creating TblHeader
                var thead = document.createElement('thead');
                thead.style.position = "sticky";
                thead.style.top = "0";

                //creating TblHeader Row
                var row = document.createElement('tr');
                row.className = "border-bottom";

                for(i=0;i<tblParams.headerList.length;i++)
                {
                    var cell = document.createElement('th');
                    cell.className = "d";
                    cell.style.position = "sticky";
                    cell.style.top = "0";
                    cell.style.background = "#eee";

                    var text = document.createTextNode(tblParams.headerList[i]);
                    cell.appendChild(text);
                    row.appendChild(cell);
                }
                
                thead.append(row);
                tblHTML.appendChild(thead);

                //creating TblBody
                var tbody = document.createElement("tbody");
                var colCount = tblParams.colCount; //denotes number of columns in the table, if 3 table is for onto, else for any other *.nymy for ex. Hypernymy,Hyponymy
                var cellColSpan = 0;
                var noData;
                var currentLength = Object.keys(data).length;
                for(i=0;i<Object.keys(data).length;i++)
                {
                    
                    noData = false;
                    cellColSpan = 0;
                    var row = document.createElement('tr');
                    row.className = "border-bottom";
                    
                    // Checking if data available or not, if not then setting colCount 1 will only print first column data and other columns will be empty.
                    if(data[i.toString()][3][0] == "1"){
                        noData = true;
                        row.style.backgroundColor = "#FFCCCB";
                        
                    }
                    for(j=0;j<colCount;j++)
                    {
                        // console.log("i:" + i + " j:" + j);
                        // console.log("j:"+j);
                        var cell = document.createElement('td');
                        cell.className = "d";
                        // cell.style.color = tblParams["colColor"][j];
                        // cell.style.fontWeight = "bold";
                        // cell.style.wordBreak = "break-word";
                        cell.style.overflowWrap = "break-word";
                        cell.style.wordWrap = "break-all";
                        cell.colSpan = cellColSpan.toString();
                        // console.log("Colspan of cell:" + cell.colSpan);
                        // cell.style.textAlign = tblParams["colTextAlign"][j];    
                        
                        switch(j)
                        {
                            case 0:
                                cell.style.color = "black";
                                var text = document.createTextNode(data[i.toString()][j]);
                                cell.appendChild(text);
                                break;
                            case 1:
                                if(colCount == 4)
                                {
                                    cell.style.textAlign = "left";
                                    for(k=0;k<data[i.toString()][j].length;k++)
                                    {
                                        var a = document.createElement("a");
                                        a.textContent = data[i.toString()][j][k] + ", ";
                                        a.href = "wordnet?langno="+ langno +"&query=" + data[i.toString()][j][k];
                                        // a.appendChild(linkText);
                                        cell.appendChild(a);
                                    }
                                }
                                else
                                {
                                    var a = document.createElement("a");
                                    a.textContent = data[i.toString()][j];
                                    a.href = "showonto?synset_id="+ synset_id + "&oid=" + data[i.toString()][j-1] +"&langno=" + langno;
                                    // a.appendChild(linkText);
                                    cell.appendChild(a);
                                    //var text = document.createTextNode(data[i.toString()][j]);
                                    //cell.appendChild(text);
                                }
                                break;
                            case 2:
                                if(colCount == 4)
                                {
                                    cell.style.color = "red";
                                    cell.style.textAlign = "left";
                                    var text = document.createTextNode(data[i.toString()][2][0]);
                                    cell.appendChild(text);
                                }
                                else
                                {
                                    cell.style.textAlign = "left";
                                    var text;
                                    if(noData){
                                        // console.log("In No Data");
                                        cell.style.color = "black";
                                        cell.style.fontWeight = "bold";
                                        text = document.createTextNode(data[i.toString()][j][1]);
                                    }
                                    else{   
                                        cell.style.color = "green";
                                        text = document.createTextNode(data[i.toString()][j]);    
                                    }  
                                    cell.appendChild(text); 
                                }
                                break;
                            case 3:
                                cell.style.textAlign = "left";
                                var text;
                                if(noData){
                                    // console.log("In No Data");
                                    cell.style.color = "black";
                                    cell.style.fontWeight = "bold";
                                    text = document.createTextNode(data[i.toString()][j][1]);
                                }
                                else{
                                    cell.style.color = "green";   
                                    text = document.createTextNode(data[i.toString()][2][1]);    
                                }  
                                cell.appendChild(text); 
                                break;
                            default:
                                cell.style.color = "black";
                                var text = document.createTextNode(data[i.toString()][j]);
                                cell.appendChild(text);
                                break;
                        }
                        cellColSpan = 0;
                        row.appendChild(cell);
                        if(noData){
                            j += colCount - 2;
                            cellColSpan =  colCount - 1;
                            console.log("Colspan: " + cellColSpan);
                        }
                    }
                    tbody.appendChild(row);
                }
                tblHTML.appendChild(tbody);
                if(btnValue == "11"){
                    $("#start").trigger("change");
                    document.getElementById("start").value = (start + currentLength).toString();
                    document.getElementById("currentLength").value = currentLength.toString();
                    $("#currentLength").trigger("change");
                }                
            }
        },
        error: function(response){
            console.log(response["status"]);
            if(response["status"] == 404){
                showErrorMessage("Page Not Found");
            }
            else if(response["status"] == 500){
                showErrorMessage("Internal Server Error");
            }
        },
        complete: function(){
            // Show image container
            console.log("finished");
            //$("#loader").show();
           }
    })
}

// function fetchRecomendationData(){
function showErrorMessage(msg){

    // removing table visibility
    tblHTML = document.getElementById('tbldivHTML');
    tblHTML.style.display = "None";
    errText = document.getElementById("errText");
    errText.innerHTML = msg;
    errMsg = document.getElementById("errMsg");
    errMsg.style.display = "block";
    
    // errText.style.display = "inline";
    
}
function fetchRecomendationData(){
    var currentRequest = null;



    var word = document.getElementById("queryword").value;
    word = word.trim()
    var l = document.getElementById("lang");
    var lang = l.options[l.selectedIndex].value
    
    
    console.log(word.length)
    console.log(word)
    console.log(lang)

  
    if(word.length != 0){
        console.log(word)
    
        var ajaxReq = 'ToCancelPrevReq';
        ajaxReq =$.ajax({
            url: 'word',
            data: {
            'q': word,
            'langno': lang
            },
            dataType: 'json',
            beforeSend : function() {
                if(ajaxReq != 'ToCancelPrevReq' && ajaxReq.readyState < 4) {
                    ajaxReq.abort();
                }
            },
            success: function (data) {
                if (data) {
                    var data = JSON.parse(data);
                    // console.log(word)
                    // console.log(data);
                    var inp = document.getElementById("queryword");
                    // inp.focus()
                    autocomplete(inp,data)
                }
            }
        });
    }
    else{
        console.log("close")
        var list = document.getElementById("autocomplete-list");
        list.remove();
    }
}

function fetchReverseOnto(oid){
    var selectedOntoID = document.getElementById("selectedOntoID");
    selectedOntoID.value = oid;
    var tlangno = document.getElementById('tlangOnto').value;
    var btnValue = "11";
    var synset_id = oid;
    var pos = "noun";

    document.getElementById("start").value = "0";
    document.getElementById("currentLength").value = "25";
    fetchTblData(synset_id,tlangno,pos,btnValue);
}


$(document).ready(function(){
  
    $("#lang").on('change',function(){
        localStorage.setItem('langSelected',$(this).val()) ;
        $("#lang").val(localStorage.getItem("langSelected"));
    });

    $("#tlang, #tlangOnto").on('change',function(){
        localStorage.setItem('tlangSelected',$(this).val()) ;
        $("#tlang, #tlangOnto").val(localStorage.getItem("tlangSelected"));
    });

    $(window).on('load',function(){
        $("#lang").val(localStorage.getItem("langSelected"));
        $("#tlang, #tlangOnto").val(localStorage.getItem("tlangSelected"));
    });

    
    
    // langno = document.getElementById("lang").value;
   
    $("#aBtnGroup button").on('click',function(){
        var thisBtn = $(this);
        var btnValue = thisBtn.val();
        var tlangno =  $("#tlang").val();
        var synset_id = $("#s_id").text();
        var pos = document.getElementById("pos").innerHTML.toLowerCase();
        
        fetchTblData(synset_id,tlangno,pos,btnValue);
        // if(thisBtn.val() == '0'){
        //     getSynsetData(tlangno)
        // }
        thisBtn.siblings().removeClass('active');
        thisBtn.addClass('active');
        thisBtn.siblings().removeClass('btn-info').addClass('btn-outline-info');
        thisBtn.removeClass('btn-outline-info').addClass('btn-info');
       //alert(thisBtn.val());
    });

    $('#tlang').on('change',function(){
        var tlang = $(this);
        var tlangno = tlang.val();
        var btnValue = $("button.btn-info").val();
        var synset_id = $("#s_id").text();
        var pos = document.getElementById("pos").innerHTML.toLowerCase();

        //preserve k and cl
        fetchTblData(synset_id,tlangno,pos,btnValue);
        //alert($(this).val());
    });

    $('#tlangOnto').on('change',function(){
        var start = document.getElementById("start").value;
        console.log(start);
        var currentLength = document.getElementById("currentLength").value;
        console.log(currentLength);
        if((parseInt(start) - parseInt(currentLength))>0){
            document.getElementById("start").value = (parseInt(start) - parseInt(currentLength)).toString();
        }
        else{
            document.getElementById("start").value = "0";
        }
        
        console.log($("#start").val());
        
        var tlang = $(this);
        var tlangno = tlang.val();
        var pos = "noun";
        var btnValue = "11";
        var selectedOntoID = document.getElementById("selectedOntoID").value;
        fetchTblData(selectedOntoID,tlangno,pos,btnValue);
        //alert($(this).val());
    });
    
    $('#prevOnto').on('click',function(){
        var start = document.getElementById("start").value;
        console.log(start);
        var currentLength = document.getElementById("currentLength").value;
        console.log(currentLength);
        if((parseInt(start) - parseInt(currentLength) - 25)>0){
            document.getElementById("start").value = (parseInt(start) - parseInt(currentLength) - 25).toString();
        }
        else{
            document.getElementById("start").value = "0";
        }
        console.log($("#start").val());
        console.log("prevStart");
        var tlangno = $("#tlangOnto").val();
        var btnValue = "11";
        var synset_id = document.getElementById("selectedOntoID").value;
        var pos = "noun";
        fetchTblData(synset_id,tlangno,pos,btnValue);
        //alert($(this).val());
    });

    $('#nextOnto').on('click',function(){
        // var start = document.getElementById("start").value;
        // var currentLength = document.getElementById("currentLength").value;
        // var newstart = document.getElementById("start").value = start - currentLength - 25;
        // console.log("newStart");
        console.log("nextStart");
        var tlangno = $("#tlangOnto").val();
        var btnValue = "11";
        var synset_id = document.getElementById("selectedOntoID").value;
        var pos = "noun";
        fetchTblData(synset_id,tlangno,pos,btnValue);
        //alert($(this).val());
    });

    $("#start").change(function(){
        console.log("in prevonto dissable enable");
        var start = parseInt(document.getElementById("start").value);
        if(start <= 0){
            console.log("disabling previous")
            $("#prevOnto").css("display", "none");
        }
        else{
            console.log("enabling previous");
            $("#prevOnto").css("display", "inline-block");
        }
    });

    $("#currentLength").change(function(){
        console.log("in nextonto dissable enable");
        var currentLength = parseInt(document.getElementById("currentLength").value);
        if(currentLength < 25){
            console.log("enabling next");
            $("#nextOnto").css("display", "none");
        }
        else{
            console.log("enabling next");
            $("#nextOnto").css("display", "inline-block");
        }
    });

    $('#queryword').change(function(){
        // console.log($(this).val());
        // var word = $(this).val();
        // var lang = $("#lang").val();
        // alert('value changed');
        fetchRecomendationData();
    });

    var typingTimer;                //timer identifier
    var doneTypingInterval = 500;  //time in ms, 5 second for example
    var $input = $('#queryword');

    //on keyup, start the countdown
    $input.on('input', function () {
        clearTimeout(typingTimer);
        typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });

    //on keydown, clear the countdown 
    $input.on('keydown', function () {
        clearTimeout(typingTimer);
    });

    function doneTyping () {
        fetchRecomendationData();
    }







});

function fetchTableSynsetTitle(tlang){
    switch(tlang) {
        case "0":
            return "Regional Synset : Hindi";
            break;
        case "1":
            return "Regional Synset : English";
            break;
        case "2":
            return "Regional Synset : Assamese";
            break;
        case "3":
            return "Regional Synset : Bengali";
            break;
        case "4":
            return "Regional Synset : Bodo";
            break;
        case "5":
            return "Regional Synset : Gujarati";
            break;
        case "6":
            return "Regional Synset : Kannada";
            break;
        case "7":
            return "Regional Synset : Kashmiri";
            break;
        case "8":
            return "Regional Synset : Konkani";
            break;
        case "9":
            return "Regional Synset : Malyalam";
            break;
        case "10":
            return "Regional Synset : Manipuri";
            break;
        case "11":
            return "Regional Synset : Marathi";
            break;
        case "12":
            return "Regional Synset : Nepali";
            break;
        case "13":
            return "Regional Synset : Sanskrit";
            break;
        case "14":
            return "Regional Synset : Tamil";
            break;
        case "15":
            return "Regional Synset : Telugu";
            break;
        case "16":
            return "Regional Synset : Punjabi";
            break;
        case "17":
            return "Regional Synset : Urdu";
            break;
        case "18":
            return "Regional Synset : Oriya";
            break;
        default:
            return "Regional Synset";
            break;
      } 
}  


