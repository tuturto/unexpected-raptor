from django.conf.urls import patterns, url

from mercs.armoury import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
