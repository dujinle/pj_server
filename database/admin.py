# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from django.contrib import admin

from database.models import paijiu,player
class paijiuAdmin(admin.ModelAdmin):
	list_display = ('id','name','paixing','score') #添加字段显示
	search_fields = ('name','paixing') #添加快速查询栏

class playerAdmin(admin.ModelAdmin):
	list_display = ('id','nick_name','player_id','phone_num','head_img_url','sex','fangka_num','fangka_history') #添加字段显示
	search_fields = ('nick_name','player_id','phone_num') #添加快速查询栏
#	list_editable = ['fangka_num']
	list_display_links = []
	readonly_fields = [
		'id',
		'nick_name',
		'player_id',
		'phone_num',
		'head_img_url',
		'sex',
		'round_num',
		'all_score',
		'win_num',
		'lose_num',
		'fangka_history',
		'invalid_fangka',
		'gonghui_id',
		'loginCount',
		'createTime',
		'continueLoginDays',
		'lastLoginTime'
	]
	def has_delete_permission(self, request, obj=None):
		return False
	def has_add_permission(self, request):
		return False

admin.site.register(paijiu,paijiuAdmin)
admin.site.register(player,playerAdmin)
# Register your models here.
