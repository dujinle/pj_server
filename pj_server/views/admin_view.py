# -*- coding: utf-8 -*-
 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from database import models
from django.views.decorators.csrf import csrf_exempt
import json

def login(request):
	return render(request,'admin/login.html')

@csrf_exempt
def onlogin(request):
	username = request.POST['username'];
	password = request.POST['password'];
	user = auth.authenticate(username=username, password=password)
	print username,user
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponse(json.dumps({'code':200,'msg':'正确'}))
	else:
		return HttpResponse(json.dumps({'code':201,'msg':'密码不正确'}))

@login_required
def login_out(request):
	auth.logout(request)
	return HttpResponseRedirect("/admin")

@csrf_exempt
@login_required
def equipment(request):
	user = request.user;
	print 'equipment',user
	return render(request,'admin/equipment.html',{'username':user})
