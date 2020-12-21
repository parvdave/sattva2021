
if ($(window).width() < 700) {
   document.getElementById('bgMap').style.marginTop = '0px';
}

function viewevents(number) {
  var island = { 1 : "one" , 
          2 : "two" ,
          3 : "three" ,
          4 : "four" ,
          5 : "five" ,
          6 : "six" ,
          7 : "seven" ,
          8 : "eight" ,
        };
  var event = island[number] + "events";
  document.getElementById(event).style.display = 'block';
}

function viewisland(number) {
  var islands = document.getElementsByClassName("islands");
  var bgIsland = document.getElementById("bgIsland");
  var dict = { 1 : "./static/images/islands/withflag/Management.png" , 
            2 : "./static/images/islands/withflag/Informals.png" ,
            3 : "./static/images/islands/withflag/LAFA.png" ,
            5 : "./static/images/islands/withflag/Sports.png" ,
            6 : "./static/images/islands/withflag/Photography.png" ,
            7 : "./static/images/islands/withflag/Workshops.png" ,
            8 : "./static/images/islands/withflag/Pa.png" ,
          };
          
  for (var i = 0; i < islands.length; i++) {
  islands[i].style.display = 'none';
  }
  bgIsland.src = dict[number];
  viewevents(number);
}

function imgHover(number) {
  if ( $(window).width()>= '900') {
    var big = { 0 : "big1" , 
              1 : "big2" ,
              2 : "big3" ,
              3 : "big4" ,
              4 : "big5" ,
              5 : "big6" ,
              6 : "big7" ,
              7 : "big8" ,
            };

    var small = { 0 : "small1" , 
              1 : "small2" ,
              2 : "small3" ,
              3 : "small4" ,
              4 : "small5" ,
              5 : "small6" ,
              6 : "small7" ,
              7 : "small8" ,
            };
    var island = { 0 : "island1" , 
              1 : "island2" ,
              2 : "island3" ,
              3 : "island4" ,
              4 : "island5" ,
              5 : "island6" ,
              6 : "island7" ,
              7 : "island8" ,
            }; 

    var small = document.getElementById(small[number]);
    var big = document.getElementById(big[number]);
    var island = document.getElementById(island[number]);
    small.style.opacity = 0;
    big.style.opacity = 1;
    island.style.zIndex = 3;
  }
}

function imgOut(number) {
  if ( $(window).width()>= '900') {
    var big = { 0 : "big1" , 
              1 : "big2" ,
              2 : "big3" ,
              3 : "big4" ,
              4 : "big5" ,
              5 : "big6" ,
              6 : "big7" ,
              7 : "big8" ,
            };

    var small = { 0 : "small1" , 
              1 : "small2" ,
              2 : "small3" ,
              3 : "small4" ,
              4 : "small5" ,
              5 : "small6" ,
              6 : "small7" ,
              7 : "small8" ,
            };
    var island = { 0 : "island1" , 
              1 : "island2" ,
              2 : "island3" ,
              3 : "island4" ,
              4 : "island5" ,
              5 : "island6" ,
              6 : "island7" ,
              7 : "island8" ,
            }; 
            
    var small = document.getElementById(small[number]);
    var island = document.getElementById(island[number]);
    var big = document.getElementById(big[number]);
    small.style.opacity = 1;
    big.style.opacity = 0;
    island.style.zIndex = 2;
  }

}