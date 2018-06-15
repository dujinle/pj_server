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
from views import download_view,admin_view,player_view,gonghui_view,gonggao_view,records_view

urlpatterns = [
	url(r'^$', download_view.index),
	url(r'^index$', download_view.index),
	url(r'^open_app$', download_view.open_app),
	url(r'^open_app_dw$', download_view.open_app_dw),
	url(r'^download_app$', download_view.download_app),
	url(r'^admin$', admin_view.login),
	url(r'^admin/onlogin$', admin_view.onlogin),
	url(r'^admin/login_out$', admin_view.login_out),
	url(r'^admin/equipment$', admin_view.equipment),
	url(r'^admin/update_fangka$', player_view.update_fangka),
	url(r'^admin/get_player$', player_view.get_player_page),
	url(r'^admin/get_player_by_id$', player_view.get_player_by_id),
	url(r'^admin/search_player_item$', player_view.search_player_item),
	url(r'^admin/get_gonghui$', gonghui_view.get_gonghui_page),
	url(r'^admin/get_gonghui_ans$', gonghui_view.get_gonghui_ans_page),
	url(r'^admin/add_gonghui$', gonghui_view.add_gonghui),
	url(r'^admin/add_gonghui_ans$', gonghui_view.add_gonghui_ans),
	url(r'^admin/to_add_gonghui$', gonghui_view.to_add_gonghui),
	url(r'^admin/search_gonghui_item$', gonghui_view.search_gonghui_item),
	url(r'^admin/del_gonghui_item$', gonghui_view.del_gonghui_item),
	url(r'^admin/del_gonghui_ans_item$', gonghui_view.del_gonghui_ans_item),
	url(r'^admin/get_fangka_order$', records_view.get_fangka_order_page),
	url(r'^admin/get_xufangka$', records_view.get_xufangka_page),
	url(r'^admin/get_gonggao$', gonggao_view.get_gonggao_page)
]
