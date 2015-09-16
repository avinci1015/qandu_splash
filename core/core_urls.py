from django.conf.urls import patterns, include, url from .views import *

urlspatterns = patterns ('',
                         url(r'^$', Home.as_view(), name='home'),)