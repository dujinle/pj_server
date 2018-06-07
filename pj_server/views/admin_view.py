# -*- coding: utf-8 -*-
 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.safestring import mark_safe
import os,sys,json,time,random
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from database import models
from django.views.decorators.csrf import csrf_exempt


def login(request):
	return render(request,'login.html')

@csrf_exempt
def onlogin(request):
	username = request.POST['username'];
	password = request.POST['password'];
	user = auth.authenticate(username=username, password=password)
	print user
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponse(json.dumps({'code':200,'msg':'登录成功'}))
	else:
		return HttpResponse(json.dumps({'code':201,'msg':'密码不正确'}))

@login_required
def equipment(request):
	user = request.user;
	return render(request,'equipment.html',{'username':user})

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
	xml = render_to_response("equipment-players.html",content)
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
	xml = render_to_response("equipment-players.html",content)
	return xml;

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
	xml = render_to_response("equipment-gonghui.html",content)
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
	xml = render_to_response("equipment-gonghui.html",content)
	return xml;

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
	xml = render_to_response("equipment-gonghui_ans.html",content)
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
	xml = render_to_response("equipment-detail-add_gonghui.html",{"gonghui":content})
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
		return HttpResponse(json.dumps({'code':200,'msg':'添加成功'}))
	else:
		return HttpResponse(json.dumps({'code':200,'msg':'已经添加完成'}))

@csrf_exempt
@login_required
def get_fangka_order_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	items =  models.buy_fangka.objects.all()
	for item in items:
		time_local = time.localtime(item.creat_time/1000)
		item.creat_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
		time_local = time.localtime(item.pay_time/1000)
		item.pay_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
		if item.status == 1:
			item.status = "完成"
		else:
			item.status = "未完成"
	content = {};

	content["cur_page"] = page_id
	content["length"] = len(items)
	content["items"] = items
	xml = render_to_response("equipment-fangka_order.html",content)
	return xml;

@csrf_exempt
@login_required
def get_xufangka_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	items =  models.xufangka.objects.all()
	content = {};

	content["cur_page"] = page_id
	content["length"] = len(items)
	content["items"] = items
	xml = render_to_response("equipment-xufangka.html",content)
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

		xml = render_to_response("equipment-detail-player.html",{'user':user})
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


@csrf_exempt
@login_required
def get_gonggao_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	items =  models.gonggao.objects.all()
	content = {};

	content["cur_page"] = page_id
	content["length"] = len(items)
	content["items"] = items
	xml = render_to_response("equipment-fangka_order.html",content)
	return xml;
