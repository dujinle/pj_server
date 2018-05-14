# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
import os,sys
from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper

def download_app(request):
	tag = request.GET.get('tag');
	print tag
	file_dstpath = 'enjoy_paijiu-release.apk';
	dw_app_name = "畅游牌九.apk";
	if tag == "iphone":
		file_dstpath = 'enjoy_paijiu-release.app';
		dw_app_name = "畅游牌九.app";
	# add uid to the filename if the requesting user is authenticated
	response = HttpResponse()
	response['Content_Type']='application/octet-stream'
	response["Content-Disposition"] = "attachment; filename={0}".format(dw_app_name)
	response['Content-Length'] = os.path.getsize('/var/webserver/nginx/myapp/download/' + file_dstpath)
#	response["Content-Disposition"] = "attachment; filename=\""+dw_app_name + "\""
	response['X-Accel-Redirect'] = "/get_file/" + file_dstpath
	print response
	return response
