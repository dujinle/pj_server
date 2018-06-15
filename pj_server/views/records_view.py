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
	xml = render_to_response("admin/equipment-fangka_order.html",content)
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
	xml = render_to_response("admin/equipment-xufangka.html",content)
	return xml;
