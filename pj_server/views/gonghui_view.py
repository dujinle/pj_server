# -*- coding: utf-8 -*-
 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import os,sys,json,time,random
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from database import models
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def get_gonghui_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	items =  models.gonghui.objects.all()
	content = {};

	content["cur_page"] = page_id
	content["length"] = len(items)
	content["items"] = items
	xml = render_to_response("admin/equipment-gonghui.html",content)
	return xml;

@csrf_exempt
@login_required
def search_gonghui_item(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	param = request.GET['param'];
	players =  models.gonghui.objects.all().filter(gonghui_id=param)
	content = {};

	content["cur_page"] = 1
	content["length"] = len(players)
	content["items"] = players
	xml = render_to_response("admin/equipment-gonghui.html",content)
	return xml;

@csrf_exempt
@login_required
def del_gonghui_item(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	print request.POST
	param = request.POST["ids[]"];
	for mid in param:
		gonghui = models.gonghui.objects.get(id=mid)
		if gonghui is not None:
			player = models.player.objects.get(id=gonghui.player_id)
			player.gonghui_id = None;
			player.save()
			gonghui_ans = models.gonghui_ans.objects.get(player_id=gonghui.player_id);
			if gonghui_ans is not None:
				gonghui_ans.delete();
		gonghui.delete()
	return HttpResponse(json.dumps({'code':200,'msg':'删除成功'}))

@csrf_exempt
@login_required
def del_gonghui_ans_item(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	param = request.POST["ids[]"];
	for mid in param:
		gonghui_ans = models.gonghui_ans.objects.get(id=mid)
		if gonghui_ans is not None:
			gonghui_ans.delete()
	return HttpResponse(json.dumps({'code':200,'msg':'删除成功'}))

@csrf_exempt
@login_required
def get_gonghui_ans_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	items =  models.gonghui_ans.objects.all()
	for item in items:
		time_local = time.localtime(item.creat_time/1000)
		#转换成新的时间格式(2016-05-05 20:28:54)
		item.creat_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	content = {};

	content["cur_page"] = page_id
	content["length"] = len(items)
	content["items"] = items
	xml = render_to_response("admin/equipment-gonghui_ans.html",content)
	return xml;

@csrf_exempt
@login_required
def add_gonghui_ans(request):
	player_id = request.POST['player_id'];
	player_name = request.POST['player_name'];
	telphone = request.POST['telphone'];
	gonghui_name = request.POST['gonghui_name'];
	level = request.POST['level'];
	money = request.POST['money'];
	status = -1;

	creat_time = request.POST['creat_time'];

	item = models.gonghui_ans(player_id=player_id,player_name=player_name,telphone=telphone,gonghui_name=gonghui_name,level=level,money=money,status=status,creat_time=creat_time);
	item.save();
	return HttpResponse(json.dumps({'code':200,'msg':'添加成功'}))

@csrf_exempt
@login_required
def to_add_gonghui(request):
	id = request.GET["id"]
	gonghui_ans = models.gonghui_ans.objects.get(id=id)
	content = {}
	content["player_id"] = gonghui_ans.player_id
	content["player_name"] = gonghui_ans.player_name
	content["telphone"] = gonghui_ans.telphone
	content["gonghui_name"] = gonghui_ans.gonghui_name
	content["level"] = gonghui_ans.level
	if gonghui_ans.level == 1:
		content["fangka_num"] = 10000
	elif gonghui_ans.level == 2:
		content["fangka_num"] = 25000
	elif gonghui_ans.level == 3:
		content["fangka_num"] = 40000
	else:
		congent["fangka_num"] = 0
	content["gonghui_ans_id"] = id
	content["gonghui_id"] = random.randint(100000,999999)
	content["danjia"] = 2
	content["gonggao"] = ""
	content["xuanyan"] = ""
	xml = render_to_response("admin/equipment-detail-add_gonghui.html",{"gonghui":content})
	return xml


@csrf_exempt
@login_required
def add_gonghui(request):
	gonghui_id = request.POST["gonghui_id"]
	gonghui_ans_id = request.POST["gonghui_ans_id"]
	fangka_num = request.POST["fangka_num"]
	gonghui_ans = models.gonghui_ans.objects.get(id=gonghui_ans_id)

	gonghui = models.gonghui.objects.filter(gonghui_id=gonghui_id)
	if gonghui is None or len(gonghui) == 0:
		gonghui = models.gonghui(gonghui_id=gonghui_id,
			player_id=gonghui_ans.player_id,
			player_name=gonghui_ans.player_name,
			renshu=0,
			telphone=gonghui_ans.telphone,
			level=gonghui_ans.level,
			fangka_num=fangka_num,
			danjia=2,
			gonghui_name=gonghui_ans.gonghui_name,
			gonggao="",
			xuanyan=""
		)
		gonghui.save();
		gonghui_ans.status = 1;
		gonghui_ans.save();
		player = models.player.objects.get(id=gonghui_ans.player_id)
		player.gonghui_id = gonghui_id
		player.save();
		return HttpResponse(json.dumps({'code':200,'msg':'添加成功'}))
	else:
		return HttpResponse(json.dumps({'code':200,'msg':'已经添加完成'}))
