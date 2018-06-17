# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from django.contrib import admin

from database.models import player,mana_user,gonghui,gonghui_ans,xufangka,buy_fangka,game_broadcast

admin.site.register(player)
admin.site.register(mana_user)
admin.site.register(gonghui)
admin.site.register(gonghui_ans)
admin.site.register(xufangka)
admin.site.register(buy_fangka)
admin.site.register(game_broadcast)

# Register your models here.
