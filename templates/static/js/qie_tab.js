// JavaScript Documentfunction 
function set_current(name){
	var tab = document.getElementById("player");
	var tab2 = document.getElementById("gonghui");
	var tab3 = document.getElementById("gonghui_ans");
	var tab4 = document.getElementById("buyfangka");
	var tab5 = document.getElementById("gonggao");
	var tab6 = document.getElementById("xufangka");
	tab.className = "";
	tab2.className = "";
	tab3.className = "";
	tab4.className = "";
	tab5.className = "";
	tab6.className = "";
	var tab = document.getElementById(name);
	tab.className = "current";
}

function get_player(page){
	set_current("player");
	$.ajax({
		type: "GET",
		url: "/admin/get_player?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function get_player_by_id(id){
	$.ajax({
		type: "GET",
		url: "/admin/get_player_by_id?id="+id,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function get_gonggao_by_id(id){
	$.ajax({
		type: "GET",
		url: "/admin/get_gonggao_by_id?id="+id,
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
		url: "/admin/get_gonghui?page="+page,
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
		url: "/admin/get_gonggao?page="+page,
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
		url: "/admin/get_gonghui_ans?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function to_add_gonghui(id){
	$.ajax({
		type: "GET",
		url: "/admin/to_add_gonghui?id="+id,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function add_gonghui(){
	var content = {}
	content["gonghui_id"] = document.getElementById("gonghui_id").innerHTML;
	content["gonghui_ans_id"] = document.getElementById("gonghui_ans_id").innerHTML;
	content["fangka_num"] = document.getElementById("fangka_num").innerHTML;
	$.ajax({
		type: "POST",
		url: "/admin/add_gonghui",
		data:content,
		dataType:"json",
		success: function(data){
			console.log(data);
			alert(data.msg);
		}
	});
}

function get_fangka_order(page){
	set_current("buyfangka");
	$.ajax({
		type: "GET",
		url: "/admin/get_fangka_order?page="+page,
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
		url: "/admin/get_gonggao?page="+page,
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
		url: "/admin/get_xufangka?page="+page,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function get_item(type){
	var param = document.getElementById("text_id").value;
	var url = null;
	if(type == 'player'){
		url = '/admin/search_player_item?param=' + param
	}else if(type == 'gonghui'){
		url = '/admin/search_gonghui_item?param=' + param
	}else if(type == 'gonghui_ans'){
		url = '/admin/search_gonghui_ans_item?param=' + param
	}else if(type == 'fangka_order'){
		url = '/admin/search_fangka_order_item?param=' + param
	}else if(type == 'xufangka'){
		url = '/admin/search_xufangka_item?param=' + param
	}
	$.ajax({
		type: "GET",
		url: url,
		success: function(data){
			var div = document.getElementById("content");
			div.innerHTML = data;
			console.log(data);
		}
	});
}

function del_item(type,param){
	var url = null;
	if(type == 'player'){
		url = '/admin/del_player_item'
	}else if(type == 'gonghui'){
		url = '/admin/del_gonghui_item'
	}else if(type == 'gonghui_ans'){
		url = '/admin/del_gonghui_ans_item'
	}else if(type == 'fangka_order'){
		url = '/admin/del_fangka_order_item'
	}else if(type == 'xufangka'){
		url = '/admin/del_xufangka_item'
	}
	var data = {};
	data["ids"] = param;
	$.ajax({
		type: "POST",
		url: url,
		data: data,
		dataType:'json',
		success: function(data){
			window.location.reload();
		}
	});
}

function add_item(type,cb){
	var param = {};
	var url = null;
	if(type == "gonghui_ans"){
		param["player_id"] = document.getElementById("player_id").value;
		param["player_name"] = document.getElementById("player_name").value;
		param["telphone"] = document.getElementById("telphone").value;
		param["gonghui_name"] = document.getElementById("gonghui_name").value;
		var objs = document.getElementById("select");
		var item = objs.options[objs.selectedIndex].value;
		param["money"] = item;
		param["level"] = objs.selectedIndex;
		param["creat_time"] = Date.now();
		url = "/admin/add_gonghui_ans";
	}
	$.ajax({
		type: "POST",
		url: url,
		data:param,
		dataType:'json',
		success: function(data){
			cb();
			console.log(data);
		}
	});
}

function select_level(){
	var objs = document.getElementById("select");
	var item = objs.options[objs.selectedIndex].value;
	var money = document.getElementById("money");
	money.innerHTML = item + "元";
}
