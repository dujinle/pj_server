// JavaScript Documentfunction 
function login(){
	var username = document.getElementById("username");
	var pass = document.getElementById("password");
	var error = document.getElementById("error_tip");
	if (username.value == ""){
		alert("请输入用户名");
	} else if (pass.value  == ""){
		alert("请输入密码");
	} else{
		$.ajax({
			type: "POST",
			url: "admin/onlogin",
			data:{'username':username.value,'password':pass.value},
			dataType: "json",
			success: function(data){
				console.log(data);
				if(data.code != 200){
					error.innerHTML = data.msg;
				}else{
					window.location = "/admin/equipment"
				}
			}
		});
	}
}
