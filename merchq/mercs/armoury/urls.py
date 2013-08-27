from django.conf.urls import patterns, url

from mercs.armoury import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<force_id>\d+)/$', views.force_armoury, name='force_armoury'),
    url(r'^vehicle/(?P<vehicle_id>\d+)/$', views.vehicle_details, name='force_armoury'),
    url(r'^vehicle/sell/(?P<vehicle_id>\d+)/$', views.sell_vehicle, name='force_armoury'),
    url(r'^vehicle/sell/(?P<vehicle_id>\d+)/(?P<confirmed>[a-z]+)/$', 
        views.sell_vehicle, 
        name='force_armoury'),
)

