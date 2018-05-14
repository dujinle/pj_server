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
from django.contrib import admin
from . import view
from views import download_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^hello$', view.hello),
	url(r'^test$', view.test),
	url(r'^open_app$', view.open_app),
	url(r'^$', view.open_app),
	url(r'^open_app_dw$', view.open_app_dw),
	url(r'^index$', view.open_app_dw),
	url(r'^download_app$', download_view.download_app),
]
