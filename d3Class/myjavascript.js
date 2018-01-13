
var isBulbOn = false;

var turnOn = function(){
    document.getElementById ("bulb").src="img/pic_bulbon.gif";
}


var turnOff = function(){
    document.getElementById ("bulb").src="img/pic_bulboff.gif";
}

var change = function(){
    if(isBulbOn){
	turnOff();
	isBulbOn = false;
    }else{
	turnOn();
	isBulbOn = true;
    }
}


