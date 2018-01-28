#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url,include
from blog.views import *
urlpatterns = [
    url(r'^$', get_blogs),
    url(r'^detail/(\d+)/$',get_details,name='blog_get_detail'),
]