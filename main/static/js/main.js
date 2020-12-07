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

var c = 0;
function openclose() {	
	if(c==0) {
		//console.log(c);
	    document.getElementById("open").src = "images/oyster-open.gif";
	    c=1;
	}
	else{
		//console.log(c);
	    document.getElementById("open").src = "images/oyster-close.gif";
	    c=0;
	}
}

function ourteam() {
	$('#ourteam')
  		.modal('show')
	;
	var vid = document.getElementById("scrollvid1");
	vid.play();
}

function aboutus() {
	$('#aboutus')
  		.modal('show')
	;
	var vid = document.getElementById("scrollvid2");
	vid.play();
}

function contactus() {
	$('#contactus')
  		.modal('show')
	;
}

function aftermovie() {
	$('#aftermovie')
  		.modal('show')
	;
}

$('.menu .item')
	.tab()
;