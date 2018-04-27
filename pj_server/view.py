# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import FileResponse

def hello(request):
	context = {}
	context['hello'] = 'Hello World!'
	return render(request, 'hello.html', context)

def open_app(request):
	content = {};
	room_num = request.GET.get('room_num');
	rid = request.GET.get('rid');
	name = request.GET.get('name');
	content['room_num'] = room_num;
	content['rid'] = rid;
	content['name'] = name;
	print content;
	return render(request, 'open_app.html',content);

def download_app(request):
	file=open('static/download/test_app.apk','rb')
	response = FileResponse(file)
	response['Content-Type']='application/octet-stream'
	response['Content-Disposition']='attachment;filename="test_app.apk"'
	return response
