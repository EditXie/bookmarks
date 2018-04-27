#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018/4/27 21:36
@author: Edit Xie
@file: urls.py
功能描述：

"""
from django.conf.urls import url
from images.views import *

urlpatterns = [
    url(r'^create/$', image_created, name='create'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        image_detail, name='detail'),
    url(r'^like/$', image_like, name='like'),
    url(r'^$', image_list, name='list'),
]