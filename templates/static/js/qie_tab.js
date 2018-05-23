// JavaScript Documentfunction 
function set_current(name){
	var tab = document.getElementById("player");
	var tab2 = document.getElementById("gonghui");
	var tab3 = document.getElementById("gonghui_ans");
	var tab4 = document.getElementById("buyfangka");
	var tab5 = document.getElementById("gonggao");
	tab.className = "";
	tab2.className = "";
	tab3.className = "";
	tab4.className = "";
	tab5.className = "";
	var tab = document.getElementById(name);
	tab.className = "current";
}

function get_player(page){
	set_current("player");
	$.ajax({
		type: "GET",
		url: "get_player?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function get_gonghui(page){
	set_current("gonghui");
	$.ajax({
		type: "GET",
		url: "get_gonghui?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function get_gonghui_ans(page){
	set_current("gonghui_ans");
	$.ajax({
		type: "GET",
		url: "get_gonghui_ans?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function get_fangka_order(page){
	set_current("buyfangka");
	$.ajax({
		type: "GET",
		url: "get_fangka_order?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function get_gonggao(page){
	set_current("gonggao");
	$.ajax({
		type: "GET",
		url: "get_gonggao?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function get_xufangka(page){
	set_current("xufangka");
	$.ajax({
		type: "GET",
		url: "get_xufangka?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}
