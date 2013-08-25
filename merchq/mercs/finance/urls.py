from django.conf.urls import patterns, url

from mercs.finance import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<force_id>\d+)/$', views.force_finances, name='force_finances'),
)

