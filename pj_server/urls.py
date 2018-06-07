"""pj_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import view
from views import download_view
from views import admin_view
urlpatterns = [
	url(r'^$', download_view.index),
	url(r'^index$', download_view.index),
	url(r'^open_app$', download_view.open_app),
	url(r'^open_app_dw$', download_view.open_app_dw),
	url(r'^download_app$', download_view.download_app),
	url(r'^admin$', admin_view.login),
	url(r'^onlogin$', admin_view.onlogin),
	url(r'^equipment$', admin_view.equipment),
	url(r'^update_fangka$', admin_view.update_fangka),
	url(r'^get_player$', admin_view.get_player_page),
	url(r'^get_player_by_id$', admin_view.get_player_by_id),
	url(r'^get_gonghui$', admin_view.get_gonghui_page),
	url(r'^add_gonghui$', admin_view.add_gonghui),
	url(r'^get_gonghui_ans$', admin_view.get_gonghui_ans_page),
	url(r'^add_gonghui_ans$', admin_view.add_gonghui_ans),
	url(r'^to_add_gonghui$', admin_view.to_add_gonghui),
	url(r'^get_fangka_order$', admin_view.get_fangka_order_page),
	url(r'^get_xufangka$', admin_view.get_xufangka_page),
	url(r'^get_gonggao$', admin_view.get_gonggao_page),
	url(r'^search_player_item$', admin_view.search_player_item),
	url(r'^search_gonghui_item$', admin_view.search_gonghui_item)
]
