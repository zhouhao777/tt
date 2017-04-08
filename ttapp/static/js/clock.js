// function timeCount(){
// 	var date = new Date;
// 	var time = date.getHours()
// 	document.getElementById("time").innerHTML=date.getHours()+":"+date.getMinutes()+":"date.getSeconds();
// }
// setTimeout("timedCount()",1000);


// var num=0;
// function startCount() {
// 	document.getElementById('count').value=num;
// 	num=num+1;
// 	setTimeout("startCount()",1000);
// }
// setTimeout("startCount()",1000);



var attime;
function clock(){
	var time=new Date();          
	attime=time.getHours()+":"+time.getMinutes()+":"+time.getSeconds();
	document.getElementById("clock").value = attime;
}
setInterval(clock,1000);