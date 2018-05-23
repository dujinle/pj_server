// JavaScript Documentfunction 
function modify_fangka(user_id){
	var fangka_num = document.getElementById("fangka_num");
	if (fangka_num.value == ""){
		alert("房卡数据无效");
	} else{
		$.ajax({
			type: "POST",
			url: "update_fangka",
			data:{'fangka_num':fangka_num.value,'id':user_id},
			dataType: "json",
			success: function(data){
				console.log(data);
				if(data.code == 200){
					alert("修改成功");
				}else{
					alert(data.msg);
				}
			}
		});
	}
}
