from django.conf.urls import url
from django.contrib import admin
from zhaopin import views

urlpatterns = [
    url(r'^index/(?P<pIndex>[0-9]+)$',views.index,name='index'),
    url(r'^search/(?P<pIndex>[0-9]+)$',views.search,name='search'),
]
