# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import FileResponse

def hello(request):
	context = {}
	context['hello'] = 'Hello World!'
	return render(request, 'hello.html', context)

def test(request):
	return render(request, 'test.html')

def download(request):
	context = {}
	context['hello'] = 'Hello World!'
	return render(request, 'download.html', context)

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

def open_app_dw(request):
	content = {};
	room_num = request.GET.get('room_num');
	rid = request.GET.get('rid');
	name = request.GET.get('name');
	content['room_num'] = room_num;
	content['rid'] = rid;
	content['name'] = name;
	return render(request, 'open_app_dw.html',content);

def download_app(request):
	tag = request.GET.get('tag');
	if tag == 'android':
		file=open('/home/ubuntu/pj_server/templates/static/download/enjoy_paijiu-debug.apk','rb')
		response = FileResponse(file)
		response['Content-Type']='application/octet-stream'
		response['Content-Disposition']='attachment;filename="test_app.apk"'
		return response
	else:
		file=open('/home/ubuntu/pj_server/templates/static/download/test_app.app','rb')
		response = FileResponse(file)
		response['Content-Type']='application/octet-stream'
		response['Content-Disposition']='attachment;filename="test_app.app"'
		return response
