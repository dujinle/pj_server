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
	items =  models.gonggao.objects.all()
	content = {};

	content["cur_page"] = page_id
	content["length"] = len(items)
	content["items"] = items
	xml = render_to_response("admin/equipment-fangka_order.html",content)
	return xml;
