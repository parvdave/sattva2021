today=new Date();

const cmas=new Date(today.getFullYear()+1, 0, 6); //2021 Jan 06
console.log(today.getFullYear())
console.log(cmas);
if (today.getMonth()==11 && today.getDate()>25) {
	cmas.setFullYear(cmas.getFullYear()+1); 
}

const one_day=1000*60*60*24;
var remdays = `${Math.ceil((cmas.getTime()-today.getTime())/(one_day))}`;

for(let i=1; i <=remdays; i++) {
	setTimeout(function(){
		document.getElementById('remdays').innerHTML = i;
	}, 40*i);

	if(i == remdays) {
		break;
	}
}

document.querySelector("body").addEventListener("mousemove", needleMove);

function needleMove() {
  var needle = document.querySelector(".needle");
  let x = (needle.getBoundingClientRect().left) - (needle.clientWidth / 2);
  let y = (needle.getBoundingClientRect().top) - (needle.clientHeight / 2);
  let radian = Math.atan2(event.pageX - x, event.pageY - y);
  let rot = (radian * (180 / Math.PI) * -1) + 270;
  console.log(event.PageY - y);
  needle.style.transform = "rotate(" + rot * 2 + "deg)";
}

var is_safari = navigator.userAgent.indexOf("Safari") > -1;

window.onload = function() {
	document.getElementById("mobmenu").classList.remove("pulldown");
  	document.getElementById("mobmenu").classList.add("bounce");
  	document.getElementById("mobmenu").classList.add("bounced");
  	
  	if (navigator.userAgent.indexOf('Safari') != -1 && navigator.userAgent.indexOf('Chrome') == -1) {
  		document.getElementById("mobmenu").style.marginTop = '-71vh';
  	}
  	else {
  		document.getElementById("mobmenu").style.marginTop = '-78vh';
  	}

	setTimeout(function() {
		document.getElementById("mobmenu").classList.remove("bounced");
		document.getElementById("mobmenu").classList.add("bounceu");
  		document.getElementById("mobmenu").style.marginTop = '-81vh';
  	  	if (navigator.userAgent.indexOf('Safari') != -1 && navigator.userAgent.indexOf('Chrome') == -1) {
	  		document.getElementById("mobmenu").style.marginTop = '-75vh';
	  	}
	  	else {
	  		document.getElementById("mobmenu").style.marginTop = '-81vh';
	  	}
	}, 750)
	document.getElementById("mobmenu").classList.add("pulldown");
	if ($(window).width() < 960) {
		
	}

};

var c = 0;

function ourteam() {
	$('#ourteam')
  		.modal('show')
	;
	var vid = document.getElementById("scrollvid1");
	vid.play();
}

function aboutus() {
	document.getElementById("abouttab1").classList.add("active");
	document.getElementById("abouttab2").classList.remove("active");
	document.getElementById("aboutseg1").classList.add("active");
	document.getElementById("aboutseg2").classList.remove("active");
	$('#aboutus')
  		.modal('show')
	;
	var vid = document.getElementById("scrollvid5");
	vid.play();
}

function contactus() {
	$('#contactus')
  		.modal('show')
	;
	var vid = document.getElementById("scrollvid4");
	vid.play();
}

function aftermovie() {
	$('#aftermovie')
  		.modal('show')
	;
	var vid = document.getElementById("scrollvid3");
	vid.play();
}

function spons() {
	document.getElementById("abouttab1").classList.remove("active");
	document.getElementById("abouttab2").classList.add("active");
	document.getElementById("aboutseg1").classList.remove("active");
	document.getElementById("aboutseg2").classList.add("active");	
	$('#aboutus')
  		.modal('show')
	;
	var vid = document.getElementById("scrollvid5");
	vid.play();
}


$('.menu .item')
	.tab()
;

var pull = 0;

function pulldown() {
	if(pull==0){
		document.getElementById("mobmenu").classList.remove("pullu");
	  	document.getElementById("mobmenu").classList.add("pulld");
	  	document.getElementById("mobmenu").style.marginTop = '0vh';
		setTimeout(function() {
			document.getElementById('pulltext').innerHTML = 'Back to Map';
		}, 700)
		pull=1;
	}
	else if(pull==1) {
	  	document.getElementById("mobmenu").classList.remove("pulld");
  		document.getElementById("mobmenu").classList.add("pullu");
  	  	if (navigator.userAgent.indexOf('Safari') != -1 && navigator.userAgent.indexOf('Chrome') == -1) {
	  		document.getElementById("mobmenu").style.marginTop = '-75vh';
	  	}
	  	else {
	  		document.getElementById("mobmenu").style.marginTop = '-81vh';
	  	}
		setTimeout(function() {
			document.getElementById('pulltext').innerHTML = 'Menu';
		}, 700)
		pull=0;		
	}
}