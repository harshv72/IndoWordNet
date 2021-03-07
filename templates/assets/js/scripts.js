
  
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

var slider_img = document.querySelector('.slider-img');
var images = ['a.jpg', 'b.jpg', 'c.jpg', 'd.jpg', 'e.jpg'];
var i = 0;

function prev(){
	if(i <= 0) i = images.length;	
	i--;
	return setImg();			 
}

function next(){
	if(i >= images.length-1) i = -1;
	i++;
	return setImg();			 
}

function setImg(){
	return slider_img.setAttribute('src', "images/"+images[i]);
	
}