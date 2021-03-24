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
    langno = $('#lang').val()
    console.log(q)
    // alert(q)
    $.ajax({
        url: 'word',
        data: {
            'q' : q ,
            'langno' : langno
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
    s_id = document.getElementById('s_id').innerHTML = wl[synset][0];

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
    
    createOntoTbl(wl[synset][0],0);

    synset = synset+1;
}


function prev(l,wl,ln){
    
    document.getElementById('next').style.display = null;
    if((synset-2)==0){
        document.getElementById('prev').style.display = "none"; 
    }
    synset = synset-1;
    num = document.getElementById('num').innerHTML = synset;
    s_id = document.getElementById('s_id').innerHTML = wl[synset-1][0];
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
    
    createOntoTbl(wl[synset-1][0],0);
    
}



function createOntoTbl(synset_id,langno)
{
    // console.log(exm)
    $.ajax({
        url: 'fetch_onto',
        data: {
          'synset_id': synset_id,
          'langno': langno
        },
        dataType: 'json',
        success: function (data) {
          if (data) {
            var data = JSON.parse(data);
            console.log(data);
            ontodata = document.getElementById('onto_data');
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

function getSynsetData(tlang){
    var sId = document.getElementsByTagName("")
}


var word;

$(document).ready(function(){
    langno = document.getElementById("lang").value;
   
    $("#aBtnGroup button").on('click',function(){
        var thisBtn = $(this);
        var tlangno =  $("#tlang").val();
        if(thisBtn.val() == '0'){
            getSynsetData(tlangno)
        }
        thisBtn.siblings().removeClass('btn-info').addClass('btn-outline-info');
        thisBtn.removeClass('btn-outline-info').addClass('btn-info');
       // alert(thisBtn.val());
    });

    $('#tlang').on('change',function(){
        
        alert($(this).val());
    });
    
      $('#queryword').on('change',function(){
        // search();
        // alert('value changed');
    });
});

  



