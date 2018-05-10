<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
{% load staticfiles %}
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=2.0, user-scalable=yes" />

<title>打开应用</title>
</head>
		<script type="text/javascript">
			function open_or_download_app() {
				if (navigator.userAgent.match(/(iPhone|iPod|iPad);?/i)) {
					// 判断useragent，当前设备为ios设备
					var loadDateTime = new Date();
					// 设置时间阈值，在规定时间里面没有打开对应App的话，直接去App store进行下载。
					window.setTimeout(function() {
						var timeOutDateTime = new Date();
						if (timeOutDateTime - loadDateTime <2200) {
							window.location = "/index";  // APP下载地址
						} else {
							window.close();
						}
					},2000);
					window.location = "xinchang://enjoypuke?scene=enter_room&room_num={{room_num}}&&rid={{rid}}";　　//ios端URL Schema
				} else if (navigator.userAgent.match(/android/i)) {
					// 判断useragent，当前设备为Android设备
					// 判断useragent，当前设备为ios设备
					var loadDateTime = new Date();
					// 设置时间阈值，在规定时间里面没有打开对应App的话，直接去App store进行下载。
					window.setTimeout(function() {
						var timeOutDateTime = new Date();
						if (timeOutDateTime - loadDateTime < 2200) {
							window.location = "/index";   // APP下载地址
						} else {
							window.close();
						}
					},2000);
					window.location = "xinchang://enjoypuke?scene=enter_room&room_num={{room_num}}&&rid={{rid}}";　　//android端URL Schema
				}
			}
		</script>
	<body onload="open_or_download_app()">
		<p>it is a test ! </p>
	</body>
</html>
