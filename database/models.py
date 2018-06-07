# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

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

class mana_user(models.Model):
	id = models.IntegerField(primary_key=True,unique=True);
	username = models.CharField(max_length=32,verbose_name="用户名");
	password = models.CharField(max_length=32,verbose_name="密码");
	level = models.IntegerField(verbose_name="权限");

	class Meta:
		db_table = "mana_user";
		verbose_name = "管理员账户";
		ordering = ['id'];

class gonghui(models.Model):
	id = models.IntegerField(primary_key=True,unique=True);
	gonghui_id = models.CharField(max_length=16,verbose_name="工会ID");
	player_id = models.IntegerField(verbose_name="用户ID");
	player_name = models.CharField(max_length=64,verbose_name="玩家名称");
	renshu = models.IntegerField(verbose_name="人数");
	telphone = models.CharField(max_length=20,verbose_name="电话");
	level = models.IntegerField(verbose_name="等级");
	fangka_num = models.IntegerField(verbose_name="房卡数量");
	danjia = models.FloatField(verbose_name="房卡单价");
	gonghui_name = models.CharField(max_length=64,verbose_name="工会名称");
	gonggao = models.CharField(max_length=240,verbose_name="工会公告");
	xuanyan = models.CharField(max_length=240,verbose_name = "工会宣言");

	class Meta:
		db_table = "gonghui";
		verbose_name = "工会表";
		ordering = ["id"];

class gonghui_ans(models.Model):
	id = models.IntegerField(primary_key=True,unique=True);
	player_id = models.IntegerField(verbose_name="用户ID");
	player_name = models.CharField(max_length=64,verbose_name="玩家名称");
	telphone = models.CharField(max_length=20,verbose_name="电话");
	level = models.IntegerField(verbose_name="等级");
	gonghui_name = models.CharField(max_length=64,verbose_name="工会名称");
	money = models.FloatField(verbose_name="金额");
	creat_time = models.BigIntegerField(verbose_name="创建时间");
	status = models.IntegerField(verbose_name = "状态");

	class Meta:
		db_table = "gonghui_ans";
		verbose_name = "工会申请表";
		ordering = ["id"];

class xufangka(models.Model):
	id = models.IntegerField(primary_key=True,unique=True);
	gonghui_id = models.CharField(max_length=16,verbose_name="工会ID");
	player_id = player_id = models.IntegerField(verbose_name="用户ID");
	phone_num = models.CharField(max_length=20,verbose_name="电话");
	player_name = models.CharField(max_length=64,verbose_name="玩家名称");
	creat_time = models.BigIntegerField(verbose_name="创建时间");
	xuaka_status = models.IntegerField(verbose_name = "状态");

	class Meta:
		db_table = "xufangka";
		verbose_name = "续房卡表";
		ordering = ["id"];

class buy_fangka(models.Model):
	id = models.IntegerField(primary_key=True,unique=True);
	order_id = models.CharField(max_length=32,verbose_name="订单号");
	player_id = models.IntegerField(verbose_name="用户ID");
	fangka_num = models.IntegerField(verbose_name="购买数量");
	status = models.IntegerField(verbose_name = "状态");
	creat_time = models.BigIntegerField(verbose_name="创建时间");
	pay_time = models.BigIntegerField(verbose_name="付费时间");
	danjia = models.FloatField(verbose_name="单价");
	zongjia = models.FloatField(verbose_name="总价");

	class Meta:
		db_table = "buy_fangka";
		verbose_name = "购买房卡记录";
		ordering = ["id"]

#creat model
