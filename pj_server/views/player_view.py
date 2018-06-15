# -*- coding: utf-8 -*-
 
import os,sys,json,time,random
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from database import models
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def update_fangka(request):
	fangka_num = int(request.POST['fangka_num']);
	user_id = request.POST['player_id'];
	uobj =  models.player.objects.get(id=user_id)

	print uobj.fangka_num
	uobj.fangka_num = uobj.fangka_num + fangka_num;
	uobj.fangka_history = uobj.fangka_history + fangka_num;
	uobj.save()

	buyfangka = models.buy_fangka(order_id=request.POST["order_id"],
			player_id = user_id,
			fangka_num=fangka_num,
			creat_time=request.POST["creat_time"],
			pay_time=request.POST["creat_time"],
			danjia=request.POST["danjia"],
			zongjia=request.POST["zongjia"],
			status=1)
	buyfangka.save();
	return HttpResponse(json.dumps({'code':200,'msg':'修改成功'}))

@csrf_exempt
@login_required
def get_player_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	players =  models.player.objects.all()
	for user in players:
		if user.sex == 1:
			user.sex = '男';
		else:
			user.sex = '女';
		time_local = time.localtime(user.createTime/1000)
		#转换成新的时间格式(2016-05-05 20:28:54)
		user.createTime = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	content = {};

	content["cur_page"] = page_id
	content["length"] = len(players)
	content["users"] = players
	xml = render_to_response("admin/equipment-players.html",content)
	return xml;

@csrf_exempt
@login_required
def search_player_item(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	param = request.GET['param'];
	players =  models.player.objects.all().filter(nick_name=param)
	for user in players:
		if user.sex == 1:
			user.sex = '男';
		else:
			user.sex = '女';
		time_local = time.localtime(user.createTime/1000)
		#转换成新的时间格式(2016-05-05 20:28:54)
		user.createTime = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	content = {};

	content["cur_page"] = 1
	content["length"] = len(players)
	content["users"] = players
	xml = render_to_response("admin/equipment-players.html",content)
	return xml;

@csrf_exempt
@login_required
def get_player_by_id(request):
	if request.method == 'GET':
		id = request.GET["id"]
		user = models.player.objects.get(id=id)
		if user.sex == 1:
			user.sex = '男';
		else:
			user.sex = '女';
		time_local = time.localtime(user.createTime/1000)
		#转换成新的时间格式(2016-05-05 20:28:54)
		user.createTime = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

		time_local = time.localtime(user.lastLoginTime/1000)
		user.lastLoginTime = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

		xml = render_to_response("admin/equipment-detail-player.html",{'user':user})
		return xml;
	else:
		id = request.POST["id"]
		user = models.player.objects.get(id=id)
		content = {};
		content["user"] = {};
		content["user"]['id'] = user.id;
		content["user"]['fangka_num'] = user.fangka_num;
		if not user.gonghui_id is None:
			gonghui = models.gonghui.objects.get(gonghui_id=user.gonghui_id)
			content["gonghui"] = {}
			content["gonghui"]["danjia"] = gonghui.danjia;

		content['code'] = 200;
		return HttpResponse(json.dumps(content))
