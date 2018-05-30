# encoding: utf-8
"""biyesheji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from hospital import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/index.html', views.index),
    url(r'^index/admin', views.admin),
    url(r'^index/bingren.html', views.bingren),
    url(r'^index/guahao.html', views.guahao),
    url(r'^index/yiyuan.html', views.yiyuan),
    url(r'^index/keshi.html', views.keshi),
    url(r'^index/yaopin.html', views.yaopin),
    url(r'^index/guanli.html', views.guanli),
    url(r'^index/get_code$', views.get_code),
    url(r'^index/ajax_login$', views.ajax_login),
    url(r'^index/ajax_admin_updatepwd$', views.ajax_admin_updatepwd),
]
