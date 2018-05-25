// JavaScript Documentfunction 
function login(){
	var username = document.getElementById("username");
	var pass = document.getElementById("password");
	if (username.value == ""){
		alert("请输入用户名");
	} else if (pass.value  == ""){
		alert("请输入密码");
	} else{
		$.ajax({
			type: "POST",
			url: "onlogin",
			data:{'username':username.value,'password':pass.value},
			dataType: "json",
			success: function(data){
				if(data.code == 200){
					window.location = "/equipment"
				}
				console.log(data);
			}
		});
	}
}

		//全选
function checkAll() {
	var allCheckBoxs = document.getElementsByName("check");
	var desc = document.getElementById("check_all").value;
	if (desc == "全选") {
		document.getElementById("check_all").value = "全不选";
		for (var i = 0; i < allCheckBoxs.length; i++) {
			allCheckBoxs[i].checked = true;
		}
	} else {
		document.getElementById("check_all").value = "全选";
		for (var i = 0; i < allCheckBoxs.length; i++) {
			allCheckBoxs[i].checked = false;
		}
	}
}
//批量删除
function del() {
	var checkFlag = false;
	var allCheckBoxs = document.getElementsByName("check");
	for (var i = 0; i < allCheckBoxs.length; i++) {
		if (allCheckBoxs[i].checked == true) {
			checkFlag = true;
		}
	}
	if (!checkFlag) {
		var dialog = art.dialog({
			title: "批量删除",
			content: "请先选择至少一条数据",
			icon: "warning",
			ok: true
		});
	} else {
		//提示是否真的删除
		art.dialog("确定要删除么？", 
		function() {
			var dialog = art.dialog({
				title: "批量删除",
				content: "删除成功！",
				icon: "succeed",
				ok: true
			});
		},
		function() {});
	}
}
