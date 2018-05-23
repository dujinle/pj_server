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
