
  
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

function funct(w){
    //alert(w);
    queryword = document.getElementById("queryword");
    search_button = document.getElementById("search_button");

    queryword.value = queryword.value + w;
    search_button.focus();
}

synset = 1
function next(l,wl){
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
        text = "wordnet?query="+wl[synset][2][i];
        tag.setAttribute("href",text)
        var textnode = document.createTextNode(wl[synset][2][i]+",")
        tag.appendChild(textnode);
        synonyms.appendChild(tag);
    }
   
    
    gloss = document.getElementById('gloss').innerHTML = wl[synset][3][0];
    ex = document.getElementById('ex').innerHTML = wl[synset][3][1];
    enGloss = document.getElementById('enGloss').innerHTML = wl[synset][4];   
    synset = synset+1;
}

function prev(l,wl){
    
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
        text = "wordnet?query="+wl[synset-1][2][i];
        tag.setAttribute("href",text)
        var textnode = document.createTextNode(wl[synset-1][2][i]+",")
        tag.appendChild(textnode);
        synonyms.appendChild(tag);
    }
   
    gloss = document.getElementById('gloss').innerHTML = wl[synset-1][3][0];
    ex = document.getElementById('ex').innerHTML = wl[synset-1][3][1];
    enGloss = document.getElementById('enGloss').innerHTML = wl[synset-1][4];   
}

