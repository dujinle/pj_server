# -*- coding: utf-8 -*-
 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.safestring import mark_safe
import os,sys,json,time
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

@login_required
def get_player(request):
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
	return render(request,'equipment-detail.html',{'username':'admin','user':user});

@csrf_exempt
@login_required
def update_fangka(request):
	fangka_num = request.POST['fangka_num'];
	user_id = request.POST['id'];
	uobj =  models.player.objects.get(id=user_id)

	print uobj.fangka_num
	add = int(fangka_num) - uobj.fangka_num;
	if add >= 0:
		uobj.fangka_num = fangka_num;
		uobj.fangka_history = uobj.fangka_history + add;
		uobj.save()
#		return HttpResponseRedirect('/equipment')
		return HttpResponse(json.dumps({'code':200,'msg':'修改成功'}))
#		print 'go into equipment'
#		return render(request,'hello.html',{'username':username})
	else:
		return HttpResponse(json.dumps({'code':201,'msg':'房卡的数量在减少'}))

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
def get_gonghui_ans_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	items =  models.gonghui_ans.objects.all()
	content = {};

	content["cur_page"] = page_id
	content["length"] = len(items)
	content["items"] = items
	xml = render_to_response("equipment-gonghui_ans.html",content)
	return xml;

@csrf_exempt
@login_required
def get_fangka_order_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	items =  models.buy_fangka.objects.all()
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
