function viewisland(number) {
  var islands = document.getElementsByClassName("islands");
  var bgIsland = document.getElementById("bgIsland");
  
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
  var island = { 0 : "island1" , 
            1 : "island2" ,
            2 : "island3" ,
            3 : "island4" ,
            4 : "island5" ,
            5 : "island6" ,
            6 : "island7" ,
          }; 

  var small = document.getElementById(small[number]);
  var big = document.getElementById(big[number]);
  var island = document.getElementById(island[number]);
  small.style.opacity = 0;
  big.style.opacity = 1;
  island.style.zIndex = 3;
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
  var island = { 0 : "island1" , 
            1 : "island2" ,
            2 : "island3" ,
            3 : "island4" ,
            4 : "island5" ,
            5 : "island6" ,
            6 : "island7" ,
          }; 
          
  var small = document.getElementById(small[number]);
  var island = document.getElementById(island[number]);
  var big = document.getElementById(big[number]);
  small.style.opacity = 1;
  big.style.opacity = 0;
  island.style.zIndex = 2;
}