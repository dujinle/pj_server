# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import StreamingHttpResponse

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
	def file_iterator(file_name, chunk_size=512):
		with open(file_name,'rb') as f: #如果不加‘rb’以二进制方式打开，文件流中遇到特殊字符会终止下载，下载下来的文件不完整
			while True:
				c = f.read(chunk_size)
				if c:
					yield c
				else:
					break

	try:
		if tag == 'android':
			file_dstpath = '/home/ubuntu/pj_server/templates/static/download/enjoy_paijiu-release.apk';
			response = StreamingHttpResponse(file_iterator(file_dstpath))
			response['Content-Type'] = 'application/octet-stream'
			response['Content-Disposition'] = 'attachment;filename="畅游牌九.apk"' #此处kwargs['fname']是要下载的文件的文件名称
			return response
		else:
			file_dstpath = '/home/ubuntu/pj_server/templates/static/download/enjoy_paijiu-release.app';
			response = StreamingHttpResponse(file_iterator(file_dstpath))
			response['Content-Type'] = 'application/octet-stream'
			response['Content-Disposition'] = 'attachment;filename="畅游牌九.app"' #此处kwargs['fname']是要下载的文件的文件名称
			return response
	except Exception as e:
		pass;

