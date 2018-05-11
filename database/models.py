# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class paijiu(models.Model):
	id = models.IntegerField(primary_key=True,unique=True);
	paixing = models.CharField(max_length=32);
	score = models.IntegerField();
	name = models.CharField(max_length=64);
	class Meta:
		db_table = 'paijiu' #自定义表名称为mytable
		verbose_name = '牌九信息表' #指定在admin管理界面中显示的名称 
		#app_label = 'app02'
		ordering = ['id'] 

class player(models.Model):
	id = models.IntegerField(primary_key=True,unique=True);
	player_id = models.CharField(max_length=32,verbose_name="微信ID");
	phone_num = models.CharField(max_length=20,verbose_name="手机号");
	nick_name = models.CharField(max_length=64,verbose_name="微信名称");
	head_img_url = models.CharField(max_length=256);
	sex = models.IntegerField();
	fangka_num = models.IntegerField(verbose_name="房卡数量");
	round_num = models.IntegerField(verbose_name="游戏局数");
	all_score = models.IntegerField(verbose_name="游戏得分");
	win_num = models.IntegerField(verbose_name="胜利局数");
	lose_num = models.IntegerField(verbose_name="失败局数");
	fangka_history = models.IntegerField(verbose_name="购买房卡总数");
	invalid_fangka = models.IntegerField(verbose_name="无效的房卡");
	gonghui_id = models.CharField(max_length=12,verbose_name="工会ID");
	loginCount = models.IntegerField();
	createTime = models.BigIntegerField();
	continueLoginDays = models.IntegerField();
	lastLoginTime = models.BigIntegerField();
	class Meta:
		db_table = 'player';
		verbose_name = '玩家信息表';
		ordering = ['id'];

