# -*- coding: utf-8 -*-

#   Copyright 2013 Tuukka Turto
#
#   This file is part of unexpected-raptor.
#
#   unexpected-raptor is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   unexpected-raptor is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with unexpected-raptor.  If not, see <http://www.gnu.org/licenses/>.

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

