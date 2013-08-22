from django.conf.urls import patterns, url

from mercs.personnel import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<force_id>\d+)/$', views.force_personnel, name='force personnel')
)
