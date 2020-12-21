var flag = 1;

function flagZero() {
  flag = 0;
}

function flagOne() {
  flag = 1;
}



function uniCharCode(event) {
  console.log(flag);
  var char = event.which || event.keyCode;
  if ((event.keyCode === 65 || event.keyCode === 97) && flag == 1) { 
      aboutus();
  }
  if ((event.keyCode === 77 || event.keyCode === 109) && flag == 1) { 
      aftermovie();
  } 
  if ((event.keyCode === 84 || event.keyCode === 116) && flag == 1) { 
      ourteam();
  } 
  if ((event.keyCode === 67 || event.keyCode === 99) && flag == 1) { 
      contactus();
  }
  if ((event.keyCode === 83 || event.keyCode === 115) && flag == 1) { 
      contactus();
  }
}
