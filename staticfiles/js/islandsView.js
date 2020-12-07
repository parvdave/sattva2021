function viewisland(number) {
  var islands = document.getElementsByClassName("islands");
  var bgIsland = document.getElementById("bgIsland");

  var dict = { 1 : "./images/islands/FINAL_ISLAND1.png" , 
            2 : "./images/islands/FINAL_ISLAND2.png" ,
            3 : "./images/islands/FINAL_ISLAND3.png" ,
            4 : "./images/islands/FINAL_ISLAND4.png" ,
            5 : "./images/islands/FINAL_ISLAND5.png" ,
            6 : "./images/islands/FINAL_ISLAND6.png" ,
            7 : "./images/islands/FINAL_ISLAND7.png" ,
          };

  for (var i = 0; i < islands.length; i++) {
  islands[i].style.display = 'none';
  }

  bgIsland.src = dict[number];
}

function imgHover(number) {
  var big = { 0 : "big1" , 
            1 : "big2" ,
            2 : "big3" ,
            3 : "big4" ,
            4 : "big5" ,
            5 : "big6" ,
            6 : "big7" ,
          };

  var small = { 0 : "small1" , 
            1 : "small2" ,
            2 : "small3" ,
            3 : "small4" ,
            4 : "small5" ,
            5 : "small6" ,
            6 : "small7" ,
          };


  var small = document.getElementById(small[number]);
  var big = document.getElementById(big[number]);
  small.style.opacity = 0;
  big.style.opacity = 1;
  big.style.zIndex = 6;

}

function imgOut(number) {

    var big = { 0 : "big1" , 
            1 : "big2" ,
            2 : "big3" ,
            3 : "big4" ,
            4 : "big5" ,
            5 : "big6" ,
            6 : "big7" ,
          };

  var small = { 0 : "small1" , 
            1 : "small2" ,
            2 : "small3" ,
            3 : "small4" ,
            4 : "small5" ,
            5 : "small6" ,
            6 : "small7" ,
          };
          
  var small = document.getElementById(small[number]);
  var big = document.getElementById(big[number]);
  small.style.opacity = 1;
  big.style.opacity = 0;
  big.style.zIndex = 2;
  small.style.zIndex = 2;
}