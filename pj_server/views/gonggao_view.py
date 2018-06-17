# -*- coding: utf-8 -*-
 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import os,sys,json,time,random
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from database import models
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def get_gonggao_page(request):
	response = HttpResponse()
	response['Content-Type'] = "text/json"
	page_id = request.GET['page'];
	items =  models.game_broadcast.objects.all()
	content = {};
	content["cur_page"] = page_id
	content["length"] = len(items)
	content["items"] = items
	for value in items:
		value.id = value._id
	xml = render_to_response("admin/equipment-gonggao.html",content)
	return xml;

@csrf_exempt
@login_required
def get_gonggao_by_id(request):
	if request.method == 'GET':
		id = request.GET["id"]
		item = models.game_broadcast.objects.get(_id=id)
		print item
		content = {};
		content['id'] = item._id
		content['broadcast_type'] = item.broadcast_type
		content['broadcast_content'] = item.broadcast_content
		xml = render_to_response("admin/equipment-detail-gonggao.html",{'gonggao':content})
		return xml;
	else:
		id = request.POST["id"]
		item = models.game_broadcast.objects.get(_id=id)
		content = {};
		content["item"] = {};
		content["item"]['id'] = item._id
		content["item"]['broadcast_type'] = item.broadcast_type
		content["item"]['broadcast_content'] = item.broadcast_content

		content['code'] = 200;
		return HttpResponse(json.dumps(content))

@csrf_exempt
@login_required
def update_gonggao(request):
	id = request.POST['id'];
	content = request.POST['content']
	uobj =  models.game_broadcast.objects.get(_id=id)
	print id,content
	uobj.broadcast_content = content;
	uobj.save()
	return HttpResponse(json.dumps({'code':200,'msg':'修改成功'}))
