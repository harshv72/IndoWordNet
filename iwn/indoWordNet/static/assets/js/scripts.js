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

function autocomplete(inp, arr) {
    var currentFocus;
    console.log("1")
    var a, b, i, val = inp.value;
    currentFocus = -1;
    // a = document.createElement("DIV");
    // a.setAttribute("id", "autocomplete-list");
    // a.setAttribute("class", "autocomplete-items ");
    // inp.parentNode.appendChild(a);
    if (arr.length == 0){
        b = document.getElementById("l0").style.display = null; 
        b.innerHTML = "<strong>Not Found </strong>";
        b.addEventListener("click", function(e) {
            inp.value = this.getElementsByTagName("input")[0].value;
            closeAllLists();
        });
    
    }
    else{
        for (i = 0; i < arr.length; i++) {
            id = "l"+i.toString();
            console.log(id)
            b = document.getElementById(id)
            b.innerHTML = "<strong>" + arr[i] + "</strong>";
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            b.style.display = null
            b.addEventListener("click", function(e) {
                inp.value = this.getElementsByTagName("input")[0].value;
                closeAllLists();
            b.style.display = null
            });
        };
        
        }
          
    }
    
    function closeAllLists(elmnt) {
      for (var i = 0; i < 10; i++) {
            id = "l"+i.toString();
            // console.log(id);
            b = document.getElementById(id);
            b.style.display = "none";
        }
      }
    
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });


function search(){
    q=$('#queryword').val()
    tlangno = $('#lang').val()
    console.log(q)
    // alert(q)
    $.ajax({
        url: 'word',
        data: {
            'q' : q ,
            'langno' : tlangno
        },
        dataType: 'json',
        success: function(data){
            word = JSON.parse(data);
            // alert(word)
            console.log(word)
            // alert($(this).val());
            autocomplete(document.getElementById('queryword'),word)
        }

     });
}

function funct(w){
    //alert(w);
    queryword = document.getElementById("queryword");
    search_button = document.getElementById("search_button");

    queryword.value = queryword.value + w;
    // search()
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
    
    //console.log(ele);
    for(i = 0; i < ele.length; i++) { 
        //console.log(ele[i].className)
        if(ele[i].className.includes("btn-info")){
            //console.log(ele[i].value)
            fetch_tbl_data(synset_id,tlangno,ele[i].value);
            
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
    
    //console.log(ele);
    for(i = 0; i < ele.length; i++) { 
        //console.log(ele[i].className)
        if(ele[i].className.includes("btn-info")){
            //console.log(ele[i].value)
            fetch_tbl_data(synset_id,tlangno,ele[i].value);
            
            break; 
        }
    }
    
}

function fetch_tbl_data(synset_id,tlangno,btnValue){
    console.log(synset_id)
    console.log(tlangno)
    console.log(btnValue)
    switch(btnValue){
        case "0":
            getSynsetData(synset_id,tlangno);
            break;
        case "1":
            createHyperTbl(synset_id,tlangno);
            break;
        case "2":
            createHypoTbl(synset_id,tlangno);
            break;
        case "6":
            console.log("Fetching Ontology data");
            createOntoTbl(synset_id,tlangno);
            console.log("Fetched Ontology data");
            break;
        default:
            console.log("default case in fetch_tbl_data");
            break;
    }
}

function createOntoTbl(synset_id,tlangno)
{
    document.getElementById("tblLabel").innerHTML = "Ontology";
    //var synset_id = document.getElementById("s_id").innerHTML;
    $.ajax({
        url: 'fetch_onto',
        data: {
          'synset_id': synset_id,
          'langno': tlangno
        },
        dataType: 'json',
        success: function (data) {
          if (data) {
            var data = JSON.parse(data);
            console.log(data);
            ontodata = document.getElementById('tbl_data');
            ontodata.innerHTML = "";

            //Adding Table Header
            var row = document.createElement('tr');
            row.className = "border-bottom";

            var cell1 = document.createElement('th');
            var cell2 = document.createElement('th');
            var cell3 = document.createElement('th');

            cell1.className = "d";
            cell2.className = "d";
            cell3.className = "d";

            var text1 = document.createTextNode("Onto Id");
            var text2 = document.createTextNode("Onto Label");
            var text3 = document.createTextNode("Onto Description");

            cell1.appendChild(text1);
            cell2.appendChild(text2);
            cell3.appendChild(text3);

            row.appendChild(cell1);
            row.appendChild(cell2);
            row.appendChild(cell3);

            ontodata.appendChild(row); // Table Header row added

            //Adding Table Data Rows
            var i,j;
            for (i=0; i <data.length;i++){  
                row = document.createElement('tr');
                row.className = "border-bottom";
         
                for(j=0;j<3;j++){
                    var cell = document.createElement('td');
                    cell.className = "d";
                    cell.style.fontWeight = "bold";
                    switch(j){
                        case 0:
                            cell.style.color = "black";
                            break;
                        case 1:
                            cell.style.color = "blue";
                            break;
                        case 2:
                            cell.style.color = "green";
                            break;
                        default:
                            cell.style.color = "black";
                    }
                    var text = document.createTextNode(data[i.toString()][j]);
                    cell.appendChild(text);
                    row.appendChild(cell);
                }
                ontodata.appendChild(row);
            }
          }
        }
      });
}

function createHyperTbl(synset_id,tlangno)
{
    document.getElementById("tblLabel").innerHTML = "Hypernymy";
    var pos = document.getElementById("pos").innerHTML.toLowerCase();
    $.ajax({
        url: 'fetch_hyper',
        data: {
          'synset_id': synset_id,
          'langno': tlangno,
          'pos':pos
        },
        dataType: 'json',
        success: function (data) {
          if (data) {
            var data = JSON.parse(data);
            console.log(data);
            hyperdata = document.getElementById('tbl_data');
            hyperdata.innerHTML = "";

            //Adding Table Header
            var row = document.createElement('tr');
            row.className = "border-bottom";

            var cell1 = document.createElement('th');
            var cell2 = document.createElement('th');
            var cell3 = document.createElement('th');
            var cell4 = document.createElement('th');

            cell1.className = "d";
            cell2.className = "d";
            cell3.className = "d";
            cell4.className = "d";

            var text1 = document.createTextNode("Hypernymy Id");
            var text2 = document.createTextNode("Synonyms");
            var text3 = document.createTextNode("Gloss");
            var text4 = document.createTextNode("Example");

            cell1.appendChild(text1);
            cell2.appendChild(text2);
            cell3.appendChild(text3);
            cell4.appendChild(text4);

            row.appendChild(cell1);
            row.appendChild(cell2);
            row.appendChild(cell3);
            row.appendChild(cell4);

            hyperdata.appendChild(row); // Table Header row added

            //Adding Table Data Rows
            var i,j;
            for (i=0; i <data.length;i++){  
                row = document.createElement('tr');
                row.className = "border-bottom";
         
                for(j=0;j<4;j++){
                    var cell = document.createElement('td');
                    cell.style.wordBreak = "break-all";
                    cell.className = "d";
                    cell.style.fontWeight = "bold";
                    switch(j){
                        case 0:
                            cell.style.color = "black";
                            break;
                        case 1:
                            cell.style.color = "blue";
                            break;
                        case 2:
                            cell.style.color = "red";
                            break;
                        case 3:
                            cell.style.color = "green";
                            break;
                        default:
                            cell.style.color = "black";
                    }
                    if(j == 1)
                    {
                        for(k=0;k<data[i.toString()][j].length;k++)
                        {
                            var a = document.createElement("a");
                            a.textContent = " " + data[i.toString()][j][k] + ",";
                            a.href = "wordnet?langno="+ tlangno +"&query=" + data[i.toString()][j][k];
                            // a.appendChild(linkText);
                            cell.appendChild(a);
                        }
                    }
                    else
                    {
                        if(j == 2)
                        {
                            var text = document.createTextNode(data[i.toString()][2][0]);
                            cell.appendChild(text);
                        }
                        else if(j == 3)
                        {
                            var text = document.createTextNode(data[i.toString()][2][1]);
                            cell.appendChild(text);
                        }
                        else
                        {
                            var text = document.createTextNode(data[i.toString()][j]);
                            cell.appendChild(text);
                        }
                    }
                    
                    row.appendChild(cell);
                }
                hyperdata.appendChild(row);
            }
          }
          else{
              console.log("No data");
          }
        }
      });
}

function createHypoTbl(synset_id,tlangno)
{
    document.getElementById("tblLabel").innerHTML = "Hyponymy";
    var pos = document.getElementById("pos").innerHTML.toLowerCase();
    $.ajax({
        url: 'fetch_hypo',
        data: {
          'synset_id': synset_id,
          'langno': tlangno,
          'pos':pos
        },
        dataType: 'json',
        success: function (data) {
          if (data) {
            var data = JSON.parse(data);
            console.log(data);
            hypodata = document.getElementById('tbl_data');
            hypodata.innerHTML = "";

            //Adding Table Header
            var row = document.createElement('tr');
            row.className = "border-bottom";

            var cell1 = document.createElement('th');
            var cell2 = document.createElement('th');
            var cell3 = document.createElement('th');
            var cell4 = document.createElement('th');

            cell1.className = "d";
            cell2.className = "d";
            cell3.className = "d";
            cell4.className = "d";

            var text1 = document.createTextNode("Hyponymy Id");
            var text2 = document.createTextNode("Synonyms");
            var text3 = document.createTextNode("Gloss");
            var text4 = document.createTextNode("Example");

            cell1.appendChild(text1);
            cell2.appendChild(text2);
            cell3.appendChild(text3);
            cell4.appendChild(text4);

            row.appendChild(cell1);
            row.appendChild(cell2);
            row.appendChild(cell3);
            row.appendChild(cell4);

            hypodata.appendChild(row); // Table Header row added

            //Adding Table Data Rows
            var i,j;
            for (i=0; i <data.length;i++){  
                row = document.createElement('tr');
                row.className = "border-bottom";
         
                for(j=0;j<4;j++){
                    var cell = document.createElement('td');
                    cell.style.wordBreak = "break-all";
                    cell.className = "d";
                    cell.style.fontWeight = "bold";
                    switch(j){
                        case 0:
                            cell.style.color = "black";
                            break;
                        case 1:
                            cell.style.color = "blue";
                            break;
                        case 2:
                            cell.style.color = "red";
                            break;
                        case 3:
                            cell.style.color = "green";
                            break;
                        default:
                            cell.style.color = "black";
                    }
                    if(j == 1)
                    {
                        for(k=0;k<data[i.toString()][j].length;k++)
                        {
                            var a = document.createElement("a");
                            a.textContent = " " + data[i.toString()][j][k] + ",";
                            a.href = "wordnet?langno="+ tlangno +"&query=" + data[i.toString()][j][k];
                            // a.appendChild(linkText);
                            cell.appendChild(a);
                        }
                    }
                    else
                    {
                        if(j == 2)
                        {
                            var text = document.createTextNode(data[i.toString()][2][0]);
                            cell.appendChild(text);
                        }
                        else if(j == 3)
                        {
                            var text = document.createTextNode(data[i.toString()][2][1]);
                            cell.appendChild(text);
                        }
                        else
                        {
                            var text = document.createTextNode(data[i.toString()][j]);
                            cell.appendChild(text);
                        }
                        
                    }
                    
                    row.appendChild(cell);
                }
                hypodata.appendChild(row);
            }
          }
          else{
              console.log("No data");
          }
        }
      });
}

function getSynsetData(synset_id,tlangno){

    var langText = fetch_tbl_synset_title(tlangno);
    document.getElementById("tblLabel").innerHTML = langText;
    //var synset_id = document.getElementById("s_id").innerHTML;
    $.ajax({
        url: 'fetch_synset',
        data: {
          'synset_id': synset_id,
          'langno': tlangno
        },
        dataType: 'json',
        success: function (data) {
          if (data) {
            var data = JSON.parse(data);
            console.log(data);
            
            syndata = document.getElementById('tbl_data');
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
            console.log(data["synonyms"].length)
            for(i=0;i<data["synonyms"].length;i++)
            {
                var a = document.createElement("a");
                a.textContent = " " + data["synonyms"][i] + ",";
                a.href = "wordnet?langno="+ tlang +"&query=" + data["synonyms"][i];
               // a.appendChild(linkText);
                cell3.appendChild(a);
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
            text3 = document.createTextNode(data["gloss"][0]);
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
            text3 = document.createTextNode(data["gloss"][1]);
            cell3.appendChild(text3);
            
            row4.appendChild(cell1);
            row4.appendChild(cell2);
            row4.appendChild(cell3);
            syndata.appendChild(row4);

          }
          else{
              console.log("No data found");
          }
        }
      });
}


var word;

$(document).ready(function(){
    langno = document.getElementById("lang").value;
   
    $("#aBtnGroup button").on('click',function(){
        var thisBtn = $(this);
        var btnValue = thisBtn.val();
        var tlangno =  $("#tlang").val();
        var synset_id = $("#s_id").text();
        
        fetch_tbl_data(synset_id,tlangno,btnValue);
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
        fetch_tbl_data(synset_id,tlangno,btnValue);
        //alert($(this).val());
    });
    
      $('#queryword').on('change',function(){
        // search();
        // alert('value changed');
    });
});

function fetch_tbl_synset_title(tlang){
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



