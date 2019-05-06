// JavaScript Documentfunction 
function get_uuid(){
	var uuid = Date.now() + "" + Math.round(Math.random() * 10000);
	return uuid.substring(0,16);
};

function modify_fangka(user_id){
	var fangka_num = document.getElementById("fangka_num").value;
	var gold = document.getElementById("gold").value;
	if (fangka_num == ""){
		alert("房卡数据无效");
	} else{
		$.ajax({
			type: "POST",
			url: "/admin/get_player_by_id",
			data:{'id':user_id},
			dataType: "json",
			success: function(data){
				console.log(data);
				if(data.code == 200){
					var player = data.user;
					var gonghui = data.gonghui;
					var content = {};
					content["order_id"] = get_uuid();
					content["player_id"] = player.id;
					content["fangka_num"] = fangka_num - player.fangka_num;
					content["gold"] = gold - player.gold;
					content["gold_danjia"] = 1;
					content["danjia"] = 2;
					content["zongjia"] = 2 * content["fangka_num"] + content["gold"];
					content["creat_time"] = Date.now();
					document.getElementById("pop_order_id").innerHTML = content["order_id"];
					document.getElementById("pop_player_id").innerHTML = content["player_id"];
					document.getElementById("pop_fangka_num").innerHTML = content["fangka_num"];
					document.getElementById("pop_gold").innerHTML = content["gold"];
					document.getElementById("pop_gold_danjia").innerHTML = 1;
					document.getElementById("pop_danjia").innerHTML = content["danjia"];
					document.getElementById("pop_zongjia").innerHTML = content["zongjia"];
					if(gonghui != null){
						content["danjia"] = gonghui.danjia;
						content["zongjia"] = content["danjia"] * content["fangka_num"] + content["gold"];
						document.getElementById("pop_danjia").innerHTML = content["danjia"];
						document.getElementById("pop_zongjia").innerHTML = content["zongjia"];
					}
					var d = dialog({
						title:"订单信息",
						content:document.getElementById("buyfangka_pop"),
						ok:function(){
							$.ajax({
								type: "POST",
								url: "/admin/update_fangka",
								data:content,
								dataType: "json",
								success: function(data){
									console.log(data);
									var tt = dialog({
										content:data.msg,
										icon:"succeed"
									});
									-tt.show();
									setTimeout(function () {
										tt.close().remove();
										d.close().remove();
									}, 2000);
								}
							});
							return false;
						},
						cancel:function () {},
						okVal:"提交",
						cancelVal:"取消"
					});
					d.show();
				}
			}
		});
	}
}

function modify_gonggao(id){
	var gonggao = document.getElementById("gonggao_content");
	var content = gonggao.value;
	if (content == ""){
		alert("内容不能为空");
	} else{
		var data = {};
		data["id"] = id;
		data["content"] = content;
		$.ajax({
			type: "POST",
			url: "/admin/update_gonggao",
			data:data,
			dataType: "json",
			success: function(data){
				console.log(data);
				var tt = dialog({
					content:data.msg,
					icon:"succeed"
				});
				tt.show();
				setTimeout(function () {
					tt.close().remove();
				}, 2000);
			}
		});
	}
}
