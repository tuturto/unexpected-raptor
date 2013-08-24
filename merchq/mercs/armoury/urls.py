from django.conf.urls import patterns, url

from mercs.armoury import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<force_id>\d+)/$', views.force_armoury, name='force_armoury'),
)
