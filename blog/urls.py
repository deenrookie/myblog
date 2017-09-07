# -*-coding:utf-8-*-
__author__ = 'Deen'

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^post_list$', views.post_list, name='post_list'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
]
